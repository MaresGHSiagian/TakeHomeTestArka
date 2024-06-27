-- Create the database
CREATE DATABASE OilAndGasCompany;

-- Use the newly created database
USE OilAndGasCompany;

-- Create the Users table
CREATE TABLE Users (
    user_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Create the Products table
CREATE TABLE Products (
    product_id INT PRIMARY KEY IDENTITY(1,1),
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL
);

-- Create the Clients table
CREATE TABLE Clients (
    service_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT,
    start_date DATE NOT NULL,
    contract_value DECIMAL(15, 2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);