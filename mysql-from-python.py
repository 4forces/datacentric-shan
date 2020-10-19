import os
import pymysql

# to get username and connection screen
username = os.getenv('c9_user')
connection = pymysql.connect(host='localhost',
                             user="root", password='',
                             db='Chinook')


# # to return Genre
# try:
#     with connection.cursor() as cursor:
#         # 'sql' = sql statement
#         sql = "select * from Genre limit 5;"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)


# # to return tag name
# try: 
#     with connection.cursor(pymysql.cursors.DictCursor) as cursor:
#         sql = "select * from Genre;"
#         cursor.execute(sql)
#         for row in cursor:
#             print(row)


# CREATE table
# try:
#       with connection.cursor() as cursor:
#         cursor.execute("""CREATE TABLE IF NOT EXISTS
#                           Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the

# CREATE rows
# try:
#     with connection.cursor() as cursor:
#        # Insert
#         rows = [("bob", 21, "1990-02-06 23:04:56"),
#                 ("jim", 56, "1955-05-09 13:12:45"),
#                 ("fred", 100, "1911-09-12 01:01:01")]
#         cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
#         # commit = save function
#         connection.commit()
#         # to show 'n' rows affected
#         print(cursor.rowcount, "record(s) affected")
#         # inserting another command into try statement
#         sql = "select * from Friends;"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)
# finally:
#     connection.close()


# UPDATE eg 1
# try: 
#     with connection.cursor() as cursor:
#         # # method 1
#         # sql = "UPDATE Friends SET age = 22 WHERE name = 'bob';"
#         # cursor.execute(sql)
#         # method 2 - shorthand
#         cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;", (21, 'bob'))
#         connection.commit()
#         print(cursor.rowcount, "record(s) affected")
# finally:
#     connection.close()

# UPDATE eg 2 - insert multi records
# try: 
#     with connection.cursor() as cursor:
#         rows = [(21, 'bob'),
#                 (21, 'jim'),
#                 (21, 'fred'),]
#         cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
#         connection.commit()
#         print(cursor.rowcount, "record(s) affected")
# finally:
#     connection.close()


# DESTROY/DELETE method 1
try: 
    with connection.cursor() as cursor:
        sql = "Delete from Friends where name = 'bob'"
        cursor.execute(sql)
        connection.commit()
        print(cursor.rowcount, "record(s) affected")
finally:
    connection.close()

# DESTROY/DELETE method 2
try: 
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Friends WHERE name = %s;", ['bob','jim'])
        connection.commit()
        print(cursor.rowcount, "record(s) affected")
finally:
    connection.close()

# DESTROY/DELETE multi value
try: 
    with connection.cursor() as cursor:
        rows = ['bob', 'jim']
        cursor.executemany("DELETE FROM Friends WHERE name = %s;", rows)
        connection.commit()
        print(cursor.rowcount, "record(s) affected")
finally:
    connection.close()


# # dictionary vs value-only eg
# try:
#     with connection.cursor(pymysql.cursors.DictCursor) as cursor:
#         sql = "select * from Artist limit 5;"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)
# finally:
#     connection.close()
