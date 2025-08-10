let balance = 0;
let expenses = 0;

function deposit() {
    let amount = Number(document.getElementById("amount").value);
    if (amount > 0) {
        balance += amount;
        updateDisplay();
    } else {
        alert("Enter a valid deposit amount.");
    }
}

function withdraw() {
    let amount = Number(document.getElementById("amount").value);
    if (amount > 0 && amount <= balance) {
        balance -= amount;
        expenses += amount;
        updateDisplay();
    } else {
        alert("Enter a valid amount or check your balance.");
    }
}

function updateDisplay() {
    document.getElementById("balance").innerText = balance.toFixed(2);
    document.getElementById("expenses").innerText = expenses.toFixed(2);
}