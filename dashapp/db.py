import mysql.connector

def connectDB():
	try:
		cnx = mysql.connector.connect(user='root1', passwd='mysql', host='127.0.0.1', db='dashboard', port = '3306')
	except:
		None
	else:
		# cursor = cnx.cursor()
		cursor = cnx.cursor()
		return cursor, cnx

def insertDB(query,val):
	(cursor, cnx) = connectDB()
	try:
		cursor.execute(query,val)
	except mysql.connector.Error as err:
		cnx.rollback()
		print(err)
		if '1062' in str(err):
			lastid = -1
		elif '1451' in str(err):
			lastid = -2
		else:
			lastid = None
	except:
		cnx.rollback()
		lastid = None
	else:
		lastid = cursor.lastrowid
		cnx.commit()
	finally:
		cnx.close()
	return lastid

def selectDB(query):
	(cursor, cnx) = connectDB()
	# query = ("SELECT * FROM customer_master")
	cursor.execute(query)
	rows = cursor.fetchall()
	data = {}
	temp = []
	for row in rows:
		iterrow = iter(row)
		next(iterrow)
		for cell in iterrow:
			temp.append(cell)
		data.update({row[0]: temp})
		temp = []
	# print(data)
	cnx.close()
	return data

def selectDBParam(query, projName):
	(cursor, cnx) = connectDB()
	# query = ("SELECT * FROM customer_master")
	cursor.execute(query)
	rows = cursor.fetchall()
	data = {}
	temp = []
	for row in rows:
		iterrow = iter(row)
		next(iterrow)
		for cell in iterrow:
			temp.append(cell)
		data.update({projName: temp})
		temp = []
	# print(data)
	cnx.close()
	return data

def getIndex():
	(cursor, cnx) = connectDB()
	cursor.execute("SELECT * FROM ragdetails;")
	rows = cursor.fetchall()
	print(len(rows))
	cnx.close()
	return (len(rows))


# list of tuples
def listDB(query):
	(cursor, cnx) = connectDB()
	# query = ("SELECT * FROM customer_master")
	cursor.execute(query)
	rows = cursor.fetchall()
	cnx.close()
	return rows

# deletion of tuples
def deleteDB(query):
	(cursor, cnx) = connectDB()
	# query = ("SELECT * FROM customer_master")
	cursor.execute(query)
	cnx.commit()
	rows = cursor.rowcount
	cnx.close()
	return rows

#UpdateQuery
def updateDB(query):
	(cursor, cnx) = connectDB()
	# query = ("SELECT * FROM customer_master")
	cursor.execute(query)
	cnx.commit()
	rows = cursor.rowcount
	cnx.close()
	return rows