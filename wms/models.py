from wms import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(400), nullable=False, default="No Address")
    mobno = db.Column(db.Integer,unique=True,default="0000")
    Complain= db.relationship('Complain',backref='author',lazy=True)
    

    def __init__ (self,username,email,image_file,address,mobno,password):
        self.name=username
        self.email=email
        self.image_file=image_file
        self.address=address
        self.mobno=mobno
        self.password=password

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}','{self.address}','{self.mobno}','{self.password}')"

class Complain(db.Model):
    __tablename__ = 'Complain'
    id = db.Column(db.Integer, primary_key=True)
    userid= db.Column(db.Integer,db.ForeignKey('User.id'), nullable=False)
    mob_no=db.Column(db.Integer,nullable=False)
    landmark=db.Column(db.String(200),nullable=False)
    pincode=db.Column(db.Integer,nullable=False)
    tycomp=db.Column(db.String(20),nullable=False) #type of complain
    Complaint=db.Column(db.String(200),nullable=False)
    photo=db.Column(db.String(20), nullable=False, default="default2.jpg")
    dateposted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    


    def __init__(self,mob_no,landmark,pincode,Complaint,photo,dateposted,tycomp):
        
        self.mob_no=mob_no
        self.landmark=landmark
        self.pincode=pincode
        self.Complaint=Complaint
        self.photo=photo
        self.dateposted=dateposted
        self.tycomp=tycomp

    def __repr__(self):
        return f"Complain('{self.mob_no}','{self.landmark}','{self.pincode}','{self.Complaint}','{self.photo}','{self.dateposted}','{self.tycomp}'')"    



class admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")

    def __init__ (self,username,image_file,password):
        self.name=username
        self.image_file=image_file
        self.password=password

    def __repr__(self):
        return f"admin('{self.name}','{self.image_file}','{self.password}')"



class Solved(db.Model):
    __tablename__ = 'Solved'
    id = db.Column(db.Integer, primary_key=True)
    userid= db.Column(db.Integer,db.ForeignKey('User.id'), nullable=False)
    mob_no=db.Column(db.Integer,nullable=False)
    landmark=db.Column(db.String(200),nullable=False)
    pincode=db.Column(db.Integer,nullable=False)
    tycomp=db.Column(db.String(20),nullable=False) #type of complain
    Complaint=db.Column(db.String(200),nullable=False)
    datesaw=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)



    def __init__(self,userid,mob_no,landmark,pincode,Complaint,datesaw,tycomp):
        self.userid=userid
        self.mob_no=mob_no
        self.landmark=landmark
        self.pincode=pincode
        self.Complaint=Complaint
        self.datesaw=datesaw
        self.tycomp=tycomp

    def __repr__(self):
        return f"Complain('{ self.userid}','{self.mob_no}','{self.landmark}','{self.pincode}','{self.Complaint}','{self.datesaw}','{self.tycomp}'')"    



    