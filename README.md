# Tugas 4
## Apa itu UserCreationForm?
UserCreationForm merupakan formulir yang disediakan oleh Django untuk membuat pengguna baru yang dapat menggunakan aplikasi web kita. Formulir ini memiliki tiga bidang yaitu username, password1, dan password2 (password2 digunakan untuk konfirmasi password).

Kelebihan UserCreationForm:
- UserCreationForm merupakan formulir built-in pada Django yang artinya kita tidak perlu untuk membuat dari awal.
- Terdapat Validasi Data: UserCreationForm menyediakan validasi data bawaan, seperti memastikan kata sandi yang dimasukkan memenuhi kebijakan keamanan tertentu.

Kekurangan UserCreationForm:
- Keterbatasan Desain: UserCreationForm memiliki tampilan default yang sederhana dan mungkin tidak sesuai dengan visual aplikasi kita. Kita harus melakukan penyesuaian secara manual jika ingin memiliki tampilan menarik.
- Tidak ada Perlindungan Tambahan: Meskipun Djago melakukan validasi dasar, tidak ada perlindungan tambahan seperti captcha atau pertanyaan tambahan. UserCreationForm juga tidak melakukan validasi email secara default.

## Perbedaan Autentikasi dan Otorisasi Django
Autentikasi adalah proses verifikasi identitas pengguna. Dalam Django, biasanya proses ini memerlukan pengguna untuk memasukkan nama pengguna dan kata sandi, yang kemudian dibandingkan dengan data yang disimpan dalam database. Proses autentikasi bertujuan untuk memastikan bahwa pengguna yang mengakses sistem adalah orang yang memiliki hak dalam mengaksesnya.

Sedangkan otorisasi merupakan proses penentuan apa yang dapat diakses pengguna setelah melakukan autentikasi. Biasanya melibatkan pengecekan terhadap peran atau hak akses pengguna apakah mereka diizinkan untuk melakukan tindakan tertentu. Contoh dari otorisasi adalah akun Admin memiliki akses lebih dibandingkan dengan akun pengguna biasa.

Singkatnya, autentikasi membantu memastikan hanya pengguna yang sah yang dapat mengakses aplikasi, sedangkan otorisasi membantu membatasi apa yang dapat dilakukan setelah proses autentikasi. Kedua konsep ini penting untuk mencegah akses yang tidak sah dan penyalahgunaan aplikasi.
## Pengertian Cookies dan Penggunaannya pada Django
Cookies adalah sejumlah data berukuran kecil berisi informasi yang dikirim oleh server web ke browser dan kemudian dikirim kembali oleh peramban pada page request. Cookies diletakkan di komputer kita ketika kita mengunjungi suatu website. Dalam Django, cookies biasanya digunakan untuk mengelola data sesi pengguna seperti informasi login, pengaturan website, dan menyesuaikan referensi konten yang sesuai penggunanya. Penyimpanan data tersebut disimpan oleh Django pada browser pengguna. Secara singkatnya, cookies adalah "ingatan" Django tentang pengguna dan preferensinya.
## Keamanan dalam Penggunaan Cookies
Penggunaan cookies memang membawa manfaat yang signifikan dalam pengembangan web. Namun, terdapat beberapa resiko dari penggunaan cookies yang perlu diwaspadai, seperti:
- Masalah Privasi: Berdasarkan penggunaan dan sistem kerja pada cookies, secara umum cookies bisa disebut membahayakan privasi karena menyimpan data dan user id seseorang.
- Masalah Keamanan: Cookies merupakan sekumpulan data berisi informasi yang berbentuk teks. Oleh karena itu, cookies dapat menimbulkan resiko keamanan yang memungkinkan seseorang dapat membuka dan merubah pengaturan cookies seseorang lainnya.
## Implementasi Checklist
Hal yang pertama kali saya lakukan adalah membuat method-method pada views.py. Method-method tersebut adalah method register, login_user, logout. Saya juga mengimpor package yang dibutuhkan. Setelah membuat method-method tadi, saya membuat file html untuk tampilan halaman method-method tadi pada folder templates. Lalu saya juga membuat routing method yang sudah dibuat tadi di urls.py pada main. Setelah itu saya meretriksi halaman main agar hanya dapat diakses setelah login. Pada method login_user, saya menambahkan beberapa fungsi untuk mendapatkan sebuah cookie, yaitu data last login. Data last login tadi akan terhapus ketika pengguna logout karena saya menambahkan fungsi untuk menghapus data tersebut pada method logout. Lalu untuk menampilkan last login tadi, saya menambahkan ke method show_main dan mengubah sedikit tampilan html main. Agar setiap object terhubung dengan pembuatnya, saya membuat variable baru pada models.py dengan menggunakan foreignkey. Lalu saya menambahkan beberapa fungsi pada method create_product agar product yang disimpan sesuai dengan pembuatnya. Lalu pada method show_main, saya lakukan filter barang yang ditampilkan hanya barang yang dibuat pembuatnya. Terakhir, saya menjalankan perintah makemigrations pada terminal untuk memigrasi model yang sudah dibuat.
# Tugas 3 PBP
## Perbedaan POST dan GET pada Django
Pada Django, POST dan GET memiliki beberapa perbedaan dari segi fungsi. POST adalah metode untuk melakukan pengiriman data. Data yang akan dikirimkan dikemas oleh browser, dienkripsi, dikirim ke server, lalu menerima response. sedangkan metode GET adalah metode untuk mendapatkan data dari server. 

