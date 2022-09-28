Todolist App: https://tugas-2-pbp-rafa.herokuapp.com/todolist/  
login: https://tugas-2-pbp-rafa.herokuapp.com/todolist/login  
register: https://tugas-2-pbp-rafa.herokuapp.com/todolist/register  
create task: https://tugas-2-pbp-rafa.herokuapp.com/todolist/create-task  
logout: https://tugas-2-pbp-rafa.herokuapp.com/todolist/logout  
---

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

  
