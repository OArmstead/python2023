document.addEventListener("DOMContentLoaded", function() {
    function clearPin() {
        // Assuming your PIN input field has an id "pin-input"
        var pinInput = document.getElementById("pin-input");
        if (pinInput) {
            pinInput.value = "";
        }
    }

    var clearButton = document.getElementById("clear_button");
    if (clearButton) {
        clearButton.addEventListener("click", clearPin);
    }
});

document.addEventListener('DOMContentLoaded', function () {
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
            // Update the withdrawal amount input value
            withdrawalAmountInput.value = this.dataset.amount;

            // Submit the form
            withdrawForm.submit();
        });
    });
});

function withdrawFrom(accountType, userId) {
    // Set the account type in the href attributes of withdrawal options
    document.getElementById('withdrawBtn10').href = `/process_withdraw?user_id=${userId}&account_type=${accountType}&amount=10`;
    document.getElementById('withdrawBtn20').href = `/process_withdraw?user_id=${userId}&account_type=${accountType}&amount=20`;
    document.getElementById('withdrawBtn50').href = `/process_withdraw?user_id=${userId}&account_type=${accountType}&amount=50`;
    document.getElementById('withdrawBtn100').href = `/process_withdraw?user_id=${userId}&account_type=${accountType}&amount=100`;
}


// Function to handle account selection
function selectAccount(accountType) {
    // Log the accountType to check if it's correct
    console.log('Selected Account Type:', accountType);

    // Reset the styles for all buttons
    resetButtonStyles();

    // Attempt to get the button by ID
    var selectedButton = document.getElementById(accountType + 'Btn');
    console.log('Selected Button:', selectedButton);

    // Check if the button exists before trying to modify its classList
    if (selectedButton) {
        selectedButton.classList.add('selected');
    } else {
        console.error('Button not found.');
    }
}


// Function to reset the styles for all buttons
function resetButtonStyles() {
    // Get all buttons with the class 'btn-primary'
    var buttons = document.getElementsByClassName('btn-primary');

    // Loop through each button and remove the 'selected' class
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove('selected');
    }
}


// function selectAccount(accountType) {
//     var selectedAccount = document.getElementById('selected_account');
//     selectedAccount.value = accountType;
//     var cards = document.querySelectorAll('.card-select');
//     cards.forEach(function(card) {
//         card.classList.remove('card-selected');
//     });
//     document.querySelector('.card-select[onclick="selectAccount(\'' + accountType + '\')"]').classList.add('card-selected');
//     // Redirect to withdraw options page
//     window.location.href = '/withdraw_options?selected_account=' + accountType;
// }

function redirectToWithdrawOptions(accountType) {
    window.location.href = `/withdraw_options?selected_account=${accountType}`;
}

function selectAccount(accountType) {
    window.location.href = `/withdraw_options?selected_account=${accountType}`;
}

function appendNumber(number) {
    var amountInput = document.getElementById('amountInput');
    amountInput.value = amountInput.value + number;
}

function clearInput() {
    var amountInput = document.getElementById('amountInput');
    amountInput.value = '';
}

function submitAmount() {
    var amountInput = document.getElementById('amountInput').value;
    if (amountInput) {
        // You can add your logic to handle the submitted amount here
        alert('You entered: ' + amountInput);
        // Example: Redirect to another page or send data to the server
        // window.location.href = '/process_withdraw?amount=' + amountInput;
    } else {
        alert('Please enter an amount.');
    }
}
