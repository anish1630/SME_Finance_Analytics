
import pyodbc

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=SME_Finance_Analytics;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

try:
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    query = """
    SELECT
        SUM(CASE
            WHEN transaction_type = 'Sales' THEN amount
            ELSE 0
        END) AS Total_Sales,

        SUM(CASE
            WHEN transaction_type = 'Expense' THEN amount
            ELSE 0
        END) AS Total_Expenses,

        SUM(CASE
            WHEN transaction_type = 'Sales' THEN amount
            WHEN transaction_type = 'Expense' THEN -amount
            ELSE 0
        END) AS Net_Profit
    FROM Transactions;
    """

    cursor.execute(query)
    result = cursor.fetchone()

    print("SME FINANCE ANALYTICS")
    print("-" * 35)
    print(f"Total Sales:    Rs. {result[0]:,.2f}")
    print(f"Total Expenses: Rs. {result[1]:,.2f}")
    print(f"Net Profit:     Rs. {result[2]:,.2f}")

    connection.close()

except Exception as error:
    print("Error:", error)
