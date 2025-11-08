CREATE TABLE IF NOT EXISTS Salesman (
  SALESMAN_ID TEXT PRIMARY KEY,
  name TEXT,
  city TEXT,
  COMMISSION REAL   
);

INSERT INTO Salesman (SALESMAN_ID, name, city, COMMISSION) VALUES
  ('5001', 'James Hoog', 'New York', 0.15),
  ('5002', 'Nail Knite', 'Paris', 0.13),
  ('5003', 'Pit Alex', 'London', 0.11),
  ('5004', 'Mc Lyon', 'Paris', 0.14),
  ('5005', 'Paul Adam', 'Rome', 0.13),
  ('5006', 'Lauson Hen', 'San Jose', 0.12);

SELECT * FROM Salesman;

SELECT * FROM Salesman
WHERE city == "Paris";

CREATE TABLE IF NOT EXISTS Orders (
  ord_no TEXT PRIMARY KEY,
  purch_amt REAL,
  ord_date TEXT,
  customer_id TEXT,
  Salesman_id TEXT
);

INSERT INTO Orders (ord_no, purch_amt, ord_date, customer_id, Salesman_id) VALUES
  ('70001', 150.5, '2012-10-05', '3005', '5002'),
  ('70009', 270.65, '2012-09-10', '3001', '5001'),
  ('70002', 65.26, '2012-10-05', '3002', '5003'),
  ('70004', 110.5, '2012-08-17', '3009', '5007'),
  ('70007', 948.5, '2012-09-10', '3005', '5005'),
  ('70005', 2400.6, '2012-10-05', '3007', '5006');

-- Now view the Orders table
SELECT * FROM Orders;

-- This assumes a Salesman table already exists
SELECT name, commission
FROM Salesman;