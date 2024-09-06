# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:18:44 2024

@author: emirh
"""

import pandas as pd

# Veri setini okuma
file_path = "C:/Users/emirh/Desktop/DOSYALAR/veri_bilimi/cinematch/data/datasets/netflix_data.csv"
df = pd.read_csv(file_path)

# İlk 5 satırı görüntüleme
pd.set_option('display.max_columns', None)
print("Veri Setinin İlk 5 Satırı:")
print(df.head())

# Eksik değerlerin kontrolü
print("\nEksik Değerlerin Kontrolü:")
print(df.isnull().sum())

# Eksik değerleri doldurma (Gerekli alanları doldurabilir veya satırları silebilirsiniz)
df['cast'] = df['cast'].fillna('Unknown')

# 'date_added' sütununu datetime formatına çevirme
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# 'duration' sütununu sayısal formata çevirme (dakika veya sezon olarak ayrılması gerekebilir)
# Boş olmayan değerleri kontrol ederek işlem yapıyoruz.
def parse_duration(duration):
    if isinstance(duration, str):  # Sadece string olanları işle
        if 'min' in duration:
            return int(duration.replace(' min', ''))
        elif 'Season' in duration:
            return int(duration.split(' ')[0])
    return None  # Boş veya uygun olmayan durumlar için

# Fonksiyonu uygulama
df['duration_parsed'] = df['duration'].apply(parse_duration)

# 'rating' sütunundaki kategorileri düzenleme (Örneğin, TV-MA, PG-13 vs.)

# listed_in sütununda kategorileri split ederek düzenlemek:
df['listed_in'] = df['listed_in'].apply(lambda x: x.split(', ') if isinstance(x, str) else [])

# Veri setini tekrar gözden geçirme
print("\nÖn İşlemeden Geçmiş Veri Seti:")
print(df.head())

# Temizlenmiş ve işlenmiş veriyi kaydetme
output_path = "C:/Users/emirh/Desktop/DOSYALAR/veri_bilimi/cinematch/data/datasets/processed_netflix_data.csv"
df.to_csv(output_path, index=False)
print(f"\nİşlenmiş veri kaydedildi: {output_path}")

