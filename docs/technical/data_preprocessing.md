# Veri Ön İşleme Dokümantasyonu

## Proje Bilgisi

Bu doküman, Cinematch projesinde Netflix veri setinin nasıl ön işlendiğini detaylı bir şekilde açıklar. Amaç, veri setini analiz ve modelleme için uygun hale getirmektir.

## Veri Seti

### Netflix Verisi
- **Özellikler:**
  - `show_id`: Gösteri ID'si
  - `type`: Film veya TV şovu
  - `title`: Başlık
  - `director`: Yönetmen
  - `cast`: Oyuncular
  - `country`: Ülke
  - `date_added`: Eklenme tarihi
  - `release_year`: Yayın yılı
  - `rating`: Derecelendirme
  - `duration`: Süre
  - `listed_in`: Kategoriler
  - `description`: Açıklama

## Veri Ön İşleme Adımları

1. **Eksik Değerlerin Kontrolü:**
   - Veri setindeki eksik değerler kontrol edildi. Özellikle `cast`, `country`, `rating`, `duration` gibi sütunlarda eksik değerler bulundu.

2. **Eksik Değerlerin Doldurulması:**
   - `cast` sütunundaki eksik değerler `"Unknown"` olarak dolduruldu.
   - `country` sütunundaki eksik değerler ise işlem görmeden bırakıldı (bu eksik değerler üzerinde ek analiz yapılabilir).
   - `rating` ve `duration` sütunlarındaki eksik değerler uygun şekilde ele alındı.

3. **Tarih Formatının Dönüştürülmesi:**
   - `date_added` sütunu datetime formatına dönüştürüldü. Bu, tarih bazlı analizler yapabilmek için önemlidir.

4. **Süre (Duration) Dönüşümü:**
   - `duration` sütunundaki süre bilgileri, dakika veya sezon olarak ayrıldı. `parse_duration` fonksiyonu kullanılarak süreler sayısal formata dönüştürüldü.

5. **Kategorilerin Düzenlenmesi:**
   - `listed_in` sütunundaki kategoriler, virgüllerle ayrılmış liste formatında düzenlendi. Bu, veri analizi sırasında kategorilerin daha iyi anlaşılmasını sağlar.

6. **Temizlenmiş Verinin Kaydedilmesi:**
   - Ön işlenmiş veri, işlenmiş veri dosyasına kaydedildi. Bu dosya, modelleme ve analiz aşamalarında kullanılmak üzere hazır hale getirildi.

## Gelecek Adımlar

1. **Veri Analizi:** İşlenmiş veri seti üzerinde keşifsel veri analizi yapılacak.
2. **Modelleme:** Veriler, makine öğrenimi algoritmaları ile işlenerek öneri sistemleri geliştirilecek.
3. **API Entegrasyonu:** API'ler aracılığıyla veriler kullanıcı arayüzüne entegre edilecek.