## Perbedaan XML, JSON, HTML dalam Pengiriman Data
- XML (Extensible Markup Language) digunakan untuk menyimpan dan mengirim data. XML menggunakan tag sebagai representasi datanya dan dapat mempresentasi hampir semua jenis data. Biasanya digunakan dalam web service, dll.

- JSON (JavaScript Object Notation) juga memiliki fungsi untuk menyimpan dan mengirimkan data seperti XML. Namun, JSON merupakan format pertukaran data terbuka dan mudah dibaca oleh mesin maupun manusia. Hal tersebut dikarenakan JSON menggunakan struktur data pada JavaScipt yaitu berupa key dan value.

- HTML (Hypertext Markup Language) adalah bahasa yang digunakan untuk membuat halaman web. HTML menggunakan tag untuk merepresentasikan elemen-elemennya.

Secara umum, perbedaannya adalah XML dan JSON digunakan untuk menyimpan data sedangkan HTML untuk mengatur tampilan visual dari data tersebut

## JSON Sering digunakan dalam Pertukaran Data
JSON lebih sering digunakan dalam pertukaran data pada aplikasi web modern dikarenakan struktur data yang terdapat dalam JSON mudah dipahami dibanding dengan XML atau yang lainnya. Selain itu JSON juga memiliki ukuran yang lebih ringan.

## Implementasi Checklist
Melanjutkan apa yang saya lakukan di TUgas 2, saya menambahkan form untuk menambahkan data dalam aplikasi saya. Dimulai dengan membuat struktur data untuk form dan juga methodnya yang menggunakan method POST. Tidak lupa saya menambahkan method tadi pada show_main di view.py agar data yang diterima dapat ditampilkan. Setelah itu saya membuat HTML yang digunakan untuk menerima input form dan mengirimkan data ke database. Saya juga membuat template HTML yang digunakan untuk seluruh HTML pada aplikasi. Selanjutnya saya membuat method pada viewa.py untuk menampilkan data berupa JSON dan XML dan memastikan responsnya menggunakan POSTMAN. Terakhir, tidak lupa saya menambahkan path dari method yang sudah saya buat kedalam urls.py pada main.


## Screenshot Mengakses Menggunakan POSTMAN
- HTML
![html](images/html.png)
- JSON
![json](images/json.png)
- JSON by Id
![jsonid](images/jsonid.png)
- XML
![xml](images/xml.png)
- XML by Id
![xmlid](images/xmlid.png)


# Tugas 2 PBP
Link : https://shop-inventory-web.adaptable.app/

