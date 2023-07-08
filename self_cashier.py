#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Self_Cashier
#Import modul pandas untuk membantu visualisasi tabel pada proses check order

import pandas as pd


# In[5]:


#Fungsi class untuk menjalankan program self cashier
class Transaction:
    
    #Fungsi dictionary untuk menginisiasi data belanjaan
    def __init__(self):
        self.data_belanjaan = dict()
    
    #Fungsi untuk menambahkan item belanjaan
    #nama_item : str
    #jumlah_item : int
    #harga_item : int
    def add_item(self, nama_item, jumlah_item, harga_item):
        try:
            self.data_belanjaan.update({nama_item: [jumlah_item, harga_item, jumlah_item * harga_item]})
        except ValueError:
          print("Input salah!")
    
    #Fungsi untuk mengganti nama item, jika ada kesalahan memasukkan nama item
    def update_item_name(self, nama_item, nama_baru):
        try:
          item = self.data_belanjaan[nama_item]
          self.data_belanjaan.pop(nama_item)
          self.data_belanjaan.update({nama_baru: item})
        except KeyError:
          print("Nama item tidak sesuai!")
    
    #Fungsi untuk mengganti jumlah item
    def update_item_qty(self, nama_item, jumlah_baru):
        self.data_belanjaan[nama][0] = jumlah_baru
        self.data_belanjaan[nama][2] = jumlah_baru * self.data_belanjaan[nama_item][1]
    
    #Fungsi untuk mengubah harga dari suatu item
    def update_item_price(self, nama_item, harga_baru):
        self.data_belanjaan[nama][1] = harga_baru
        self.data_belanjaan[nama][2] = harga_baru * self.data_belanjaan[nama_item][0]
    
    #Fungsi untuk menghapus salah satu item belanjaan
    def delete_item(self,nama_item):
        self.nama = nama_item
        if nama_item == nama_item:
          self.data_belanjaan.pop(nama_item)
    
    #Fungsi untuk menghapus seluruh data belanjaan
    def reset_transaction(self):
        self.data_belanjaan.clear()
        print("Semua item berhasil di hapus!")
    
    #Fungsi untuk menampilkan keseluruhan item belanja yang sudah diinput, untuk dilakukan pengecekan
    def check_order(self):
        if(len(self.data_belanjaan) == 0):
            print("Terdapat Kesalahan Input Data!")
        else:
            data = pd.DataFrame(self.data_belanjaan).T
            data.columns = [ "Jumlah item", "Harga per item", "Total Harga"]
            data["Total Harga"] = data["Jumlah item"] * data["Harga per item"]
            print(data.to_markdown())
    
    #Fungsi untuk menghitung total harga dari seluruh belanjaan yang sudah sesuai
    #dengan ketentuan diskon sebagai berikut:
    #total belanja diatas Rp 200.000 mendapat diskon 5%
    #total belanja diatas Rp 300.000 mendapat diskon 8%
    #total belanja diatas Rp 500.000 mendapat diskon 10%
    def total_price(self):
        total = 0
        for i in self.data_belanjaan.values():
          total += i[2]

    
        if total > 500000:
          total *= 0.9
        elif total > 300000:
          total *= 0.92
        elif total > 200000:
          total *= 0.95
    
        return f"Total belanja yang harus dibayarkan adalah Rp. {format(total, ',')}"


# In[ ]:




