CREATE DATABASE company;


USE company;

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    PASSWORD VARCHAR(100) NOT NULL
);

CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    DESCRIPTION TEXT,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Clients (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    start_date DATE NOT NULL,
    contract_value DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

INSERT INTO Products (product_name, DESCRIPTION, price) VALUES
('Keyboard', 'Mechanical keyboard with RGB lighting', 99.99),
('Mouse', 'Wireless mouse with ergonomic design', 49.99),
('Monitor', '27-inch LED monitor with Full HD resolution', 199.99);
('Keyboard', 'Mechanical keyboard with RGB lighting', 99.99),
('Mouse', 'Wireless mouse with ergonomic design', 49.99),
('Monitor', '27-inch LED monitor with Full HD resolution', 199.99),
('Keyboard', 'Mechanical keyboard with RGB lighting and additional features', 129.99);


SELECT * FROM products

-- Memasukkan data ke dalam tabel Clients
INSERT INTO Clients (user_id, start_date, contract_value) VALUES
(1, '2024-06-01', 500.00),
(2, '2024-06-15', 800.00),
(3, '2024-07-01', 1200.00);

SELECT * FROM Clients

-- Memasukkan data ke dalam tabel Users
INSERT INTO Users (NAME, email, PASSWORD) VALUES
('John Doe', 'john.doe@example.com', 'password123'),
('Jane Smith', 'jane.smith@example.com', 'securepassword'),
('Michael Johnson', 'michael.johnson@example.com', 'strongpassword');

SELECT * FROM Users