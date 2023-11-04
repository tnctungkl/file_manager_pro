import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil


def show_last_action(action_text, cancelled=False):
    status_text = f'Last Action: {action_text}'
    if cancelled:
        status_text += ' (Cancelled)'
    status_label.config(text=status_text)
    root.update_idletasks()


def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            os.startfile(file_path)
            show_last_action("Open File")
        except:
            messagebox.showinfo('Failed!', 'File not found!')


def copy_file():
    source_file = filedialog.askopenfilename()
    destination_folder = filedialog.askdirectory()
    if source_file and destination_folder:
        try:
            shutil.copy(source_file, destination_folder)
            show_last_action("Copy File")
            messagebox.showinfo('Congratulations', 'File Copied')
        except:
            messagebox.showinfo('Failed!', 'File could not be copied.')


def delete_file():
    file_to_delete = filedialog.askopenfilename()
    if file_to_delete:
        if os.path.exists(file_to_delete):
            os.remove(file_to_delete)
            show_last_action("Delete File")
        else:
            messagebox.showinfo('Failed!', 'File not found!')


def rename_file():
    file_to_rename = filedialog.askopenfilename()
    if file_to_rename:
        new_name = filedialog.asksaveasfilename(initialfile=os.path.basename(file_to_rename))
        if new_name:
            try:
                os.rename(file_to_rename, new_name)
                show_last_action("Rename File")
                messagebox.showinfo('Congratulations', 'File Renamed!')
            except:
                messagebox.showinfo('Failed!', 'File could not be renamed.')


def create_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        new_folder_name = filedialog.simpledialog.askstring("New Folder", "Enter folder name:")
        if new_folder_name:
            new_folder_path = os.path.join(folder_path, new_folder_name)
            os.mkdir(new_folder_path)
            show_last_action("Create Folder")
            messagebox.showinfo('Congratulations', 'Folder created!')


def delete_folder():
    folder_to_delete = filedialog.askdirectory()
    if folder_to_delete:
        try:
            os.rmdir(folder_to_delete)
            show_last_action("Delete Folder")
            messagebox.showinfo('Congratulations', 'Folder Deleted!')
        except:
            messagebox.showinfo('Failed!', 'Folder could not be deleted.')


def list_files():
    folder_to_list = filedialog.askdirectory()
    if folder_to_list:
        file_list = os.listdir(folder_to_list)
        show_last_action("List Files")
        messagebox.showinfo('Files in {}'.format(folder_to_list), '\n'.join(file_list))


root = tk.Tk()
root.geometry('600x500')
root.title('File Manager PRO v1.1.0.a')

frame = tk.Frame(root)
frame.pack(pady=20)
tk.Label(frame, text="File Manager PRO!", bg="Red").pack()

frame1 = tk.Frame(root, borderwidth=2, relief="solid", padx=10, pady=10)
frame1_label = tk.Label(root, text="File Parts")
frame1_label.pack(side="left", padx=10, pady=20)
frame1.pack(side="left", padx=10, pady=20)

open_icon = tk.PhotoImage(file="C:/file_manager/icons/search.png")
copy_icon = tk.PhotoImage(file="C:/file_manager/icons/copy.png")
delete_icon = tk.PhotoImage(file="C:/file_manager/icons/cut.png")
rename_icon = tk.PhotoImage(file="C:/file_manager/icons/duplicate.png")

button_open = tk.Button(frame1, image=open_icon, text="Open File", compound="top", command=open_file, bd=1,
                        cursor="hand2")
button_copy = tk.Button(frame1, image=copy_icon, text="Copy file", compound="top", command=copy_file, bd=1,
                        cursor="hand2")
button_delete = tk.Button(frame1, image=delete_icon, text="Delete File", compound="top", command=delete_file, bd=1,
                          cursor="hand2")
button_rename = tk.Button(frame1, image=rename_icon, text="Rename file", compound="top", command=rename_file, bd=1,
                          cursor="hand2")

button_open.pack(pady=10, fill="both", expand=True)
button_copy.pack(pady=10, fill="both", expand=True)
button_delete.pack(pady=10, fill="both", expand=True)
button_rename.pack(pady=10, fill="both", expand=True)

frame2 = tk.Frame(root, borderwidth=2, relief="solid", padx=10, pady=10)
frame2_label = tk.Label(root, text="Folder Parts")
frame2_label.pack(side="right", padx=10, pady=20)
frame2.pack(side="right", padx=10, pady=20)

new_folder = tk.PhotoImage(file="C:/file_manager/icons/new.png")
remove_folder = tk.PhotoImage(file="C:/file_manager/icons/delete.png")
list_folder = tk.PhotoImage(file="C:/file_manager/icons/duplicut.png")

button_newfol = tk.Button(frame2, image=new_folder, text="New Folder", compound="top", command=create_folder, bd=1,
                          cursor="hand2")
button_delfol = tk.Button(frame2, image=remove_folder, text="Remove Folder", compound="top", command=delete_folder,
                          bd=1, cursor="hand2")
button_lisfol = tk.Button(frame2, image=list_folder, text="List Folder", compound="top", command=list_files, bd=1,
                          cursor="hand2")

button_newfol.pack(pady=10, fill="both", expand=True)
button_delfol.pack(pady=10, fill="both", expand=True)
button_lisfol.pack(pady=10, fill="both", expand=True)

status_label = tk.Label(root, text='', bg="LightGray")
status_label.pack(side="bottom", padx=10, pady=20)

root.mainloop()
