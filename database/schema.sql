CREATE DATABASE InventoryMasterDB;
GO
USE InventoryMasterDB;
GO

CREATE TABLE Roles (
    RoleID INT PRIMARY KEY IDENTITY(1,1),
    RoleName NVARCHAR(50) NOT NULL UNIQUE
);
INSERT INTO Roles (RoleName) VALUES ('Admin'), ('Sales'), ('Accounting'), ('Supply');

CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50) NOT NULL UNIQUE,
    Password NVARCHAR(255) NOT NULL, 
    FullName NVARCHAR(100),
    RoleID INT FOREIGN KEY REFERENCES Roles(RoleID)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY IDENTITY(1,1),
    ProductName NVARCHAR(100) NOT NULL,
    Category NVARCHAR(50),
    Price DECIMAL(10,2),
    StockQuantity INT,
    CriticalLevel INT DEFAULT 10 
);

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY IDENTITY(1,1),
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    Quantity INT,
    TotalPrice DECIMAL(10,2),
    SaleDate DATETIME DEFAULT GETDATE()
);