import subprocess
import tkinter as tk
import sqlite3

conn = sqlite3.connect('C:\\Users\\Levne\\Downloads\\Курсовая Финал-20250629T203955Z-1-001\\Курсовая Финал\\Code\\py\\base.db')
cursor = conn.cursor()

def open_another_code():
    subprocess.Popen(['python', 'C:\\Users\\Levne\\Downloads\\Курсовая Финал-20250629T203955Z-1-001\\Курсовая Финал\\Code\\py\\2beta.py'])

def get_entry_data():
    global a, b
    a = entry1.get()
    b = entry2.get()
    checkin()

def checkin():
    global a, b, error_label
    cursor.execute("SELECT * FROM APFT WHERE unCode=? AND Password=?", (a, b))
    if cursor.fetchone():
        root.destroy()
        open_another_code()
        close_program()
    else:
        if error_label.winfo_ismapped():
            error_label.grid_forget()
        error_label.grid(row=3, column=1,padx=(0,60))

def close_program():
    root.destroy()

root = tk.Tk()
root.title("FuelTrack")
root.geometry("500x500")
root.minsize(500, 500)
root.maxsize(500, 500)

frame = tk.Frame(root)
frame.pack(expand=True)

exit_button = tk.Button(root, text="Выход", command=close_program)
exit_button.pack()

label1 = tk.Label(frame, text="UnCode:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1)

label2 = tk.Label(frame, text="Password:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(frame, show="*")  
entry2.grid(row=1, column=1)

button1 = tk.Button(frame, text="Check", command=get_entry_data)
button1.grid(row=2, column=1)

error_label = tk.Label(frame, text="Invalid UnCode or password", fg='red')

root.mainloop()
