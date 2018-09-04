from app import db, login
from datetime import datetime
from app.models import User


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    __tablename__ = 'posts'
    __searchable__ = ['title', 'subtitle', 'content']
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, index=True)
    subtitle = db.Column(db.String, index=True)
    content = db.Column(db.String, index=True)
    date = db.Column(db.String, index=True, default=datetime.now().strftime('%Y-%m-%d'))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Post %r>' % self.title
    












