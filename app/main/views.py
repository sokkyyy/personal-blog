from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required,current_user
from ..models import Post,Comment,Subscriber
from .forms import PostForm,CommentForm
from ..requests import get_quotes
from ..email import mail_message
from sqlalchemy import desc
import markdown2


@main.route('/')
def index():

    posts = Post.query.order_by(desc('posted')).all()
    recent = posts[0:2]
    other_posts = posts[2:]
   

    



    quotes = get_quotes()


    title = "Home - Ray's Blog"
    return render_template('index.html',title=title,posts=other_posts,quotes=quotes,recent=recent)

@main.route('/new-post',methods=['GET','POST'])
@login_required
def new_post():

    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        subscribers = Subscriber.query.all()

        new_post = Post(title=title,content=content,user=current_user)
        new_post.save_post()

        for subscriber in subscribers:
            mail_message("New Post from Ray's Blog",'email/new_post',subscriber.email,post=new_post)



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
    user = None
    if current_user.is_authenticated:
        user = current_user.role.name
    else:
        user = "anonymous"
    return render_template('post.html',title=title,post=post,form=form,comments=comments,user=user)

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
    return render_template('new-post.html',title=title,post_form=form)

@main.route('/subscribe')
@login_required
def subscribe():
    email = current_user.email
    subscribed = Subscriber.query.filter_by(email=email).first()

    if not subscribed:
        subscriber = Subscriber(email=email)
        subscriber.save_subscriber()
        
        return redirect(url_for('main.index'))
    