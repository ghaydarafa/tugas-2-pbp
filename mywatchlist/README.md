mywatchlist App: https://tugas-2-pbp-rafa.herokuapp.com/mywatchlist/  
    in html: https://tugas-2-pbp-rafa.herokuapp.com/mywatchlist/html  
    in xml: https://tugas-2-pbp-rafa.herokuapp.com/mywatchlist/xml  
    in json: https://tugas-2-pbp-rafa.herokuapp.com/mywatchlist/json  
--

### Perbedaan JSON, XML, dan HTML
|    JSON                 |    XML                   |    HTML                 |
--------------------------|--------------------------|-------------------------|
JavaScript Object Notation|eXtensible Markup Language|Hypertext Markup Language|
Fokus pada transfer data  |Fokus pada transfer data  |Fokus pada penyajian data|
Format dalam JavaScript   |Markup Language           |Markup Language          |
Data disimpan sebagai key-value|Data disimpan sebagai tree structure|Data disimpan sebagai tree structure|
Transmisi data cepat      |Transmisi data lambat     | - |

### Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?  
Kita memerlukan data delivery dalam pengimplementasian sebuah platform untuk mengirim data dari satu stack ke stack lain di saat data tersebut dibutuhkan.

### Bagaimana cara saya mengimplementasikan checklist pada tugas
Mengikuti tutorial Lab 1 dan Lab 2, saya membuat aplikasi mywatchlist, membuat models.py berisi beberapa type field sebagai atribut aplikasi ini,
menambahkan initial_mywatchlist_data.json sesuai dengan field yang ada pada model, membuat mywatchlist.html sebagai template, menambahkan function show_watchlist
untuk menampilkan data dalam html, show_xml untuk menampilkan data dalam xml, show_json untuk menampilkan data dalam json, dan show_by_id untuk menampilkan data
berdasarkan idnya. Saya juga melakukan migrate dan loaddata. Kemudian saya membuat testing untuk ketiga link html, xml, dan json. Saya juga menambahkan perintah
untuk loaddata bagi heroku di procfiles, serta merubah value dari STATICFILES_STORAGE pada settings.py agar testing tidak meminta style css.
Ketika saya melakukan push ke github maka aplikasi akan ter-deploy secara otomatis pada link heroku Tugas 2 sebelumnya karena saya menggunakan repositori yang sama.

### POSTMAN  
* HTML  
<img width="960" alt="image" src="https://user-images.githubusercontent.com/85816679/191782214-181a7ace-d34d-46d1-b483-60de40ae16c6.png">  

* XML  
<img width="960" alt="image" src="https://user-images.githubusercontent.com/85816679/191782412-e8229290-a412-4d3b-80ee-680e46bdfae9.png">  

* JSON
<img width="960" alt="image" src="https://user-images.githubusercontent.com/85816679/191782503-0726d008-f681-43ff-9fd4-bb8a52ccac0f.png">  

