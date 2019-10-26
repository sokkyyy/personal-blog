from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField('Blog Title',validators=[Required()])
    content = TextAreaField('Write your Blog:',validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = StringField('Thoughts about the Blog',validators=[Required()])
    submit = SubmitField('Comment')
