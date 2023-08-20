from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Members(db.Model):
    """ table name : members
        table info 
    - id : index id 
    - name 
    - start: start datetime
    - end: end datetime """
    
    __tablename__ = 'users'
    
    id = db.Column(db.String(20, 'utf8mb4_unicode_ci'), primary_key=True, nullable=False, autoincrement=True)
    pwd = db.Column(db.String(20, 'utf8mb4_unicode_ci'))
    name = db.Column(db.String(20, 'utf8mb4_unicode_ci'))
    email = db.Column(db.String(50, 'utf8mb4_unicode_ci'))
    image = db.Column(db.BLOB)

    def __init__(self, name, email, phone, pwd, image):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.image = image
        self.pwd = pwd