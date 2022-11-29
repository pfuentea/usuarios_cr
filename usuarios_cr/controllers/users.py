from usuarios_cr import app
from flask import request,flash,render_template,redirect,session 
from usuarios_cr.models.user import User



@app.route('/users')
def index():
    usuarios=User.get_all()
    return render_template("all_user.html",usuarios=usuarios)


@app.route('/users/new', methods=['GET'])
def create():
    return render_template("create_user.html")

    
@app.route('/users/new', methods=['POST'])
def new_user():

    print(request.form)

    User.create(request.form)

    return redirect("/users")