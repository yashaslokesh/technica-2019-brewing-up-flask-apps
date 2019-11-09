
""" This script is not executable, but just provides the examples on how to work
with your database. 
"""

>>> from app import db
>>> from app import User
>>> 
>>> user = User(name='John', bio='What a great day!', email='john@gmail.com', location='France')
>>> 
>>> db.session.add(user)
>>> db.session.commit()
>>> 
>>> User.query.all()
[User: John]
>>> user = User(name='Isabella', bio='What a amazing day!', email='isabel@gmail.com', location='Spain')
>>> 
>>> db.session.add(user)                                                                      
>>> db.session.commit()      
>>> 
>>> User.query.all()                                                                          [User: John, User: Isabella]
>>> User.query.filter_by(location='France').all()
[User: John]
>>> 