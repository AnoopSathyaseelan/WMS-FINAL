from flask import  render_template , url_for, flash, redirect
from wms import app, db, bcrypt
from wms.forms import Registrationform, loginform
from wms.models import User, Complain ,admin ,Solved



@app.route('/')
@app.route("/home")
def home():
    return  render_template("home.html")

@app.route("/about")
def about():
    return  render_template("about.html", title='ABOUT')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = loginform()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/reg", methods=['GET','POST'])
def reg():
    form = Registrationform()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=hashed_password,address=form.Address.data,mobno='00',image_file="default.jpg")
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account Has been Created! Now you can login', 'success')
        return redirect(url_for('home'))
    return  render_template("reg.html", title='REGISTER',form=form)
