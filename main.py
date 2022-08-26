import datetime
import linecache
import os
import shutil
import sys
import tkinter as tk
import glob
from tkinter import ttk, Label, simpledialog
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
    new_file_name = data + " " + file
    dir_list = os.listdir(path)
    if "backup" in dir_list:
        pass
    else:
        folder_name = "backup"
        full_path = os.path.join(path, folder_name)
        os.mkdir(full_path)

    src_path = path + file
    dst_path = path + "backup/" + new_file_name
    shutil.copy(src_path, dst_path)
    showinfo(
        title='Information',
        message='File "' + file + '" duplicated as: \n"' + new_file_name + '"'
    )


def sv_info():
    time = datetime.datetime.now()
    data = time.strftime("%m.%d-%H.%M.%S")
    path = file_path()
    file = file_name()
    info = simpledialog.askstring(title="Info", prompt="Add text to save file:")
    new_file_name = data + "-" + info + " " + file
    dir_list = os.listdir(path)
    if "backup" in dir_list:
        pass
    else:
        folder_name = "backup"
        full_path = os.path.join(path, folder_name)
        os.mkdir(full_path)

    src_path = path + file
    dst_path = path + "backup/" + new_file_name
    shutil.copy(src_path, dst_path)
    showinfo(
        title='Information',
        message='File "' + file + '" duplicated as: \n"' + new_file_name + '"'
    )


def quick_save():
    time = datetime.datetime.now()
    data = time.strftime("%m.%d-%H.%M.%S")
    path = file_path()
    file = file_name()
    new_file_name = data + " " + file
    dir_list = os.listdir(path)
    if "backup" in dir_list:
        pass
    else:
        folder_name = "backup"
        full_path = os.path.join(path, folder_name)
        os.mkdir(full_path)

    src_path = path + file
    dst_path = path + "backup/" + new_file_name
    shutil.copy(src_path, dst_path)


def last_save():
    path = file_path()
    files = glob.glob(path + "backup/" + "*.eu4")
    last_save = max(files, key=os.path.getctime)
    split = last_save.rindex(" ")
    newest_file = last_save[split + 1:]
    shutil.copy(last_save, path + newest_file)


def load_file():
    load_file_name = askopenfilename()
    load_path = load_file_name
    destination_path = file_path()
    split = load_file_name.rindex(' ')
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
paddings = {'padx': 20, 'pady': 20}
root.title("EU4 Ironman Save Backup")
root.geometry('475x320')
root.resizable(False, False)
root.configure(bg='gray')

# copy button
backup_button = tk.Button(root, bg="gray", text='Copy and show save name', command=backup)
backup_button.grid(column=1, row=0, sticky=tk.W, **paddings)

# copy with info button
backup_info_button = tk.Button(root, bg="gray", text='Copy with info', command=sv_info)
backup_info_button.grid(column=2, row=0, sticky=tk.W, **paddings)

# quick copy button
fast_backup = tk.Button(root, bg="gray", text='Quick Copy', command=quick_save)
fast_backup.grid(ipadx=10, ipady=30, column=0, row=0, sticky=tk.W, **paddings)

# load button
load_button = tk.Button(root, bg="gray", text='Select file rollback', command=load_file)
load_button.grid(column=1, row=1, sticky=tk.W, **paddings)

# quick load button
quick_load_button = tk.Button(root, bg="gray", text='Rollback to last save', command=last_save)
quick_load_button.grid(column=0, row=1, sticky=tk.W, **paddings)

# select file button
btn_open = tk.Button(root, bg="gray", text="Select file to backup", command=open_file_chooser)
btn_open.grid(column=0, row=2, sticky=tk.W, **paddings)

# exit button
exit_button = tk.Button(root, bg="gray", text='Exit', command=lambda: root.quit())
exit_button.grid(column=1, row=2, sticky=tk.W, **paddings)

try:
    label2 = Label(root, text='Selected save game path: \n' + file_path())
except ValueError:
    open_file_chooser()
finally:
    label2 = Label(root, bg="gray", text='Selected save game path: \n' + file_path())
    label2.place(x=10, y=249)
    label3 = Label(root, bg="gray", text='Selected save file: ' + file_name())
    label3.place(x=10, y=295)

root.mainloop()
