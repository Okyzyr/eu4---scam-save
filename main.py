import datetime
import os
import shutil
import tkinter as tk
from tkinter import ttk, Label
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
import linecache

count = 0
root = tk.Tk()
time = datetime.datetime.now()
data = time.strftime("%m.%d-%H.%M.%S")


def open_file_chooser():
    filename = askopenfilename()
    with open('cfg.txt', 'w') as file:
        file.writelines(filename)
    file.close()
    showinfo(
        title='Info',
        message='Zrestartuj program'
    )


def file_path():
    path = linecache.getline(r'cfg.txt', 1).strip()
    split = path.rindex('/')
    path = path[:split + 1]
    return path


def file_name():
    file_name = linecache.getline(r'cfg.txt', 1).strip()
    split = file_name.rindex('/')
    file_name = file_name[split + 1:]
    return file_name


def backup():
    path = file_path()
    file = file_name()
    print(path + file)
    dir_list = os.listdir(path)
    if "backup" in dir_list:
        pass
    else:
        folder_name = "backup"
        full_path = os.path.join(path, folder_name)
        os.mkdir(full_path)

    src_path = path + file
    dst_path = path + "/backup/" + data + " (" + "CPY" + ") " + file
    shutil.copy(src_path, dst_path)
    showinfo(
        title='Information',
        message='Plik ' + file + ' skopiowany'
    )


root.title("EU4 Ironman Save Backup")
root.geometry('500x150+50+50')
root.resizable(True, True)
root.iconbitmap('EU.ico')

label = Label(root, text='Kopiowanie pliku do folderu "/backup"')
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

label2 = Label(root, text='ścieżka zapisu save')
label2.grid(row=4, column=0)

btn_open = ttk.Button(root, text="Open", command=open_file_chooser)
btn_open.grid(row=6, column=0)

root.mainloop()
