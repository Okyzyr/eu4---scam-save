import datetime
import os
import shutil
import sys
import tkinter as tk
from sys import platform
from tkinter import ttk, Label
from tkinter.messagebox import showinfo
import linecache

root = tk.Tk()
time = datetime.datetime.now()
data = time.strftime("%m.%d-%H.%M.%S")



def syschceck():
    if platform == "linux" or platform == "linux2":
        sys.exit()
    elif platform == "darwin":
        path = linecache.getline(r'cfg.txt', 2).strip()
        return path
    elif platform == "win32":
        path = linecache.getline(r'cfg.txt', 4).strip()
        return path


path = syschceck()

dir_list = os.listdir(path)


def backup():
    file = None
    # info = input("Podaj krótkie info do pliku: ")
    if "backup" in dir_list:
        pass
    else:
        folder_name = "backup"
        full_path = os.path.join(path, folder_name)
        os.mkdir(full_path)

    for i in range(len(dir_list)):
        if dir_list[i][-3:len(dir_list[i])] == "eu4" and len(dir_list[i]) == 5:
            file = dir_list[i]

    src_path = path + file
    dst_path = path + "/backup/" + data + " (" + "CPY" + ") " + file
    shutil.copy(src_path, dst_path)
    showinfo(
        title='Information',
        message='Plik skopiowany'
    )


plik = None
for i in range(len(dir_list)):
    if dir_list[i][-3:len(dir_list[i])] == "eu4" and len(dir_list[i]) == 5:
        plik = dir_list[i]

root.title("EU4 Ironman Save Backup")
root.geometry('500x130+50+50')
root.resizable(True, True)
root.iconbitmap('EU.ico')

label = Label(root, text='Kopiowanie pliku "' + plik + '" do folderu "/backup"')
label.grid(row=2, column=0)

# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)
exit_button.grid(row=5, column=0)

# copy button

backup_button = ttk.Button(
    root,
    text='Copy',
    command=backup
)

backup_button.grid(row=3, column=0)

label2 = Label(root, text='ścieżka zapisu save: \n' + path)
label2.grid(row=4, column=0)
root.mainloop()
