document.addEventListener("DOMContentLoaded", function () {
    let balance = 0;
    let expenses = 0;
    let history = [];

    const balanceEl = document.getElementById("balance");
    const expensesEl = document.getElementById("expenses");
    const historyEl = document.getElementById("history");
    const amountInput = document.getElementById("amount");

    // Deposit
    document.getElementById("depositBtn").addEventListener("click", function () {
        const amount = Number(amountInput.value);
        if (amount > 0) {
            balance += amount;
            history.push(Deposited: ${amount.toFixed(2)} PKR);
            amountInput.value = "";
            updateUI();
        } else {
            alert("Enter a valid deposit amount.");
        }
    });

    // Withdraw
    document.getElementById("withdrawBtn").addEventListener("click", function () {
        const amount = Number(amountInput.value);
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            expenses += amount;
            history.push(Withdrew (Expense): ${amount.toFixed(2)} PKR);
            amountInput.value = "";
            updateUI();
        } else {
            alert("Enter a valid amount or check your balance.");
        }
    });

    // Clear history
    document.getElementById("clearBtn").addEventListener("click", function () {
        history = [];
        updateUI();
    });

    // Update UI function
    function updateUI() {
        balanceEl.innerText = balance.toFixed(2);
        expensesEl.innerText = expenses.toFixed(2);
        historyEl.innerHTML = "";
        history.forEach(item => {
            const li = document.createElement("li");
            li.textContent = item;
            historyEl.appendChild(li);
        });
    }
});