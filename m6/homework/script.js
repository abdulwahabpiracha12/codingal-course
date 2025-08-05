let balance = 0;
let transactions = [];

// Add Transaction
function addTransaction() {
    let amountField = document.getElementById("amount");
    let amount = parseFloat(amountField.value);
    let type = document.getElementById("type").value;

    if (!isNaN(amount) && amount > 0) {
        const transaction = {
            id: Date.now(),
            amount: amount,
            type: type,
            date: new Date().toLocaleString()
        };
        transactions.push(transaction);

        // Update balance
        balance = calculateBalance();
        updateUI();

        amountField.value = "";
    } else {
        alert("Please enter a valid amount!");
    }
}

// Calculate Balance
function calculateBalance() {
    let total = 0;
    transactions.forEach(tx => {
        total += (tx.type === "income") ? tx.amount : -tx.amount;
    });
    return total;
}

// Update Transaction List
function updateUI(filteredList = transactions) {
    document.getElementById("balance").innerText = balance.toFixed(2);
    let list = document.getElementById("history");
    list.innerHTML = "";

    filteredList.forEach(tx => {
        let item = document.createElement("li");
        item.classList.add("list-group-item", tx.type === "income" ? "income-item" : "expense-item");
        item.textContent = ${tx.type === "income" ? '+' : '-'} $${tx.amount.toFixed(2)} | ${tx.date};

        // Delete button
        let delBtn = document.createElement("button");
        delBtn.textContent = "Delete";
        delBtn.classList.add("delete-btn");
        delBtn.onclick = () => deleteTransaction(tx.id);

        item.appendChild(delBtn);
        list.appendChild(item);
    });
}

// Delete Transaction
function deleteTransaction(id) {
    transactions = transactions.filter(tx => tx.id !== id);
    balance = calculateBalance();
    updateUI();
}

// Reset All
function resetAll() {
    transactions = [];
    balance = 0;
    updateUI();
}

// Filter Transactions
function filterTransactions() {
    let filterValue = document.getElementById("filter").value;
    let filtered = transactions;

    if (filterValue !== "all") {
        filtered = transactions.filter(tx => tx.type === filterValue);
    }
    updateUI(filtered);
}

// Search Transactions
function searchTransactions() {
    let searchValue = document.getElementById("search").value.trim();
    let filtered = transactions.filter(tx => tx.amount.toString().includes(searchValue));
    updateUI(filtered);
}