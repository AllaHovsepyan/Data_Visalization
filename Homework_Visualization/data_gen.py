import sqlite3
import numpy as np
import time

connection = sqlite3.connect('data_db.db')
c = connection.cursor()

c.execute("DROP TABLE IF EXISTS sept_values")

c.execute("CREATE TABLE sept_values (trial int, roll1 int, roll2 int, roll3 int, roll4 int, roll5 int, roll6 int, roll7 int, avg float)")

i = 0
a = 0

while True:
	i += 1
	a = np.random.randint(low=1,high=7,size=7)
	c.execute("INSERT INTO sept_values values ({},{},{},{},{},{},{},{},{})".format(*np.append(np.append(i,a),a.mean())))
	connection.commit()

	time.sleep(0.5)
