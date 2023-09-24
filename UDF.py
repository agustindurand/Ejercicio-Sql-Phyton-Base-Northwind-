import sqlite3 
import pandas as pd 
square = lambda n: n*n 
conn = sqlite3.connect("Nortwhind.db")

with sqlite3.coonect ("Northwind.db") as conn: 
     conn.create_function("square",1,square)
cursor = conn.cursor ()
cursor.execute ("SELECT * FROM Products")
results = cursor.fetchall ()
results_df = pd.DataFrame(results)

print (results)

#conn.commit ()
#cursor.close ()
#conn.close ()
