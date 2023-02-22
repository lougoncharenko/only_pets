from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from flask_login import login_required
from only_pets.models import *
from only_pets.main.forms import *
from only_pets.extensions import app, db
import flask_login

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    all_posts = Posts.query.all()
    return render_template('home.html', all_posts=all_posts)
    return render_template('home.html')


@main.route('/create_account', methods=['GET', 'POST'])
@login_required
def create_account():
    form = AccountForm()
    if form.validate_on_submit():
        new_account = AccountForm(
            username = form.username.data,
            biography = form.biography.data,
            photo_url = form.photo_url.data,
            created_by = flask_login.current_user
        )
        db.session.add(new_account)
        db.session.commit()
        flash('New Account Created!')
        return redirect(url_for('main.account_detail', account_id=new_account.id))
    return render_template('create_account.html', form=form)

@main.route('/account/<account_id>', methods=['GET', 'POST'])
@login_required
def account_detail(account_id):
    account = AccountForm.query.get(account_id)
    form = AccountForm(obj=account)

    if form.validate_on_submit():
        account.username = form.username.data
        account.biography = form.biography.data
        account.photo_url = form.photo_url.data
        db.session.commit()
        flash ('Account successfully updated.')
        return redirect(url_for('main.account_detail', account_id=account.id))
    account = AccountForm.query.get(account_id)
    return render_template('account_detail.html', account=account, form=form)
    

@main.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = PostForm(
            date_posted = form.date_posted.data,
            caption = form.caption.data,
            photo_url = form.photo_url.data,
            created_by = flask_login.current_user
        )
        db.session.add(new_post)
        db.session.commit()
        flash('New Post Created!')
        return redirect(url_for('main.post_detail', post_id=new_post.id))
    return render_template('create_post.html', form=form)

@main.route('/post/<post_id>', methods=['GET', 'POST'])
@login_required
def post_detail(post_id):
    post = PostForm.query.get(post_id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.date_posted = form.date_posted.data
        post.caption = form.caption.data
        post.photo_url = form.photo_url
        db.session.commit()
        flash ('Post successfully editted.')
        return redirect(url_for('main.post_detail', post_id=post.id))
    post = PostForm.query.get(post_id)
    return render_template('post_detail.html', post=post, form=form)
    pass
    

@main.route('/add_comment/<post_id>', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Posts.query.get(post_id)
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
