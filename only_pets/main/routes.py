"""Import packages and modules."""
from os import abort
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime

import flask_login
from only_pets.models import *
from only_pets.main.forms import *

# Import app and db from events_app package so that we can run app
from only_pets.extensions import app, db, bcrypt

main = Blueprint("main", __name__)

##########################################
#           Home Route                  #
##########################################


@main.route('/')
def homepage():
    all_posts = Post.query.all()
    all_users = User.query.all()
    all_stories = Story.query.all()
    return render_template('home.html',
     all_users=all_users, all_posts=all_posts, all_stories=all_stories)

@main.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).one()
    posts = Post.query.filter(Post.created_by.has(username = username))
    return render_template('profile.html', user=user, posts=posts)


##########################################
#           User Routes                 #
##########################################
@main.route('/create_user', methods=['GET', 'POST'])
@login_required
def create_user():
    form = UserForm()
    #validate form
    if form.is_submitted():
        new_user = User(
            username = form.username.data,
            password = form.password.data,
        )
        db.session.add(new_user)
        db.session.commit()
        flash('New User Created!')
        return redirect(url_for('main.homepage', user_id=new_user.id))
    return render_template('create_user.html', form=form)


##########################################
#           Post Routes                 #
##########################################

#create post
@main.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    #validate form
    if form.is_submitted():
        new_post = Post(
            title = form.title.data,
            caption = form.caption.data,
            photo_url = form.photo_url.data,
            created_by = flask_login.current_user
        )
        db.session.add(new_post)
        db.session.commit()
        flash('New Post Created!')
        return redirect(url_for('main.post_detail', post_id=new_post.id))
    return render_template('create_post.html', form=form)

# read and update post
@main.route('/post/<post_id>', methods=['GET', 'POST'])
@login_required
def post_detail(post_id):
    post = Post.query.get(post_id)
    form = PostForm(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.caption = form.caption.data
        post.photo_url = form.photo_url
        db.session.commit()
        flash ('Post successfully editted.')
        return redirect(url_for('main.post_detail', post_id=post.id))
    return render_template('post_detail.html', post=post, form=form)

# delete post
@main.route('/delete_post/<post_id>', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        abort(404)
    if request.method == 'POST':
        post = Post.query.get(post_id)
        db.session.delete(post)
        db.session.commit()
        flash('Post was deleted successfully', 'success')
        return redirect(url_for('main.homepage'))
    return render_template('post_detail.html', post=post)


##########################################
#           Comment Routes               #
##########################################

@main.route('/add_comment/<post_id>', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get(post_id)
    form = CommentForm(obj=post)
    if form.validate_on_submit():
        new_comment = CommentForm (
            comment = form.comment.data,
            created_by = flask_login.current_user
        )
        db.session.add(new_comment)
        post.all_comments.append(new_comment)
        db.session.commit()
        flash('Comment Added.')
        return redirect(url_for('post_detail.html', post_id=post.id))
    return render_template('create_comment.html', form=form)  

#delete comment
@main.route('/delete_comment/<comment_id>', methods=['GET', 'POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        abort(404)
    if request.method == 'POST':
        comment = Comment.query.get(comment_id)
        db.session.delete(comment)
        db.session.commit()
        flash('Story was deleted successfully', 'success')
        return redirect(url_for('main.homepage'))
    return render_template('post_detail.html', comment=comment)

##########################################
#           Story Routes                 #
##########################################


#create story
@main.route('/create_story', methods=['GET', 'POST'])
@login_required
def create_story():
    form = StoryForm()
    if form.is_submitted():
        new_story = Story(
            photo_url = form.photo_url.data,
            created_by = flask_login.current_user
        )
        db.session.add(new_story)
        db.session.commit()
        flash('New Story Created!')
        return redirect(url_for('main.story_detail', story_id=new_story.id))
    return render_template('create_story.html', form=form)

# read and update story
@main.route('/story/<story_id>', methods=['GET', 'POST'])
@login_required
def story_detail(story_id):
    story = Story.query.get(story_id)
    form = StoryForm(obj=story)
    if form.validate_on_submit():
        story.photo_url = form.photo_url
        db.session.commit()
        flash ('Story successfully editted.')
        return redirect(url_for('main.story_detail', story_id=story.id))
    return render_template('story_detail.html', story=story, form=form)

# delete story
@main.route('/delete_story/<story_id>', methods=['GET', 'POST'])
@login_required
def delete_story(story_id):
    story = Story.query.get(story_id)
    if not story:
        abort(404)
    if request.method == 'POST':
        story = Story.query.get(story_id)
        db.session.delete(story)
        db.session.commit()
        flash('Story was deleted successfully', 'success')
        return redirect(url_for('main.homepage'))
    return render_template('post_detail.html', story=story)
