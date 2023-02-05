from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
# from only_pets.models import GroceryStore, GroceryItem
# from only_pets.forms import GroceryStoreForm, GroceryItemForm
from only_pets.extensions import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    
    return render_template('home.html')

# @main.route('/create_user', methods=['GET', 'POST'])
# def create_post():
#     pass

# @main.route('/create_account', methods=['GET', 'POST'])
# def create_account():
#     pass

# @main.route('/create_post', methods=['GET', 'POST'])
# def create_post():
#     pass

# @main.route('/create_comment', methods=['GET', 'POST'])
# def create_comment():
#     pass

# @main.route('/user/<user_id>', methods=['GET', 'POST'])
# def user_detail(user_id):
#     pass

# @main.route('/account/<account_id>', methods=['GET', 'POST'])
# def account_detail(account_id):
#     pass

# @main.route('/post/<post_id>', methods=['GET', 'POST'])
# def post_detail(post_id):
#     pass

# @main.route('/comment/<comment_id>', methods=['GET', 'POST'])
# def comment_detail(comment_id):
#     pass

