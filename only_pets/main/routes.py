from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from flask_login import login_required
from only_pets.models import *
from only_pets.main.forms import *
from only_pets.extensions import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    # all_posts = Posts.query.all()
    # return render_template('home.html', all_posts=all_posts)
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
    pass 

@main.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    pass

# @main.route('/create_comment', methods=['GET', 'POST'])
#@login_required
# def create_comment():
#     pass

# @main.route('/user/<user_id>', methods=['GET', 'POST'])
#@login_required
# def user_detail(user_id):
#     pass



# @main.route('/post/<post_id>', methods=['GET', 'POST'])
#@login_required
# def post_detail(post_id):
#     pass

# @main.route('/comment/<comment_id>', methods=['GET', 'POST'])
#@login_required
# def comment_detail(comment_id):
#     pass

