let balance = 0;
let income = 0;
let expense = 0;

function addTransaction() {
  const amount = parseFloat(document.getElementById("amount").value);
  const type = document.getElementById("type").value;

  if (isNaN(amount) || amount <= 0) {
    alert("Please enter a valid amount");
    return;
  }

  const transactionsList = document.getElementById("transactions");
  const li = document.createElement("li");

  if (type === "income") {
    income += amount;
    balance += amount;
    li.textContent = `+ ${amount} PKR (Income)`;
    li.classList.add("income");
  } else {
    expense += amount;
    balance -= amount;
    li.textContent = `- ${amount} PKR (Expense)`;
    li.classList.add("expense");
  }

  transactionsList.appendChild(li);

  // update UI
  document.getElementById("balance").textContent = balance;
  document.getElementById("income").textContent = income;
  document.getElementById("expense").textContent = expense;

  document.getElementById("amount").value = "";
}