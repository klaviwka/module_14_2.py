import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total_records = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
total_balance = cursor.fetchone()[0]

if total_records > 0:
    average_balance = total_balance / total_records
else:
    average_balance = 0

print(f'Средний баланс всех пользователей: {average_balance:.2f}')


connection.close()
