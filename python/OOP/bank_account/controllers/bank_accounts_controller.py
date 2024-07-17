from bank_account import app
from flask import request, render_template, redirect, url_for,flash,session,jsonify
from bank_account.models.user_model import User
from bank_account.models.bank_account_model import BankAccount
from datetime import datetime
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




#____________newly added____________________________________________#





@app.route("/select_withdraw_account", methods=['GET', 'POST'])
def select_withdraw_account():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    user_id = session['user_id']
    user = get_user_by_id(user_id)

    if user:
        return render_template("select_withdraw_account.html", user=user, user_id=user_id)
    else:
        flash('User ID is required', 'error')
        return redirect(url_for("index"))

@app.route('/withdraw_options', methods=['GET', 'POST'])
def withdraw_options():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    user_id = session['user_id']
    selected_account = request.args.get('selected_account')
    user = get_user_by_id(user_id)

    if user:
        return render_template("withdraw_options.html", user=user, selected_account=selected_account)
    else:
        flash('User ID is required', 'error')
        return redirect(url_for("index"))

@app.route('/api/process_withdraw', methods=['POST'])
def api_process_withdraw():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    user_id = session['user_id']
    data = request.json
    account_type = data.get('account_type')
    amount = float(data.get('amount'))

    user = get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if account_type == 'checking':
        account = user.checking_account
    elif account_type == 'savings':
        account = user.savings_account
    else:
        return jsonify({'error': 'Invalid account type'}), 400

    if account.balance < amount:
        return jsonify({'error': 'Insufficient funds'}), 400

    account.withdraw(amount)
    return jsonify({'message': 'Withdrawal successful', 'new_balance': account.balance, 'amount': amount})


# @app.route('/confirmation', methods=['GET'])
# def confirmation():
#     amount = request.args.get('amount')
#     return render_template('confirmation.html', amount=amount)


@app.route('/confirmation', methods=['GET'])
def confirmation():
    amount = request.args.get('amount')
    account_type = request.args.get('account_type')
    new_balance = request.args.get('new_balance')  # Assuming this is passed in the query string
    transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return render_template('confirmation.html', amount=amount, account_type=account_type, new_balance=new_balance, transaction_date=transaction_date)

@app.route('/transfer')
def transfer():
    user_id = session.get('user_id')
    if not user_id:
        flash('User ID is required', 'error')
        return redirect(url_for("index"))

    user = get_user_by_id(user_id)
    if not user:
        flash('User not found', 'error')
        return redirect(url_for("index"))

    return render_template('transfer.html', user=user, user_id=user_id)



@app.route('/api/process_transfer', methods=['POST'])
def api_process_transfer():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    user_id = session['user_id']
    data = request.json
    from_account_type = data.get('from_account')
    to_account_type = data.get('to_account')
    amount = float(data.get('amount'))

    user = get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    from_account = user.checking_account if from_account_type == 'checking' else user.savings_account
    to_account = user.savings_account if to_account_type == 'savings' else user.checking_account

    if from_account.balance < amount:
        return jsonify({'error': 'Insufficient funds'}), 400

    from_account.withdraw(amount)
    to_account.deposit(amount)

    return jsonify({'message': 'Transfer successful', 'new_balance': to_account.balance})
