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
    return render_template('home.html')


@main.route('/create_account', methods=['GET', 'POST'])
@login_required
def create_account():
    form = AccountForm()
    if form.validate_on_submit():
        new_account = AccountForm(
            username=form.username.data,
            biography=form.biography.data,
            photo_url=form.photo_url.data,
        )
        db.session.add(new_account)
        db.session.commit()
        flash('New Account Created!')
        return redirect(url_for('main.account_detail', account_id=new_account.id))
    return render_template('create_account.html', form=form)
    pass

# @main.route('/create_post', methods=['GET', 'POST'])
#@login_required
# def create_post():
#     pass

# @main.route('/create_comment', methods=['GET', 'POST'])
#@login_required
# def create_comment():
#     pass

# @main.route('/user/<user_id>', methods=['GET', 'POST'])
#@login_required
# def user_detail(user_id):
#     pass

# @main.route('/account/<account_id>', methods=['GET', 'POST'])
#@login_required
# def account_detail(account_id):
#     pass

# @main.route('/post/<post_id>', methods=['GET', 'POST'])
#@login_required
# def post_detail(post_id):
#     pass

# @main.route('/comment/<comment_id>', methods=['GET', 'POST'])
#@login_required
# def comment_detail(comment_id):
#     pass

