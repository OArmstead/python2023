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
    
    if (clearButton) {
        clearButton.addEventListener('click', clearInput);
    }
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
    if (amountInput) {
        amountInput.value = '';
    }
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
    const accountType = 'checking'; // or 'savings', dynamically set this based on the user's selection

    fetch('/api/process_withdraw', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            account_type: accountType,
            amount: amount
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            showLoadingModal();
            setTimeout(function() {
                hideLoadingModal();
                window.location.href = `/confirmation?amount=${amount}&account_type=${accountType}&new_balance=${data.new_balance}`;
            }, 3000); // Simulate a delay of 3 seconds
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// function submitTransfer() {
//     var amountInput = document.getElementById('amount').value;
//     var fromAccount = document.getElementById('fromAccount').value;
//     var toAccount = document.getElementById('toAccount').value;
//     var userId = document.getElementById('user_id').value;

//     if (!amountInput) {
//         alert('Please enter an amount.');
//         return;
//     }

//     if (parseInt(amountInput) % 5 !== 0) {
//         alert('Please enter an amount in denominations of 5, 10, 20, or 100.');
//         clearInput();
//         return;
//     }

//     transferFunds(amountInput, fromAccount, toAccount, userId);
// }

// Function to submit the transfer form
function submitTransfer() {
    let fromAccount = document.getElementById('fromAccount').value;
    let toAccount = document.getElementById('toAccount').value;
    let amount = document.getElementById('amount').value;

    if (amount === '') {
        alert('Please enter an amount.');
        return;
    }

    document.getElementById('confirmAmount').innerText = `$${amount}`;
    document.getElementById('confirmFromAccount').innerText = fromAccount;
    document.getElementById('confirmToAccount').innerText = toAccount;

    let confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
    confirmationModal.show();
}

function transferFunds(amount, fromAccount, toAccount, userId) {
    fetch('/api/process_transfer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            from_account: fromAccount,
            to_account: toAccount,
            amount: amount,
            user_id: userId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            showLoadingModal();
            setTimeout(function() {
                hideLoadingModal();
                window.location.href = `/confirmation?amount=${amount}&from_account=${fromAccount}&to_account=${toAccount}&new_balance=${data.new_balance}`;
            }, 3000); // Simulate a delay of 3 seconds
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function showLoadingModal() {
    var loadingModalElement = new bootstrap.Modal(document.getElementById('loadingModal'), {
        backdrop: 'static',
        keyboard: false
    });
    loadingModalElement.show();
}

function hideLoadingModal() {
    var loadingModalElement = bootstrap.Modal.getInstance(document.getElementById('loadingModal'));
    loadingModalElement.hide();
}


// Function to confirm and process the transfer
function confirmTransfer() {
    let user_id = document.getElementById('user_id').value;
    let fromAccount = document.getElementById('fromAccount').value;
    let toAccount = document.getElementById('toAccount').value;
    let amount = document.getElementById('amount').value;

    let transferData = {
        user_id: user_id,
        from_account: fromAccount,
        to_account: toAccount,
        amount: amount
    };

    fetch('/api/process_transfer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(transferData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            alert(data.message);
            // Redirect to the confirmation page with transfer details
            window.location.href = `/confirmation?amount=${data.amount}&account_type=${data.from_account}&new_balance=${data.new_balance}&transaction_date=${data.transaction_date}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while processing the transfer.');
    });
}





window.appendNumber = appendNumber;
window.clearInput = clearInput;
window.submitAmount = submitAmount;
window.submitTransfer = submitTransfer;
window.transferFunds = transferFunds;
window.showLoadingModal = showLoadingModal;
window.hideLoadingModal = hideLoadingModal;
