#!/usr/bin/env python
# coding: utf-8

# In[1]:


#kasir_mandiri
import pandas as pd


# In[5]:


class Transaction:
    def __init__(self):
        self.data_belanjaan = dict()
    
    def add_item(self, nama_item, jumlah_item, harga_item):
        try:
            self.data_belanjaan.update({nama_item: [jumlah_item, harga_item, jumlah_item * harga_item]})
        except ValueError:
          print("Input salah!")
    
    def update_item_name(self, nama_item, nama_baru):
        try:
          item = self.data_belanjaan[nama_item]
          self.data_belanjaan.pop(nama_item)
          self.data_belanjaan.update({nama_baru: item})
        except KeyError:
          print("Nama item tidak sesuai!")
    
    def update_item_qty(self, nama_item, jumlah_baru):
        self.data_belanjaan[nama][0] = jumlah_baru
        self.data_belanjaan[nama][2] = jumlah_baru * self.data_belanjaan[nama_item][1]
    
    def update_item_price(self, nama_item, harga_baru):
        self.data_belanjaan[nama][1] = harga_baru
        self.data_belanjaan[nama][2] = harga_baru * self.data_belanjaan[nama_item][0]
    
    def delete_item(self,nama_item):
        self.nama = nama_item
        if nama_item == nama_item:
          self.data_belanjaan.pop(nama_item)
    
    def reset_transaction(self):
        self.data_belanjaan.clear()
        print("Semua item berhasil di hapus!")
    
    def check_order(self):
        if(len(self.data_belanjaan) == 0):
            print("Terdapat Kesalahan Input Data!")
        else:
            data = pd.DataFrame(self.data_belanjaan).T
            data.columns = [ "Jumlah item", "Harga per item", "Total Harga"]
            data["Total Harga"] = data["Jumlah item"] * data["Harga per item"]
            print(data.to_markdown())
    
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




