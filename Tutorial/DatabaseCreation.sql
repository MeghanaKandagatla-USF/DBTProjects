CREATE DATABASE hr_analytics;
GO

USE hr_analytics;

-- Raw employee info
CREATE TABLE raw_employees (
    employee_id INT PRIMARY KEY,
    first_name NVARCHAR(50),
    last_name NVARCHAR(50),
    department NVARCHAR(50),
    hire_date DATE
);

-- Raw performance data
CREATE TABLE raw_performance (
    employee_id INT,
    review_year INT,
    rating INT, -- scale 1-5
    bonus_amount DECIMAL(10, 2)
);

-- Sample data
INSERT INTO raw_employees VALUES
(101, 'Aisha', 'Patel', 'Engineering', '2021-01-05'),
(102, 'Liam', 'Johnson', 'Marketing', '2020-07-12'),
(103, 'Mira', 'Lee', 'Engineering', '2019-09-01');

INSERT INTO raw_performance VALUES
(101, 2022, 5, 3000), (101, 2023, 4, 2500),
(102, 2022, 3, 1500), (102, 2023, 2, 1000),
(103, 2022, 4, 2000), (103, 2023, 5, 3200);
