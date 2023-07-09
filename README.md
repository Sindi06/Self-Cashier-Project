# Self Cashier Project
Self Cashier merupakan program yang dibuat menggunakan bahasa pemrograman Python. Program ini terdiri dari fungsi penambahan, penghapusan, update, reset, pengecekan dan perhitungan total harga belanjaan yang sudah diinput oleh customer secara mandiri.

## Latar Belakang
Dalam rangka perbaikan proses bisnis, Andi seorang pemilik supermarket besar di salah satu kota di Indonesia memiliki rencana untuk membuat sistem kasir yang self-service. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, harga item yang dibeli dan fitur yang lain. Selain itu, customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut.

## Requirement
1. Membuat program kasir mandiri dengan tools python sederhana yang dapat melakukan tugas:
   - Menambahkan item, jumlah dan harga barang belanjaan
   - Mengganti item, jumlah dan harga barang belanjaan
   - Menghapus salah satu item barang belanjaan
   - Menghapus secara keseluruhan item barang belanjaan
   - Menampilkan daftar barang belanjaan yang sudah diinput untuk dilakukan pengecekan
   - Menampilkan total harga dari keseluruhan belanja yang sudah diinput
2. Membuat module 'self_cashier.py' memuat fungsi-fungsi yang dibutuhkan untuk membuat program kasir mandiri. Dalam modul ini terdapat fungsi class, dictionary, add item, update item, delete item, reset transaction, check order dan total price.
3. Module 'self_cashier.py' membutuhkan modular pandas untuk visualisasi dari barang belanjaan.
4. Membuat module 'test.py' berfungsi untuk menjalankan program pada module 'self_cashier'.

## Flowchart
![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/Flowchart.jpeg?raw=true)

## Penjelasan Code
1. Definisikan fungsi-fungsi di module self_cashier.py lalu simpan dan download as Python (.py)
   - Class : dibuat untuk mendefinisikan seperangkat atribut yang menjadi ciri objek dengan nama transaction
     ![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/Class.png?raw=true)
   - Method : init dibuat untuk menginisialisasi variabel input (nama, jumlah, harga belanjaan) ke dalam bentuk dictionary
     ![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/Init.png?raw=true)
   - Method : add_item untuk menambahkan data belanjaan terdiri dari tiga variabel nama, jumlah dan harga
     ![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/add%20item.png?raw=true)
   - Method : update_item_name untuk mengganti nama item belanja jika sebelumnya belum sesuai
     ![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/Update%20Name.png?raw=true)
   - Method : update_item_qty untuk mengganti jumlah item belanja
     ![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/Update%20Qty.png?raw=true)
   - Method : update_item_price untuk mengganti harga item belanja
     ![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/Update%20Price.png?raw=true)
   - Method : delete_item untuk menghapus salah satu item belanja
     ![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/Delete.png?raw=true)
   - Method : reset_transaction untuk menghapus seluruh item belanja
     ![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/Reset.png?raw=true)
   - Method : check_order untuk melakukan pengecekan daftar item belanja yang sudah diinput, memastikan apakah keseluruhan belanja sudah sesuai
     ![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/Cek%20Order.png?raw=true)
   - Method : total_price untuk menghitung total harga dari keseluruhan belanja yang sudah diinput
     ![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/Total%20price.png?raw=true)
2. Buka Jupyter Notebook dan sesuaikan lokasi penyimpanan module self_cashier.py
3. Buat new notebook untuk menjalankan module self_cashier.py untuk melakukan test case
4. Simpan dan download module test.py tersebut
5. Module test.py menampilkan tampilan awal program dan terhubung ke modul self_cashier.py
   
## Hasil Test Case
1. Customer ingin menambahkan dua item baru menggunakan method add_item(). Item yang ditambahkan adalah sebagai berikut:
   - Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
   - Nama Item: Pasta Gigi, Qty: 3, Harga: 15000
![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/Test%201.png?raw=true)
2. Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan method delete_item() untuk menghapus item. Item yang ingin dihapuskan adalah Pasta Gigi.
![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/Test%202.png?raw=true)
3. Ternyata setelah dipikir - pikir Customer salah memasukkan item yang ingin dibelanjakan. Daripada menghapusnya satu-satu, maka Customer cukup menggunakan method reset_transaction() untuk menghapus semua item yang sudah ditambahkan.
![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/Test%203.png?raw=true)
4. Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price(). Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli.
![alt text](https://github.com/Sindi06/Self-Cashier-Project/blob/main/Pict/Test%204.png?raw=true)

## Kesimpulan
1. Project ini menggunakan function / method seperti add_item(), update_item(), check_order dan total_price sehingga mudah dipahami dan efisien karena script dapat dipanggil berulang kali.
2. Penggunaan try dan except digunakaan untuk menangani error yang mungkin terjadi saat program dijalankan.

## Future Work
1. Membuat tampilan yang lebih bagus untuk mempermudah customer.
2. Mengembangkan program dengan fungsi yang lebih kompleks. Misalnya program khusus member supermarket dengan memasukkan ID member lalu pada akhir total harga akan mendapatkan potongan khusus member.
