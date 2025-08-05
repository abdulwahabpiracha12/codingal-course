let balance = 0;

function addTransaction() {
    let amountField = document.getElementById("amount");
    let amount = parseFloat(amountField.value);
    let type = document.getElementById("type").value;

    if (!isNaN(amount) && amount > 0) {
        if (type === "income") {
            balance += amount;
            addToHistory(+ $${amount}, "income-item");
        } else {
            balance -= amount;
            addToHistory(- $${amount}, "expense-item");
        }
        document.getElementById("balance").innerText = balance;
        amountField.value = "";
    } else {
        alert("Please enter a valid amount!");
    }
}

function addToHistory(text, className) {
    let list = document.getElementById("history");
    let item = document.createElement("li");
    item.textContent = text;
    item.classList.add("list-group-item", className);
    list.appendChild(item);
}

function resetAll() {
    balance = 0;
    document.getElementById("balance").innerText = balance;
    document.getElementById("history").innerHTML = "";
}