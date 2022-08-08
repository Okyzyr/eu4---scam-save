import datetime
import linecache
import os
import shutil
import sys
import tkinter as tk
from tkinter import ttk, Label
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo


def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def open_file_chooser():
    filename = askopenfilename()
    with open('cfg.txt', 'w') as file:
        file.writelines(filename)
    file.close()
    restart()


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
    time = datetime.datetime.now()
    data = time.strftime("%m.%d-%H.%M.%S")
    path = file_path()
    file = file_name()
    dir_list = os.listdir(path)
    if "backup" in dir_list:
        pass
    else:
        folder_name = "backup"
        full_path = os.path.join(path, folder_name)
        os.mkdir(full_path)

    src_path = path + file
    dst_path = path + "backup/" + data + " =" + file
    shutil.copy(src_path, dst_path)
    showinfo(
        title='Information',
        message='File ' + file + ' duplicated'
    )
def last_save():
    pass

def quick_save():
    pass

def load_file():
    load_file_name = askopenfilename()
    load_path = load_file_name
    destination_path = file_path()
    split = load_file_name.rindex('=')
    split_backup_path = load_path.rindex('/')
    load_file_name = load_file_name[split + 1:]
    backup_path = load_path[:split_backup_path + 1]
    copy_orig_file = backup_path + load_file_name
    if os.path.exists(destination_path + load_file_name):
        os.remove(destination_path + load_file_name)
        shutil.copy(load_path, copy_orig_file)
        shutil.copy(copy_orig_file, destination_path + load_file_name)
        os.remove(copy_orig_file)
    else:
        shutil.copy(load_path, copy_orig_file)
        shutil.copy(copy_orig_file, destination_path + load_file_name)
        os.remove(copy_orig_file)


root = tk.Tk()

root.title("EU4 Ironman Save Backup")
root.geometry('485x280')
root.resizable(False, False)

# save button
backup_button = ttk.Button(root, text='Copy', command=backup)
backup_button.place(x=67, y=19)

# quick save button
fast_backup = ttk.Button(root, text='Quick Copy', command=quick_save)
fast_backup.place(x=64, y=105)

# load button
load_button = ttk.Button(root, text='Rollback', command=load_file)
load_button.place(x=317, y=19)

# quick load button
quick_load_button = ttk.Button(root, text='Rollback last save', command=last_save)
quick_load_button.place(x=300, y=105)

# select file button
btn_open = ttk.Button(root, text="Select file", command=open_file_chooser)
btn_open.place(x=67, y=185)

# exit button
exit_button = ttk.Button(root, text='Exit', command=lambda: root.quit())
exit_button.place(x=317, y=185)

label2 = Label(root, text='Selected save game path: \n' + file_path())
label2.place(x=10, y=219)
label3 = Label(root, text='Backup file: ' + file_name())
label3.place(x=185, y=255)

root.mainloop()
