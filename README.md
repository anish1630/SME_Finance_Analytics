# SME Finance Analytics

## Project Overview
SME Finance Analytics is a data analytics project designed to analyze small and medium-sized business transactions using Python, SQL Server, and Power BI.

## Objectives
- Analyze business sales and expenses.
- Calculate total sales, total expenses, and net profit.
- Compare financial performance across businesses.
- Present financial insights through an interactive Power BI dashboard.

## Technologies Used
- **Python** — Data processing and analysis
- **SQL Server** — Data storage and SQL queries
- **pyodbc** — Python-to-SQL Server connectivity
- **Power BI Desktop** — Financial dashboard and visualization

## Dataset
The sample dataset contains six transactions from three businesses:
- ABC Stores
- Fresh Foods
- City Textiles

Fields include transaction date, business name, category, amount, and transaction type.

## Key Results

| Metric | Result |
|---|---:|
| Total Sales | ₹75,000 |
| Total Expenses | ₹26,500 |
| Net Profit | ₹48,500 |

*These figures represent the sample dataset, not actual business financial records.*

## Project Structure

```text
SME_Finance_Analytics_New/
├── data/
│   └── transactions.csv
├── src/
│   ├── main.py
│   ├── analyze_data.py
│   ├── test_sql_connection.py
│   └── analyze_sql.py
├── sql/
├── powerbi/
│   └── SME_Finance_Dashboard.pbix
├── docs/
└── README.md
```

## How to Run
1. Install Python and SQL Server.
2. Install the Python dependency: `python -m pip install pyodbc`.
3. Create the `SME_Finance_Analytics` database and `Transactions` table.
4. Load the sample transaction data into SQL Server.
5. Configure the SQL Server connection settings in the Python scripts.
6. Run `src/analyze_data.py` for CSV analysis or `src/analyze_sql.py` for SQL-based analysis.
7. Open the Power BI dashboard to explore financial performance.

## Future Enhancements
- Add more transaction records.
- Analyze monthly revenue and expenses.
- Add business profitability comparisons.
- Improve dashboard interactivity with filters and slicers.
- Automate data refresh and reporting.
