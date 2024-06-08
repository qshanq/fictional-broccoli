import os
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files(directories, base_name, separate_numbering, use_directory_name):
    try:
        for directory in directories:
            index = 1
            files = sorted(os.listdir(directory))
            image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

            if not image_files:
                messagebox.showerror("エラー", f"{directory} に画像ファイルが見つかりません。")
                continue

            for filename in image_files:
                ext = os.path.splitext(filename)[1]
                if use_directory_name:
                    new_name = f"{base_name}_{os.path.basename(directory)}_{index:03}{ext}"
                else:
                    new_name = f"{base_name}{index:03}{ext}"
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
                index += 1

        messagebox.showinfo("完了", "ファイル名の変更が完了しました。")

    except Exception as e:
        messagebox.showerror("エラー", f"ファイル名の変更中にエラーが発生しました: {e}")

def select_directories():
    directories = filedialog.askdirectory()
    if directories:
        directories_list = [directories]
        while True:
            additional_directory = filedialog.askdirectory()
            if additional_directory:
                directories_list.append(additional_directory)
            else:
                break
        entry_directories.delete(0, tk.END)
        entry_directories.insert(0, directories_list)

def start_rename():
    directories = entry_directories.get().split()
    base_name = entry_base_name.get()
    separate_numbering = separate_var.get()
    use_directory_name = use_directory_var.get()

    if not directories or not base_name:
        messagebox.showerror("エラー", "ファイルとファイル名を指定してください。")
        return

    rename_files(directories, base_name, separate_numbering, use_directory_name)

# GUIのセットアップ
root = tk.Tk()
root.title("画像ファイルのリネームアプリ by qshanq ")

tk.Label(root, text="ディレクトリ:").grid(row=0, column=0, padx=10, pady=10)
entry_directories = tk.Entry(root, width=50)
entry_directories.grid(row=0, column=1, padx=10, pady=10)
btn_browse = tk.Button(root, text="参照", command=select_directories)
btn_browse.grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="ファイル名(数字の前の文字列):").grid(row=1, column=0, padx=10, pady=10)
entry_base_name = tk.Entry(root, width=50)
entry_base_name.grid(row=1, column=1, padx=10, pady=10)

separate_var = tk.BooleanVar()
separate_checkbtn = tk.Checkbutton(root, text="ファイルごとにナンバリングする", variable=separate_var)
separate_checkbtn.grid(row=2, column=1, padx=10, pady=5)

use_directory_var = tk.BooleanVar()
use_directory_checkbtn = tk.Checkbutton(root, text="親ファイル名をファイル名の一部とする", variable=use_directory_var)
use_directory_checkbtn.grid(row=3, column=1, padx=10, pady=5)

btn_start = tk.Button(root, text="リネーム開始", command=start_rename)
btn_start.grid(row=4, column=1, pady=20)

root.mainloop()