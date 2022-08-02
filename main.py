import shutil
import datetime
import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
# path = "C:\\Users\\kcuki\\Documents\\Paradox Interactive\\Europa Universalis IV\\save games\\"
config = open("cfg.txt", "r")
path = config.read()
config.close()
time = datetime.datetime.now()
data = time.strftime("%m.%d-%H.%M.%S")
dir_list = os.listdir(path)


def backup():
    plik = None
    info = input("Podaj krótkie info do pliku: ")

    for i in range(len(dir_list)):
        if dir_list[i][-3:len(dir_list[i])] == "eu4" and len(dir_list[i]) == 5:
            plik = dir_list[i]

    src_path = path + plik
    dst_path = path + "\\backup\\" + data + " (" + info + ") " + plik
    shutil.copy(src_path, dst_path)
    showinfo(
        title='Information',
        message='Plik skopiowany'
    )



root.title("EU4 Ironman Save Backup")
root.geometry('400x300+50+50')
root.resizable(False, False)
root.iconbitmap('EU.ico')

# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# copy button

backup_button = ttk.Button(
    root,
    text='Copy',
    command=backup
)

backup_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)


root.mainloop()
