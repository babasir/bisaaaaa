from app import db

class Book(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    published_at = db.Column(db.String())

    def __init__(self, content):
        self.content = content
        self.published = published_at

    def __repr__(self):
        return '<id {}>'.format(self.id)
