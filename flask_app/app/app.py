from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)

posts = [
    {
        'user': 'Elon Musk',
        'text': 'The sun is a theronuclear explosion fyi',
        'location': 'California',
        'likes': 3_000_000,
    },
    {
        'user': 'Sarah Smith',
        'text': 'Excited for school!!!!',
        'location': 'College Park',
        'likes': 87
    }
]

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    bio = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return 'User: %s' % self.name

db.create_all()



@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', message='hello')

@app.route('/about')
def about():
    pass

@app.route('/user/<username>')
def profile(username):
    return render_template('user.html', user=username)

@app.route('/feed')
def feed():
    return render_template('feed.html', posts=posts)


if __name__=='__main__':
    app.run(debug=True)