import tkinter as tk
from tkinter import messagebox, filedialog

root = tk.Tk()  # membuat tampilan awal

root.title("NotePad")  # Membuat judul GUI
root.rowconfigure(0, weight=1)  # Mengatur Tata Letak baris
root.columnconfigure(0, weight=1)  # Mengatur tata letak kolom
root.geometry("1000x600")  # Ukuran Gui

current_file = None


def new_file():  # Function Membuat file baru
    global current_file
    current_file = None
    text.delete(1.0, tk.END)


def open_file():  # function membuka file
    global current_file
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        current_file = file_path
        text.delete(1.0, tk.END)
        with open(file_path, "r") as file:
            text.insert(tk.END, file.read())


def save_file():  # function menyimpan file
    global current_file
    if current_file:  # messagebox ketika berhasil disimopan
        with open(current_file, "w") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Simpan", "File berhasil disimpan.")
    else:
        save_file_as()


def save_file_as():  # function menyimopan file sebaqgai
    global current_file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if file_path:  # messagebox ketika berhasil disimopan
        current_file = file_path
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Simpan", "File berhasil disimpan.")


# Function menghapus
def cut():
    text.event_generate("<<Cut>>")


# function menyalin
def copy():
    text.event_generate("<<Copy>>")


# function menempel
def paste():
    text.event_generate("<<Paste>>")


# mesagebox ketika akan exit
def confirm_exit():
    if messagebox.askyesno("Keluar", "Apakah Anda ingin keluar?"):
        if current_file:
            save_file()
        root.destroy()


# Membuat menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Membuat menu "File"
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Baru", command=new_file)
file_menu.add_command(label="Buka", command=open_file)
file_menu.add_command(label="Simpan", command=save_file)
file_menu.add_command(label="Simpan Sebagai", command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="Keluar", command=confirm_exit)

# Membuat menu "Edit"
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Hapus", command=cut)
edit_menu.add_command(label="Salin", command=copy)
edit_menu.add_command(label="Tempel", command=paste)

# Membuat area teks
text = tk.Text(root)
text.pack(fill=tk.BOTH, expand=True)

# Mengatur latar belakang dengan warna
text.configure(background="lightgray")

root.protocol("WM_DELETE_WINDOW", confirm_exit)

root.mainloop()
