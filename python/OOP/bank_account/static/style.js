document.addEventListener("DOMContentLoaded", function() {
    function clearPin() {
        var pinInput = document.getElementById("pin-input");
        if (pinInput) {
            pinInput.value = "";
        }
    }

    var clearButton = document.getElementById("clear_button");
    if (clearButton) {
        clearButton.addEventListener("click", clearPin);
    }

    const accountButtons = document.querySelectorAll('.account-btn');
    const withdrawButtons = document.querySelectorAll('.withdraw-btn');
    const selectedAccountInput = document.getElementById('selectedAccount');
    const withdrawalAmountInput = document.getElementById('withdrawalAmount');
    const withdrawForm = document.getElementById('withdrawForm');

    accountButtons.forEach(button => {
        button.addEventListener('click', function () {
            selectAccount(this.dataset.account);
        });
    });

    withdrawButtons.forEach(button => {
        button.addEventListener('click', function () {
            withdrawalAmountInput.value = this.dataset.amount;
            withdrawForm.submit();
        });
    });
});

function withdrawFrom(accountType, userId) {
    document.getElementById('withdrawBtn10').href = `/process_withdraw?user_id=${userId}&account_type=${accountType}&amount=10`;
    document.getElementById('withdrawBtn20').href = `/process_withdraw?user_id=${userId}&account_type=${accountType}&amount=20`;
    document.getElementById('withdrawBtn50').href = `/process_withdraw?user_id=${userId}&account_type=${accountType}&amount=50`;
    document.getElementById('withdrawBtn100').href = `/process_withdraw?user_id=${userId}&account_type=${accountType}&amount=100`;
}

function selectAccount(accountType) {
    console.log('Selected Account Type:', accountType);
    resetButtonStyles();
    var selectedButton = document.getElementById(accountType + 'Btn');
    console.log('Selected Button:', selectedButton);

    if (selectedButton) {
        selectedButton.classList.add('selected');
    } else {
        console.error('Button not found.');
    }

    window.location.href = `/withdraw_options?selected_account=${accountType}`;
}

function resetButtonStyles() {
    var buttons = document.getElementsByClassName('btn-primary');
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove('selected');
    }
}

function clearInput() {
    var amountInput = document.getElementById('amount');
    amountInput.value = '';
}

function appendNumber(number) {
    var amountInput = document.getElementById('amount');
    amountInput.value += number;
}

function submitAmount() {
    var amountInput = document.getElementById('amount').value;
    if (!amountInput) {
        alert('Please enter an amount.');
        return;
    }

    if (parseInt(amountInput) % 5 !== 0) {
        alert('Please enter an amount in denominations of 5, 10, 20, or 100.');
        clearInput();
        return;
    }

    withdraw(amountInput);
}

function withdraw(amount) {
    showLoadingModal();

    setTimeout(function() {
        var loadingModalElement = document.getElementById('loadingModal');
        var modalInstance = bootstrap.Modal.getInstance(loadingModalElement);
        modalInstance.hide();

        window.location.href = '/confirmation?amount=' + amount;
    }, 3000);
}

function showLoadingModal() {
    var loadingModalElement = new bootstrap.Modal(document.getElementById('loadingModal'), {
        backdrop: 'static',
        keyboard: false
    });
    loadingModalElement.show();
}

window.appendNumber = appendNumber;
window.clearInput = clearInput;
window.submitAmount = submitAmount;
window.withdraw = withdraw;
