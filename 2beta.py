import tkinter as tk
from tkinter import ttk
import sqlite3

def connect_to_db():
    connection = sqlite3.connect('C:\\Users\\Levne\\Downloads\\Курсовая Финал-20250629T203955Z-1-001\\Курсовая Финал\\Code\\py\\base.db')
    return connection

def get_data_from_db():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 
        Worker.id, 
        Worker.FirstName, 
        Worker.LastName,
        Worker.UnCode, 
        IFNULL(CarsId.NameCar, '-') AS NameCar,
        IFNULL(WorkerFuel.DateFuel, '-') AS DateFuel,
        IFNULL(WorkerFuel.TimeFuel, '-') AS TimeFuel, 
        IFNULL(WorkerFuel.AmounttFuel, '-') AS AmounttFuel, 
        IFNULL(WorkerFuel.NameFuel, '-') AS NameFuel 
    FROM Worker
    LEFT JOIN CarsId ON Worker.idCar = CarsId.idCar
    LEFT JOIN WorkerFuel ON CarsId.idCar = WorkerFuel.idCar
    """)

    data = cursor.fetchall()
    conn.close()
    return data

def sort_data(column_index):
    global treeview_data
    fuel_order = ["АИ-100", "ДТ", "АИ-95", "АИ-92", "АИ-80", "КВ"]
    def sort_key(row):
        value = row[column_index]
        if column_index == 8:
            if value in fuel_order:
                return fuel_order.index(value)
            else:
                return len(fuel_order) 
        elif value == '-':
            return (1, value)
        else:
            return (0, value)

    treeview_data = sorted(treeview_data, key=sort_key)
    update_treeview()

def search_data():
    global treeview_data
    search_term = search_entry.get().lower()
    filtered_data = []
    for row in treeview_data:
        for value in row:
            if search_term in str(value).lower():
                filtered_data.append(row)
                break
    update_treeview(filtered_data)

def update_treeview(data=None):
    treeview.delete(*treeview.get_children())
    if data is None:
        data = treeview_data
    for row in data:
        treeview.insert('', 'end', values=row)

def close_program():
    root.destroy()

root = tk.Tk()
root.title('FuelTrack')
root.geometry("1400x600") 

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (1400 / 2)) 
y_coordinate = int((screen_height / 2) - (800 / 2)) 

root.geometry(f"+{x_coordinate}+{y_coordinate}")

columns = ('id', 'Имя', 'Фамилия', 'Код Сотрудника', 'Название машины', 'Дата', 'Время', 'Количество топлива', 'Название Топлива')
button = ('id', 'Имени', 'Фамилии', 'Коду Сотрудника', 'Названию машины', 'Дате', 'Времени', 'Количеству топлива', 'Названию Топлива')
treeview = ttk.Treeview(root, columns=columns, show='headings', height=20) 
for col in columns:
    treeview.heading(col, text=col, command=lambda c=col: sort_data(columns.index(c)))
    treeview.column(col, width=150) 
treeview.pack(pady=20) 

treeview_data = get_data_from_db()
update_treeview()

controls_frame = tk.Frame(root)
controls_frame.pack()

sort_label = tk.Label(controls_frame, text="Сортировать по:")
sort_label.pack(side="left", pady=5)

selected_sort = tk.StringVar(value='Выберите столбец')
sort_options = [f"{col}" for col in button]
sort_menu = tk.OptionMenu(controls_frame, selected_sort, *sort_options, command=lambda choice: sort_data(sort_options.index(choice)))
sort_menu.pack(side="left", pady=5)

search_label = tk.Label(controls_frame, text="Поиск:")
search_label.pack(side="left", padx=3, pady=5)

search_entry = tk.Entry(controls_frame)
search_entry.pack(side="left", padx=5, pady=5)

search_button = tk.Button(controls_frame, text="Найти", command=search_data, width=30)
search_button.pack(pady=5)

exit_button = tk.Button(root, text="Выход", command=close_program, width=14)
exit_button.pack(pady=10,side="bottom")

root.mainloop()

