import sqlite3

nw_conn = sqlite3.connect('northwind_small.sqlite3')
nw_curs = nw_conn.cursor()

# Ten most expensive items (per unit price)
unit_price = nw_curs.execute("""SELECT ProductName, UnitPrice
                                FROM Product
                                ORDER BY UnitPrice DESC
                                LIMIT 10;""").fetchall()

# Average age of an employee at the time of their hiring

# First their birth date:
avg_birthdate = nw_curs.execute("""SELECT AVG (BirthDate)
                                   FROM Employee;""").fetchone()

# Next their hire date:
avg_hiredate = nw_curs.execute("""SELECT AVG (HireDate)
                                  FROM Employee;""").fetchone()

# The average of the first minus the average of the second is the same thing
# as finding the age of each individual employee at their start date and
# calculating the average:
avg_hireage = avg_hiredate[0] - avg_birthdate[0]

print("Part 2: The top ten products by unit price are: ", unit_price, "\n",
      "The average age of employees at the time of their hiring was: ",
       avg_hireage)

# Ten most expensive items (per unit price)
unit_price_with_suppliers = nw_curs.execute("""SELECT p.ProductName, p.UnitPrice, s.CompanyName
                                               FROM Product AS p
                                               INNER JOIN Supplier as s
                                               ON p.SupplierId = s.Id
                                               ORDER BY UnitPrice DESC
                                               LIMIT 10;""").fetchall()

largest_category = nw_curs.execute("""SELECT c.CategoryName
                                      FROM Product AS p
                                      INNER JOIN Category AS c
                                      ON p.CategoryId = c.Id
                                      GROUP BY CategoryId
                                      ORDER BY COUNT(CategoryId) DESC
                                      LIMIT 1;""").fetchone()

print("""The following are the ten most expensive products by unit price and
      their supplier: """, unit_price_with_suppliers,
      "The largest category (by unique products in it) is: ",
      largest_category[0])

nw_curs.close()
nw_conn.commit()
