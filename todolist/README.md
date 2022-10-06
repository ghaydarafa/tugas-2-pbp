Todolist App: https://tugas-2-pbp-rafa.herokuapp.com/todolist/  
login: https://tugas-2-pbp-rafa.herokuapp.com/todolist/login  
register: https://tugas-2-pbp-rafa.herokuapp.com/todolist/register  
create task: https://tugas-2-pbp-rafa.herokuapp.com/todolist/create-task  
logout: https://tugas-2-pbp-rafa.herokuapp.com/todolist/logout  
---
# Tugas 4

### Kegunaan `{% csrf_token %}` dan apa yang terjadi apabila tidak menggunakannya  
Serangan CSRF atau serangan Cross-Site Request Forgery membuat _user_ melakukan _action_ yang tidak diinginkan
di dalam web di mana pengguna tersebut terautentikasi. CSRF Token diperlukan untuk mencegah serangan CSRF. `csrf_token`
akan menghasilkan token dari sisi server ketika melakukan _rendering_ halaman dan untuk setiap _request_ dari _user_
akan dilakukan _cross-check_ terhadap token tersebut. Jika _request_ yang masuk tidak mengandung token tersebut, _request_
tidak akan dijalankan. Apabila form tidak menggunakan `csrf_token`, keamanan _user_ dapat terancam karena memungkinkan
serangan CSRF untuk terjadi.  

### Membuat elemen <form> secara manual  
Tentunya kita dapat membuat elemen <form> secara manual. Caranya adalah dengan mengedit `<nama file template>.html` seperti
kita membuat file html biasanya. Untuk mendapatkan field sebagai atribut dari form kita bisa menggunakan `{{ form.name_of_field }}`
dan menyusunnya seperti menyusun elemen-elemen html pada umumnya. Jangan lupa pula sematkan `{% csrf_token %}` untuk mencegah
serangan CSRF.  
  
### Proses alur data dari submisi, penyimpanan, dan penampilan  
HTML Form membuat _user_ dapat meng-input masukan-masukan yang sesuai. Setelah _user_ melakukan input, akan dibuat HTTP _request_,
_method_, dan argumen ke URL tujuan berdasarkan halaman HTML Form. Server akan menerima HTTP _request_ tersebut dan memanggil _function_
yang sesuai pada `views.py`. _Function_ yang dipanggil akan menyimpan data hasil input ke dalam database Django dan juga menampilkan
halaman HTML yang berisi data yang sudah disesuaikan ke tampilan _user_.  
  
### Cara pengimplementasian _checklist_ tugas  
1. Menjalankan _virtual environment_, membuat aplikasi Todolist, membuat model Task dengan atribut dan tipe field yang sesuai, melakukan migrate  
2. Membuat `todolist.html` sebagai halaman utama todolist berisi tabel dengan data-data yang di-looping sesuai model Task dan _function_ `show_todolist`
serta url-nya untuk menampilkan html tersebut.  
3. Membuat _function_ `register`, `login_user`, `logout_user`, _cookies_, dan membuat perlunya autentikasi untuk mengakses todolist pada `views.py` beserta file html dan url masing-masing.  
4. Membuat `forms.py` dengan form `CreateTaskForm` berisi atribut title dan description. Membuat _function_ `create_task` pada `views.py` untuk meng-_generate_
html form dan menyimpan data hasil input _user_.
5. Membuat `createtask.html` sebagai tampilan halaman create task dan menambahkan path-nya ke url.  
6. Mengerjakan bonus dengan menambahkan atribut `is_finished` pada model dan melakukan migrate, menambahkan tombol delete dan done/undone pada todolist
dan membuat _function_-nya pada `views.py` serta menambahkan path-nya ke url.  
7. Melakukan styling html dengan css.
8. Push ke github untuk di-deploy.
9. Membuat dua akun pengguna dan tiga dummy data menggunakan model `Task` untuk masing-masing pada aplikasi heroku yang sudah di-deploy.

  
# Tugas 5  

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
  * Inline Style
    Inline style yaitu meletakkan style pada tag HTML tertentu dengan atribut `style`. Kelebihan dari cara ini yaitu dapat digunakan ketika ingin mengecek dan melihat perbedaan, berguna untuk perbaikan kecepatan, dan permintaan HTTP yang lebih kecil. Kekurangan inline style adalah kita harus menerapkannya pada setiap elemen HTML.
  
  * Internal CSS
    Kode style CSS ada pada dalam file, diletakkan di dalam tag <style></style> pada bagian <head></head>. Kelebihan dari internal CSS adalah perubahan hanya terjadi di satu halaman jika ingin memiliki style halaman yang berbeda, class dan ID bisa digunakan oleh internal stylesheet, dan tidak perlu mengupload beberapa file karena HTML dan CSS berada pada file yang sama. Kekurangannya adalah intenal CSS dapat meningkatkan waktu akses website dan karena peubahan hanya terjadi pada satu halaman maka akan sulit jika diinginkan beberapa halaman memiliki style yang sama.
  
  * External CSS
    External CSS dilakukan dengan menempatkan style-style pada file .CSS yang kemudian dihubungkan dengan file HTML dengan menuliskan link ke halaman tersebut. Kelebihannya ukuran file HTML lebih kecil dan lebih rapi, kecepatan loading lebih cepat, satu file .CSS bisa digunakan di beberapa halaman. Kekurangannya adalah halaman dapat tampil belum maksimal sebelum file .CSS dipanggil.
  
### Tag HTML5
  Berikut beberapa tag HTML5:
  * < a > : mendefinisikan hyperlink
  * < body > : body dari dokumen
  * < button > : tombol yang dapat ditekan
  * < footer > : mendefinisikan footer dari dokumen atau suatu bagian
  * < form > : html form untuk input dari user
  * < hr > : garis horizontal
  * < img > : merepresentasikan gambar
  * < li > : list dari item-item
  * < p > : mendefinisikan paragraf
  * < style > : memasukkan rincian style suatu elemen
  
  ### Tipe-Tipe Selector
    Berikut beberpa tipe selector:
   * .class : pilih elemen dengan kelas tertentu
   * element : pilih semua elemen dengan tag tertentu
   * #id : pilih elemen dengan id tertentu
   * :active : pilih elemen tertentu yang aktif
   * ::after : masukkan sesuatu di setelah masing-masing elemen tertentu
   * ::before : masukkan sesuatu di sebelum masing-masing elemen tertentu
   * :disabled : pilih elemen tertentu yang di-non-aktifkan
   * :enabled : pilih elemen tertentu yang diaktifkan
   * :focus : pilih input elemen yang memiliki fokus
   * :link : pilih link yang belum dikunjungi
 
  ### Cara pengimplementasian checklist
  Saya melakukan searching melalui internet untuk mendesain halaman html sesuai yang saya inginkan. Saya menggunakan bootstrap dan internal serta inline style untuk styling CSS. Saya menyesuaikan tag untuk membuat elemen yang saya inginkan. Saya juga menggunakan beberapa selector. Selector yang banyak saya gunakan adalah element dan .class.
    
  
