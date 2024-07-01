from bank_account import app

#<_______Add Controllers______>
from bank_account.controllers import bank_accounts_controller
from bank_account.controllers import users_controller


if __name__=='__main__':
    print("Starting Flask application...")
    app.run(debug=True)