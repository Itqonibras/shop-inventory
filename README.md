# Tugas 2 PBP
Link : https://shop-inventory-web.adaptable.app/

## Implementasi Checklist
Hal yang pertama kali saya lakukan untuk membuat project Django adalah membuat sebuah directory baru bernama [shop_inventory](https://github.com/Itqonibras/shop-inventory) dan menginisiasi proyek menggunakan terminal. Selanjutnya saya menambahkan *dependencies* yang diperlukan dan mengaitkan *local repository* ke github *repository*. Langkah selanjutnya yang saya lakukan adalah membuat aplikasi main menggunakan terminal dan menambahkannya kedalam berkas 'settings.py'. Dilanjut dengan membuat template 'main.html' yang berisi judul web dan juga tabel yang memiliki atribut name, description, dan amount serta tidak lupa saya juga membuat model untuk atribut tersebut. Saya melakukan migrasi terhadap model yang telah dibuat menggunakan terminal dan juga membuat *function* pada 'views.py' agar template yang telah saya buat dapat ditampilkan. Untuk mengarahkan *function* yang telah saya buat ke 'views.py', saya melakukan routing melalui berkas 'urls.py' dan juga memasukkan routing ke 'urls.py' yang terletak pada direktori proyek. Terakhir saya mengupdate github *repository* saya dan melakukan deploy pada [adaptable.io](https://adaptable.io).

## Bagan Serta Keterkaitan antar Berkas
![Client Request Chart](https://raw.githubusercontent.com/Itqonibras/shop-inventory/images/bagan.png)

## Virtual Environment
Virtual environment digunakan untuk medapatkan membatasi atau mengisolasi *package* dan *dependencies* yang terdapat pada suatu aplikasi. Kita bisa saja membuat suatu aplikasi Django tanpa virtual environment, akan tetapi hal tersebut dapat menyebabkan konflik suatu *package* dengan *package* lainnya dengan versi yang berbeda yang terdapat pada komputer kita.
## Perbedaan MVC, MVT,dan MVVM
Dalam dunia pengembangan web, terdapat istilah seperti MVC, MVT, dan MVVM. Ketiganya merupakan sebuah konsep arsitektur dalam pengembangan web untuk memisahkan komponen-komponen utama dari suatu aplikasi seperti logika bisnis, tampilan, dan interaksi pengguna. Konsep tersebut ditujukan untuk mempermudah proses dalam pengembangan web dan juga mempermudah proses testing.

Perbedaan dari ketiganya adalah:
- MVC (Model-View-Controller)
    1. 
