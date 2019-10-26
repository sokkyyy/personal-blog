from flask import render_template
from . import main
from flask_login import login_required
from ..models import Post,Comment
from .forms import PostForm,CommentForm

@main.route('/')
def index():

    title = "Home - Ray's Blog"
    return render_template('index.html',title=title)

@main.route('/new-post',methods=['GET','POST'])
@login_required
def new_post():
    form = 