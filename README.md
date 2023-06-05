# Tubes Kelompok 8 PBO
1. Fadlan Dwi Febrio (G1A022051)
2. Rino Alfaridzi Hutomo (G1A022085)
3. Fanni Ghina Athiyyah (G1A022087)

# Soal
Buatlah game sederhana dengan menggunakan python dan buat laporan bagaimana konsep
OOP diterapkan pada pemrograman tersebut.

2. Notepad menggunakan Tkinter dengan Python: Tkinter adalah paket GUI dari python. Kita
dapat membuat notepad sederhana yang terdiri dari berbagai menu seperti cara menyimpan,
membuka, dan mengedit file.

# Source Code dan Penjelasan
- Lihat <a href=https://github.com/Dlann12/TubesKel8PBO/blob/main/UAS.py>Kode GUI Tkinter NotePad.</a><br><br>
Dari kode diaatas saya akan mnejelaskan kode tersebut yang mana pada uas kali ini diberikan pilihan untuk membuat sebuah projek, dan kali ini kami memilih untuk membuat sebuah notepad sederhana, jika dilihat dari pilihan , notepad berada pada pilihan ke 2.

Kode tersebut menggunakan Tkinter yang mana pada tkinter terdapat banyak sekali widget yang dapat digunakan, seperti messagebox dan fledioalog, messagebox berfungsi sebagai pesan yang keluar ketika kita melakukan suatu interaksi terhaapt sesuatu, Modul filedialog dalam library tkinter menyediakan fungsi-fungsi yang memungkinkan pengguna untuk berinteraksi dengan dialog file standar sistem operasi. Kemudian saya memembuat tampilan awal yang diikuti seperti , judul GUI, tata letak, kolom, dan juga ukuran GUI yang akan ditampilkan. lalu saya juga menambahkan function functin layaknya serbuah notepad yaitu, menyimoan file, mengedit file, membuka file, dan sebagainya. Kemudian dialan edit tadi tentunya ada atribut atribut seperti menghapus,mengcopy, dan juga menempel. saya juga menambahkan message box agar saat keluar, menyimoan file, dan lain lain akan ada pemberitahuan sebelum melakukan aksi itu atau biasa disebut double confirm. Kemudain menu menu pada file seperti simpan dan sebagainya, saya juga mengubah background dari notepad ini menjadi warna abu abu, dan akhirnya terbentuklah sebuah notepad sederhana.

Lalu bagaimana oop diterapkan dalam hal ini?
Pada kode yang diberikan, konsep OOP (Object-Oriented Programming) diterapkan dengan menggunakan modul tkinter untuk membuat antarmuka grafis (GUI) NotePad sederhana. Konsep OOP terlihat pada penggunaan kelas Tk() untuk membuat objek utama yang mewakili jendela aplikasi, dan metode-metode lainnya yang digunakan untuk mengatur perilaku dan tampilan aplikasi.Pada baris ini, modul tkinter diimpor dengan alias tk, dan beberapa komponen seperti messagebox dan filedialog juga diimpor untuk digunakan nanti.Dalam OOP, Tk() adalah kelas yang digunakan untuk membuat objek utama yang mewakili jendela aplikasi.Metode mainloop() digunakan untuk memulai loop utama aplikasi yang menunggu input dari pengguna dan merespons peristiwa-peristiwa yang terjadi di jendela aplikasi.Dengan menerapkan konsep OOP, kode tersebut memisahkan logika dan tampilan aplikasi menjadi fungsi-fungsi dan objek-objek yang berinteraksi satu sama lain. Hal ini membuat kode menjadi lebih terstruktur, modular, dan lebih mudah untuk dipahami dan dikelola.