## Implementasi Checklist
Hal yang pertama kali saya lakukan untuk membuat project Django adalah membuat sebuah directory baru bernama [shop_inventory](https://github.com/Itqonibras/shop-inventory) dan menginisiasi proyek menggunakan terminal. Selanjutnya saya menambahkan *dependencies* yang diperlukan dan mengaitkan *local repository* ke github *repository*. Langkah selanjutnya yang saya lakukan adalah membuat aplikasi main menggunakan terminal dan menambahkannya kedalam berkas 'settings.py'. Dilanjut dengan membuat template 'main.html' yang berisi judul web dan juga tabel yang memiliki atribut name, description, dan amount serta tidak lupa saya juga membuat model untuk atribut tersebut. Saya melakukan migrasi terhadap model yang telah dibuat menggunakan terminal dan juga membuat *function* pada 'views.py' agar template yang telah saya buat dapat ditampilkan. Untuk mengarahkan *function* yang telah saya buat ke 'views.py', saya melakukan routing melalui berkas 'urls.py' dan juga memasukkan routing ke 'urls.py' yang terletak pada direktori proyek. Terakhir saya mengupdate github *repository* saya dan melakukan deploy pada [adaptable.io](https://adaptable.io).

## Bagan Serta Keterkaitan antar Berkas
![bagan](images/bagan.png)
- urls.py memiliki fungsi untuk memilih tampilan (view) berdasarkan request user
- models.py memiliki fungsi untuk menghubungkan database dan view saat mengolah data
- views.py memiliki fungsi untuk melakukan logika bisnis yang dibantu oleh model dan template
- berkas HTML memiliki fungsi untuk menampilkan data-data yang dimiliki

## Virtual Environment
Virtual environment digunakan untuk medapatkan membatasi atau mengisolasi *package* dan *dependencies* yang terdapat pada suatu aplikasi. Kita bisa saja membuat suatu aplikasi Django tanpa virtual environment, akan tetapi hal tersebut dapat menyebabkan konflik suatu *package* dengan *package* lainnya dengan versi yang berbeda yang terdapat pada komputer kita.

## Perbedaan MVT, MVC,dan MVVM
Dalam dunia pengembangan web, terdapat istilah seperti MVC, MVT, dan MVVM. Ketiganya merupakan sebuah konsep arsitektur dalam pengembangan web untuk memisahkan komponen-komponen utama dari suatu aplikasi seperti logika bisnis, tampilan, dan interaksi pengguna. Konsep tersebut ditujukan untuk mempermudah proses dalam pengembangan web dan juga mempermudah proses testing.

Perbedaan dari ketiganya adalah:
### MVT (Model-View-Template)
- Pengguna mengakses satu URL tertentu.
- Django akan mencocokkan URL dengan pola yang sesuai dalam berkas urls.py dan menentukan View yang akan menangani permintaan tersebut.
- View menerima permintaan dan menjalankan logika bisnis yang dibutuhkan oleh aplikasi.
- Jika View memerlukan data dari basis data, View akan berkomunikasi melalui Model sebagai perantara.
- Setelah Model selesai memproses data dalam basis data, View akan menggunakan templat (HTML) untuk merender data tersebut ke dalam tampilan yang diinginkan.
- Setelah templat selesai mengatur tampilan, View akan menghasilkan halaman HTML yang telah dirender bersama dengan respons HTTP yang sesuai.
- Respons HTTP tersebut berisi halaman HTML yang diminta oleh pengguna.
### MVC (Model-View-Controller)
- user berinteraksi dengan view dengan melakukan suatu action.
- action kemudian diteruskan ke Controller, pada Controller action tersebut diproses sesuai kebutuhan aplikasi.
- Controller akan berinteraksi dengan Model untuk mengambil atau mengubah data pada Model.
- Setelah berinteraksi dengan Model, Controller akan  mengupdate data yang akan ditampilkan dan mengirimkan ke View.
- View menerima data dari Controller kemudian mengupdate tampilan interface.
### MVVM (Model-View-ViewModel)
- Pengguna berinteraksi dengan Tampilan melalui tindakan yang dilakukan.
- Tindakan yang diterima oleh Tampilan akan diteruskan ke Model Tampilan (ViewModel).
- ViewModel mengelola logika bisnis aplikasi dan berfungsi sebagai perantara antara Tampilan dan Model.
- Jika diperlukan untuk berinteraksi dengan basis data, Model akan melakukan interaksi tersebut.
- Setelah data dari basis data diperoleh, Model akan meneruskannya ke ViewModel.
- Kemudian, ViewModel akan menjalankan proses yang dibutuhkan oleh aplikasi pada data yang diterima sebelum mengirimkannya kembali ke Tampilan.
- Setelah data yang telah diproses diteruskan ke Tampilan, Tampilan akan melakukan pengaturan tampilan sesuai dengan kebutuhan.
- Setelah itu, pengguna dapat melihat tampilan yang telah diperbarui dan siap untuk melakukan interaksi selanjutnya.



