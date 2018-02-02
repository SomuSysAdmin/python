"""
SQLite is a zero-config DBMS that Python3 comes pre-packaged with. To use it, we use the `sqlite3` library.

Python also has a Standardized Database API that uses the same common techniques to work with several DBMSs irrespective
of their individual functionality. These steps are:
- Establish a connection to the Database backend.
- Create a _cursor_ to communicate through the connection.
- Manipulate data via SQL Statements through the cursor.
- Either *commit* or _rollback_
- Close the connection.
"""

# Setup:
import sqlite3
try:
	connection = sqlite3.connect('dataStores/testDB.sqlite')
	cursor = connection.cursor()
except Exception as err:
	print("An exception occurred: "+ str(err))
	exit(1)

# Data handling and manipulation:
cursor.execute("""SELECT DATE('NOW')""")
data = cursor.fetchall()		# Stores a reference to the output in the data variable.

# Committing and closing:
connection.commit()
connection.close()

print(type(data))
"""
The data variable is a list containing a tuple for each row in the output.
"""
for row in data:
	dt = row[0]		# Selecting the element 0 in the tuple for the current row.
	print(dt)
	"""
	Alternative Syntax: 
	The inclusion of the `,` turns the line into a 1-tuple. Note that the brackets don't really do anything, and the only
	purpose that it serves is the ease of understanding at a glance. 
	
	The line would still be valid if it were: `dt, = row`
	"""
	(dt,) = row
	print(dt)


class DBCon:
	def __init__(self, db_file):
		try:
			self.con = sqlite3.connect(db_file)
			self.cur = self.con.cursor()
		except Exception as dbErr:
			print("An exception occurred while trying to create the database connection: " + str(dbErr))

	def get_cur(self):
		if self.cur:
			return self.cur
		else:
			return None

	def close_cur(self, commit=False):
		if not self.cur:
			print("There was an error fetching the cursor! Exiting!!")
			exit(1)

		if commit:
			self.con.commit()
		else:
			self.con.rollback()
		self.con.close()


# Actual Code:
db_obj = DBCon('dataStores/testDB.sqlite')
cur = db_obj.get_cur()

sql_query = """
CREATE TABLE IF NOT EXISTS athletes (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
name TEXT NOT NULL,
dob DATE NOT NULL 
)
"""
cur.execute(sql_query)

# Insertion of Data:
sql_query = "INSERT INTO athletes (name, dob) VALUES (?, ?)"
values = ("John Cena", "1978-01-01")
cur.execute(sql_query, values)
cur.execute(sql_query, ("Hulk Hogan", "1991-04-31"))

# Fetching of Data:
sql_query = "SELECT * FROM athletes"
cur.execute(sql_query)
data = cur.fetchall()
for row in data:
	(_, name, _) = row		# Data in the tuple is of format : (1, 'John Cena', '1978-01-01')
	# The use of the `_` character in the above target selector ignores the first and the last element.
	print("Athlete = " + name)

# Closing Connection:
db_obj.close_cur(True)