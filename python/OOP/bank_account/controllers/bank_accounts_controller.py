from bank_account import app
from flask import request, render_template, redirect, url_for,flash
from bank_account.models.user_model import User
from bank_account.models.bank_account_model import BankAccount
# imported the get_user_by_id method directly from the users controller
from .users_controller import get_user_by_id


@app.route("/show_balances/<user_id>")
def show_balances(user_id):
    user = get_user_by_id(user_id)

    if user:
        return render_template("show_balances.html", user=user)
    else:
        flash('User ID is required', 'error')
        return redirect(url_for("dashboard", user_id=user_id))



# @app.route("/withdraw")
# def withdraw():
#     user_id = request.args.get('user_id')
#     user = get_user_by_id(user_id)

#     if user:
#         return render_template("withdraw.html", user=user)
#     else:
#         flash('User ID is required', 'error')
#         return redirect(url_for("dashboard", user_id=user_id))


#____________newly added____________________________________________#

@app.route("/select_withdraw_account", methods =['GET','POST'])
def withdraw():
    user_id = request.args.get('user_id')
    user = get_user_by_id(user_id)

    if request.method == 'POST':
        selected_account = request.form.get('selected_account')
        return redirect(url_for('withdraw_options', user_id=user_id, selected_account=selected_account))

    if user:
        return render_template("withdraw.html", user=user)
    else:
        flash('User ID is required', 'error')
        return redirect(url_for("dashboard", user_id=user_id))


@app.route('/withdraw_options', methods=['GET', 'POST'])
def withdraw_options():
    user_id = request.form.get('user_id')
    selected_account = request.form.get('selected_account')
    user = get_user_by_id(user_id)

    if request.method == 'POST':
        withdrawal_amount = request.form.get('withdrawal_amount')
        # Process withdrawal based on the selected account and amount
        # You need to implement the logic for withdrawal here
        # ...

    if user:
        return render_template("withdraw_options.html", user=user, selected_account=selected_account)
    else:
        flash('User ID is required', 'error')
        return redirect(url_for("index"))




