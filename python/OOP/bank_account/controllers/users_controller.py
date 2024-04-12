from bank_account import app
from flask import flash, request, render_template, redirect, url_for
from bank_account.models.user_model import User
from bank_account.models.bank_account_model import BankAccount




# John Doe will be our demo user.
# The user dictionary is to simulate info stored in a database

users ={
    '1': User("John","Doe","JDoe@demo.com"),
}



def get_user_by_id(user_id):
    return users.get(user_id)


@app.route('/')
def index():
    user_id ='1'
    user = get_user_by_id(user_id)
    # return redirect(url_for('dashboard', user_id=user_id))
    return render_template("index.html", user=user)


@app.route('/enter_pin', methods=['POST'])
def enter_pin():
    user_id = request.form.get('user_id')

    if user_id is None:
        # If not found in form data, try to get it from query parameters
        user_id = request.args.get('user_id')

    print(f"Received user_id in enter_pin: {user_id}")

    if user_id is not None and user_id in users:
        return redirect(url_for('dashboard', user_id=user_id))
    else:
        flash('User ID is required', 'error')
        return redirect(url_for('index'))





@app.route('/dashboard')
def dashboard():
    # user_id = request.args.get('user_id')
    user_id ="1"

    if user_id in users:
        user = users[user_id]
        # dummy user from dictionary making transactions
        user.make_transactions()
        return render_template('dashboard.html', user=user)

    # Redirect to the index page if user_id is not provided or not found
    flash('User ID is required', 'error')
    return redirect(url_for("index"))








# @app.route('/dashboard')
# def dashboard():
#     user_id = session.get('user_id')
#     user = users.get(user_id)

#     if user:
#         # dummy user from dictionary making transactions
#         user.make_transactions()
#         return render_template('dashboard.html', user =user)
#     else:
#         return redirect(url_for("index"))

