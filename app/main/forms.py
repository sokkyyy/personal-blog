from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField('TITLE:',validators=[Required()])
    content = TextAreaField('BLOG:')
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = StringField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')
