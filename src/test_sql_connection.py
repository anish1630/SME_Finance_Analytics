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
    print("SQL Server Connected Successfully!")

    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM Transactions")
    count = cursor.fetchone()[0]

    print(f"Total Transactions in SQL Server: {count}")

    connection.close()

except Exception as error:
    print("Connection failed:")
    print(error)