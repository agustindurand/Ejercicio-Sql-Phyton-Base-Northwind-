import sqlite3 
import pandas as pd 
import matplotlib.pyplot as plt 

#obteniendo los diez productos mas rentables
conn = sqlite3.connect("Northwind.db")
query = """SELECT ProductName, SUM (Price * Quantity) as Renevue
            FROM OrderDetails od
            JOIN Products p ON p.ProductID = od.ProductID
            GROUP BY od.ProductID 
            ORDER BY Renevue DESC
            LIMIT 10
"""

top_products =  pd.read_sql_query(query, conn) 

top_products.plot(x="ProductName", y="Renevue", kind= "bar", figsize= (10,5), legend=False)
plt.title("10 PRODUCTOS MAS VENDIDOS")
plt.xlabel("Products")
plt.ylabel ("Renevue")
plt.xticks (rotation=90) 
plt.show()

#OBTENIENDO LOS 10 EMPLEADOS MAS EFECTIVOS

query2 = """"
        SELECT FirstName || " " || LastName, COUNT (*) as Total
        FROM Orders o
        JOIN Employees e
        ON e.EmployeeID = o.EmployeeID
        Group BY o.EmployeeID
        ORDER BY TOTAL DESC
        LIMIT 10
"""
top_employees = pd.read_sql_query(query2,conn)
top_employees.plot(x="ProductName", y="Renevue", kind= "bar", figsize= (10,5), legend=False)
plt.title("10 EMPLEADOS MAS RENTABLES")
plt.xlabel("EMPLEADOS")
plt.ylabel ("TOTAL VENDIDO")
plt.xticks (rotation=45) 
plt.show()
