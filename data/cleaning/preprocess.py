# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:18:44 2024

@author: emirh
"""

import pandas as pd

# Veri setlerinin yüklenmesi
imdb_df = pd.read_csv('../datasets/imdb_data.csv')
netflix_df = pd.read_csv('../datasets/netflix_data.csv')

# Başlıkların temizlenmesi ve küçük harfe dönüştürülmesi
imdb_df['title'] = imdb_df['title'].str.strip().str.lower()
netflix_df['title'] = netflix_df['title'].str.strip().str.lower()

# "unknown" başlıkların temizlenmesi
imdb_df = imdb_df[imdb_df['title'] != 'unknown']

# Veri setlerinin birleştirilmesi
merged_df = pd.merge(imdb_df, netflix_df, on='title', how='inner')

# Birleştirilmiş veri setini kontrol et
print("Birleştirilmiş Veri Seti Başlıkları:", merged_df.columns)
print(merged_df.head())

# Birleştirilmiş veri setini kaydetme
merged_df.to_csv('../datasets/merged_movies.csv', index=False)
