import sqlite3

def compare_value_with_database(input_value):
    conn = sqlite3.connect('C:\123')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM FTA WHERE unCode = ?", (input_value,))
    result = cursor.fetchone()

    if result:
        print("Эщкере")
    else:
        print("не Эщекере")

    conn.close()

input_value = input("Ваш код сотрудника ")
compare_value_with_database(input_value)