from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required,current_user
from ..models import Post,Comment
from .forms import PostForm,CommentForm
from ..requests import get_quotes


@main.route('/')
def index():

    posts = Post.query.all()
    quotes = get_quotes()

    title = "Home - Ray's Blog"
    return render_template('index.html',title=title,posts=posts,quotes=quotes)

@main.route('/new-post',methods=['GET','POST'])
@login_required
def new_post():

    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        new_post = Post(title=title,content=content,user=current_user)
        new_post.save_post()

        return redirect(url_for('.index'))
    
    title = "New Post"
    return render_template('new-post.html',title=title,post_form=form)


@main.route('/post/<post_id>',methods=['GET','POST'])
def post(post_id):
    form = CommentForm()
    post = Post.query.filter_by(id=post_id).first()
    comments = Comment.query.filter_by(post_id=post_id).all()
    
    
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment=comment,post=post,user=current_user)
        new_comment.save_comment()
        return redirect(url_for('.post',post_id=post_id))

    

    title = f"{post.title}"
    return render_template('post.html',title=title,post=post,form=form,comments=comments)

@main.route('/delete/<post_id>/<action>')
@login_required
def delete(post_id,action):
    if action == 'comment':
        comment = Comment.query.filter_by(post_id=post_id).first()
        comment.delete_comment()
        return redirect(url_for('main.post',post_id=post_id))
    elif action == 'post':
        post = Post.query.filter_by(id=post_id).first()
        comments = Comment.query.filter_by(post_id=post_id).all()
        
        for comment in comments:
            comment.delete_comment()
        
        post.delete_post()
        return redirect(url_for('main.index'))

@main.route('/update/<post_id>',methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get(post_id)
    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.save_post()
        return redirect(url_for('main.post',post_id=post.id))
    
    title = "Update Post"
    return render_template('update_post.html',title=title,update_form=form)

