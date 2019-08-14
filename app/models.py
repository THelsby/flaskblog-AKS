from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return ''.join([
            'User:', self.first_name, ' ', self.last_name, '\r\n',
            'Email: ', self.email])


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.String(10000), nullable=False, unique=True)


    def __repr__(self):

        return ''.join([
            'Author:', self.author, '\r\n',
            'Title: ', self.title, '\r\n', self.content])

