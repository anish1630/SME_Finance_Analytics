
USE SME_Finance_Analytics;
GO

-- Financial Summary
SELECT
    SUM(CASE
        WHEN transaction_type = 'Sales'
        THEN amount ELSE 0
    END) AS Total_Sales,

    SUM(CASE
        WHEN transaction_type = 'Expense'
        THEN amount ELSE 0
    END) AS Total_Expenses,

    SUM(CASE
        WHEN transaction_type = 'Sales'
        THEN amount
        WHEN transaction_type = 'Expense'
        THEN -amount
        ELSE 0
    END) AS Net_Profit
FROM Transactions;
GO

-- Business-wise Sales
SELECT
    business_name,
    SUM(amount) AS Total_Sales
FROM Transactions
WHERE transaction_type = 'Sales'
GROUP BY business_name
ORDER BY Total_Sales DESC;
GO
