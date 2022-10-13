### Perbedaan asynchronous programming dengan synchronous programming  
Asynchronous programming akan melakukan suatu instruksi bersamaan dengan instruksi lainnya sehingga memungkinkan _user_
untuk tetap mengakses aplikasi walaupun suatu operasi lain sedang berjalan. Sedangkan synchronous programming hanya akan 
mengeksekusi satu operasi saja dan operasi lainnya akan di-blok sehingga _user_ harus menunggu operasi lain selesai berjalan 
baru aplikasi dapat diakses kembali.

### Event-Driven Programming  
Event-Driven Programming merupakan suatu cara agar program tertentu dapat berjalan hanya jika suatu _event_ terjadi. Ketika suatu _event_ 
di-_trigger_, maka program akan memanggil fungsi yang bersangkutan dan menjalankan fungsi tersebut. Salah satu contohnya pada tugas ini
adalah ketika `button` di-klik, maka function addTask() akan berjalan.

### Asynchronous programming pada AJAX  
Beberapa penerapan asinkronus pada AJAX di antaranya menggunakan XHR, JQuery, dan FEtchAPI.  
* XHR
  Buat objek XMLHttpRequest dan tentukan HTTP Method dan URL yang ingin dituju dengan dfungsi open. Lalu tentukan fungsi handler pada event `onload` dan
  `onerror`. Terakhir, kirim request dengan fungsi `send()`.  
* JQuery
  Tambahkan library JQuery, kemudian edit fungsi yang diinginkan dengan menggunakan AJAX Jquery. Salah satu contohnya sebagai berikut:  
  `function addTask() {  
            fetch("{% url 'todolist:add_task' %}", {  
                method: "POST",  
                body: new FormData(document.querySelector('#form'))  
            }).then(refreshTodolist)  
            return false  
        }`  
 * Fetch API
   Fetch API adalah gabungan dari XHR dan JQuery. Fungsi fetch akan memanfaatkan suatu Promise. Untuk menggunakan fetch dapat memakai fungsi `fetch()` dengan
   parameter berisi URL tujuan. Kemudian response handling akan menggunakan fungsi `then` yang akan berjalan jika fungsi berhasil dan `catch` yang akan berjalan 
   jika fungsi gagal dilaksanakan.  

### Cara implementasi checklist  
Pertama-tama saya mengikuti langkah berdasarkan solusi Lab 5 dari asdos. Saya membuat view function yang akan menampilkan data json dan 
async function getTodolist() yang akan mengambil data tersebut dengan fetch. Lalu saya membuat async function refreshTodolist() yang akan mengambil data
json tersebut secara asynchronous dan mengiterasi setiap fieldsnya untuk kemudian ditampilkan pada html. Lalu saya membuat form dengan modal bootstrap dan 
membuat fungsi addTask() menggunakan cara Fetch API dan view add_task yang akan membuat objek task baru, serta menambahkan url path yang sesuai.

#### Reference
  * https://www.mendix.com/blog/asynchronous-vs-synchronous-programming/
  * https://www.bbconsult.co.uk/blog/event-driven-applications
  * https://www.dicoding.com/blog/mengenal-fungsi-asynchronous-request-pada-javascript/
