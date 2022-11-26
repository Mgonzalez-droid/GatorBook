#importing applciation instance
from app import app
from models import User, Message, Post, Notification

#adding models to shell context

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification}