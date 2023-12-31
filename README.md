# Tugas 6
link: nibras-itqon-tugas.pbp.cs.ui.ac.id

## Sinkronus dan Asinkronus dalam Pemrograman
**Sinkronus** dalam pemrograman berarti program yang dieksekusi berjalan secara berurutan. Program tidak akan lanjut ke barisan berikutnya sebelum baris yang dieksekusi selesai berjalan. Sedangkan **Asinkronus** berarti program yang dieksekusi dapat berjalan secara bersamaan tanpa harus menunggu operasi sebelumnya selesai dijalankan.
## Paradigma Event-Driven Programming dalam JavaScript dan AJAX
Paradigma event-driven programming dalam JavaScript dan AJAX adalah pendekatan dimana sebuah program merespon event atau peristiwa yang terjadi. Contoh dalam tugas ini adalah sebuah method add_product_ajax yang di mana ketika method dijalankan program akan merespon dengan mengirim data ke server dan mengembalikan response.
## Penerapan Asynchronous pada AJAX
Penerapan asinkronus pada AJAX biasanya dilakukan ketika membuat permintaan AJAX seperti mengambil data dari server. Contohnya bisa dilihat pada penggunaan fetch(), await() dan then(). fetch() berfungsi untuk membuat permintaan ke server, await() untuk menunggu kode yang sedang berjalan selesai dijalankan, dan then() untuk memanggil method yang akan dijalankan setelah proses fetch selesai
## Perbandingan Fetch API dengan jQuery untuk Penerapan AJAX
**Fetch API** adalah standar JavaScript yang disediakan oleh browser modern yang merupakan cara bawaan untuk membuat permintaan HTTP dan mengelola responsnya.
Fetch API lebih modern dan lebih ringan daripada jQuery, yang berarti lebih efisien dalam hal ukuran dan kinerja.
Lebih modular dan memungkinkan untuk menggunakan berbagai jenis respons, seperti JSON, teks, atau bahkan BLOB.

**jQuery** adalah pustaka JavaScript yang lebih tua dan lebih besar yang menyediakan banyak fitur dan utilitas, termasuk AJAX.
Kompatibilitas lintas browser yang baik, karena jQuery merawat perbedaan implementasi di berbagai browser.

Kita dapat menggunakan fetch API ketika mengembangkan aplikasi web modern di mana kinerja, ukuran, dan kejelasan kode adalah hal yang penting.
## Implementasi Checklist
Hal yang pertama kali saya lakukan adalah membuat method `add_product` dan `delete_product` yang menggunakan ajax dan method `get_product` dari JSON pada `views.py`, lalu mendaftarkannya pada `urls.py` pada app main. Langkah selanjutnya saya mengubah tabel pada `main.html` menjadi sebuah fungsi yang mengimplementasikan method `get_product_json` tadi. Setelah itu saya membuat sebuah button yang akan menambilkan modal dan button untuk menghapus product. Selanjutnya saya menambahkan Modal pada `main.html` yang menampilkan form dan terdapat sebuah tombol untuk melakukan input data form tadi yang mengimplementasikan method `add_product_ajax`. Terakhir saya melakukan perintah Collecstatic pada terminal.
# Tugas 5
## Manfaat Element Selector
Element selector digunakan untuk menerapkan gaya tampilan kepada suatu element HTML yang sama. Misalnya kita memiliki beberapa element < p > pada suatu file HTML dan ingin menerapkan gaya pada semua element < p >. Kita dapat menerapkan element selector p pada CSS dan mengatur gaya tampilannya kemudian semua elemen < p > akan berubah.
## HTML5 Tag
Beberapa tag HTML5 yang saya ketahui:
- < header >: Digunakan untuk mengatur bagian atas aplikasi web seperti judul dan logo.
- < nav >: Digunakan untuk mengelompokkan elemen-elemen yang terkait dengan navigasi seperti menu.
- < main >: Berisi dari konten utama suatu halaman web.
- < footer >: Digunakan untuk mengatur bagian bawah dari aplikasi web. Biasanya digunakan untuk menuliskan hak cipta suatu aplikasi.
- < section >: Digunakan untuk mengelompokkan elemen-elemen dengan konten terkait.
## Margin vs Padding
Margin dan padding merupakan properti pada CSS yang mengatur ruang suatu elemen/content. Margin digunakan untuk mengatur ruang diluar elemen. Mudahnya, margin digunakan untuk memberikan jarak suatu elemen dengan elemen lainnya. Sedangkan padding digunakan untuk mengatur ruang didalam elemen. Padding memberikan ruang untuk content yang berada dalam suatu elemen.
![margin](images/margin.png)
Contoh Margin.
![padding](images/padding.png)
Contoh Padding.
## Tailwind vs Bootstrap
Tailwind dan Bootstrap merupakan framework CSS yang paling sering digunakan oleh orang-orang. Perbedaan keduanya terdapat pada fitur apa yang ditawarkan. Bootstrap memiliki banyak komponen yang siap pakai dan mudah disesuaikan dalam desain web. Sedangkan Tailwind dapat memungkinkan kita untuk mengkostumisasi tampilan komponen kita sendiri. Terkait penggunaannya, dapat disesuaikan dengan kebutuhan kita. Kita dapat menggunakan Bootstrap ketika kita membutuhkan komponen yang sudah siap pakai. Sedangkan ketika kita ingin memiliki kontrol lebih dalam desain kita, maka kita dapat menggunakan Tailwind.
## Implementasi Checklist
Sebelum masuk ke implementasi cheklist, saya membuat dua buah fungsi baru create_product dan delete_product dan melakukan routing untuk keduanya pada urls.py. Setelah itu barulah saya memulai mengubah tampilan aplikasi. langkah pertama yang saya lakukan adalah menambahkan framework bootstrap untuk semua halaman pada aplikasi dengan menambahkan pada base.html. Kemudian saya mengatur tiap konten pada halaman agar enak dipandang dengan menambahkan padding untuk setiap konten yang ada pada setiap halaman. Saya juga mengatur warna untuk row terakhir pada table di main.html dengan menambahkan atribut pada tag style. Terakhir saya membuat navbar untuk setiap halaman.

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