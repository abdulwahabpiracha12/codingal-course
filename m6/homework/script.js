let users = {
  "wahab": { pin: "1234", balance: 500, income: 0, expenses: 0, transactions: [] },
  "ahmed": { pin: "5678", balance: 1000, income: 0, expenses: 0, transactions: [] }
};

let currentUser = null;

function login() {
  let username = document.getElementById("username").value;
  let pin = document.getElementById("pin").value;

  if (users[username] && users[username].pin === pin) {
    currentUser = username;
    document.getElementById("loginSection").classList.add("hidden");
    document.getElementById("dashboard").classList.remove("hidden");
    document.getElementById("userDisplay").textContent = username;
    updateDashboard();
  } else {
    alert("Invalid username or PIN!");
  }
}

function updateDashboard() {
  let user = users[currentUser];
  document.getElementById("balance").textContent = user.balance.toFixed(2);
  document.getElementById("income").textContent = user.income.toFixed(2);
  document.getElementById("expenses").textContent = user.expenses.toFixed(2);
  document.getElementById("net").textContent = (user.income - user.expenses).toFixed(2);

  let transactionList = document.getElementById("transactionList");
  transactionList.innerHTML = "";
  user.transactions.slice().reverse().forEach(t => {
    let div = document.createElement("div");
    div.classList.add("transaction");
    div.textContent = t;
    transactionList.appendChild(div);
  });
}

function deposit() {
  let amount = parseFloat(document.getElementById("amount").value);
  if (amount > 0) {
    users[currentUser].balance += amount;
    users[currentUser].transactions.push(`Deposit: +$${amount}`);
    updateDashboard();
  } else {
    alert("Enter a valid amount");
  }
}

function withdraw() {
  let amount = parseFloat(document.getElementById("amount").value);
  if (amount > 0 && amount <= users[currentUser].balance) {
    users[currentUser].balance -= amount;
    users[currentUser].transactions.push(`Withdraw: -$${amount}`);
    updateDashboard();
  } else {
    alert("Insufficient balance or invalid amount");
  }
}

function addIncome() {
  let amount = parseFloat(document.getElementById("amount").value);
  if (amount > 0) {
    users[currentUser].income += amount;
    users[currentUser].balance += amount;
    users[currentUser].transactions.push(`Income: +$${amount}`);
    updateDashboard();
  } else {
    alert("Enter a valid income amount");
  }
}

function addExpense() {
  let amount = parseFloat(document.getElementById("amount").value);
  if (amount > 0 && amount <= users[currentUser].balance) {
    users[currentUser].expenses += amount;
    users[currentUser].balance -= amount;
    users[currentUser].transactions.push(`Expense: -$${amount}`);
    updateDashboard();
  } else {
    alert("Insufficient balance or invalid expense");
  }
}

function logout() {
  currentUser = null;
  document.getElementById("loginSection").classList.remove("hidden");
  document.getElementById("dashboard").classList.add("hidden");
}