# Veri İşleme ve Entegrasyon Planı

## 1. Veri Çekme

**Açıklama**: Netflix veri setinin Kaggle'dan elde edilmesi.

- **Dosya**: `data/datasets/netflix_data.csv`
- **İşlemler**:
  - Kaggle'dan Netflix veri seti indirilmiştir.
  - Veri CSV formatında saklanmıştır.

**Hedef**: Güncel ve kapsamlı Netflix verisini elde etmek.

## 2. Veri Temizleme

**Açıklama**: Kaggle'dan elde edilen Netflix verisinin temizlenmesi ve işlenmesi.

- **Dosya**: `data/cleaning/clean_data.py`
- **İşlemler**:
  - Eksik, hatalı veya tutarsız veriler tespit edilmiş ve düzeltilmiştir.
  - Veriler uygun formatlarda düzenlenmiştir (örneğin, tarih formatı, metin temizliği).
  - Gereksiz veriler temizlenmiş ve veri seti optimize edilmiştir.
  - Özellikle süre (`duration`) ve tarih (`date_added`) alanlarında dönüşüm işlemleri yapılmıştır.

**Hedef**: Veriyi analiz ve kullanım için uygun hale getirmek.

## 3. Veritabanı Tasarımı

**Açıklama**: Veritabanının tasarlanması ve yapılandırılması. MySQL ve PostgreSQL arasında karar verilecektir.

- **Dosya**: `backend/config/config.py`
- **İşlemler**:
  - Veritabanı şeması oluşturulacaktır: film tablosu, kullanıcı tablosu, yorum tablosu vs.
  - Tablolar arasındaki ilişkiler tanımlanacaktır (örneğin, film-yorum ilişkisi).
  - Seçilen veritabanına (MySQL veya PostgreSQL) bağlı olarak yapılandırma ve bağlantı ayarları yapılacaktır.

**Hedef**: Verilerin verimli ve güvenli bir şekilde saklanmasını sağlamak.

## 4. Veri Yükleme

**Açıklama**: Temizlenmiş Netflix verilerinin veritabanına yüklenmesi.

- **İşlemler**:
  - Temizlenmiş veri SQL INSERT komutlarıyla veya veritabanı kütüphanesi aracılığıyla yüklenmiştir.
  - Veri yükleme işlemi için bir script oluşturulmuş ve test edilmiştir.

**Hedef**: Verinin veritabanına sorunsuz bir şekilde yüklenmesini sağlamak.

## 5. API Entegrasyonu

**Açıklama**: API ile veritabanı arasındaki etkileşimin sağlanması.

- **Dosyalar**: `backend/api/`, `backend/services/`
- **İşlemler**:
  - API endpoint'leri oluşturulmuştur: film verisi çekme, kullanıcı profili güncelleme vs.
  - API ile veritabanı arasındaki veri alışverişi yönetilmiştir.
  - API güvenliği ve performansı sağlanmıştır.

**Hedef**: API aracılığıyla veritabanına erişim ve veri işlemenin sorunsuz çalışmasını sağlamak.

## 6. Test

**Açıklama**: Veri yükleme ve API entegrasyonunun test edilmesi.

- **Dosyalar**: `tests/`
- **İşlemler**:
  - Birim testleri: Veritabanı işlemleri, veri temizleme.
  - Entegrasyon testleri: API ile veritabanı entegrasyonu.
  - Uçtan uca testler: Kullanıcı akışları, veri işleme süreçleri.

**Hedef**: Sistemin doğru çalıştığını ve hataların olmadığını doğrulamak.

## 7. Geliştirme ve İyileştirme

**Açıklama**: İlk veriyi çektikten ve sistemi test ettikten sonra gerekli iyileştirmelerin yapılması.

- **İşlemler**:
  - Performans iyileştirmeleri yapılacaktır.
  - Kullanıcı geri bildirimlerine göre düzenlemeler yapılacaktır.
  - Yeni özellikler eklenmeye ve mevcut işlevler geliştirmeye devam edilecektir.

**Hedef**: Projeyi sürekli olarak iyileştirmek ve kullanıcı deneyimini artırmak.
