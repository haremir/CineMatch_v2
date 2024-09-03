# Cinematch Projesi Geliştirme Raporu

## 1. Proje Özeti

Cinematch, film bazlı bir tanışma uygulamasıdır ve Tinder benzeri bir etkileşim yapısıyla kullanıcıların film tercihleri üzerinden bağlantı kurmalarını sağlar. V2 sürümünde, mobil (BeeWare kullanılarak iOS ve Android uyumlu) ve web (Flask tabanlı) versiyonları geliştirilecektir.

## 2. Projenin Teknik Yapısı

### 2.1. Genel Yapı

- **Mobil Uygulama**: BeeWare ile iOS ve Android platformlarında çalışacak.
- **Web Uygulama**: Flask ile geliştirilecek. Kullanıcı arayüzü için HTML/CSS ve JavaScript kullanılacak.
- **Backend**: Python tabanlı API katmanı Flask veya Django REST Framework kullanılarak oluşturulacak.
- **Veritabanı**: MySQL kullanılarak kullanıcı, film, favori ve mesaj verileri depolanacak.

### 2.2. Geliştirme Ortamı

- **IDE**: Spyder (Python için optimize edilmiş, kullanıcı dostu bir geliştirme ortamı).
- **Versiyon Kontrol**: Git ve GitHub kullanılacak. Kod değişiklikleri takip edilecek ve işbirliği sağlanacak.

## 3. Kullanılacak Teknolojiler ve Araçlar

### 3.1. Mobil Geliştirme (BeeWare)

- **Kütüphaneler**: Toga (BeeWare’ın GUI kütüphanesi), SQLite (lokal veri depolama için), HTTP istekleri için `requests` modülü.
- **Geliştirme Süreci**: Mobil uygulama, kullanıcıdan veri alacak ve API ile iletişim kurarak öneriler sunacak. BeeWare’ın native özellikleri kullanılacak.
- **Performans**: Async işlemler, minimum bağımlılık, native bileşenlerin kullanımı.

### 3.2. Web Geliştirme (Flask)

- **Flask Modülleri**: Flask-Restful (API geliştirme), Jinja2 (template engine), WTForms (form işlemleri).
- **Frontend**: HTML, CSS, JavaScript. Tasarımın sade ve işlevsel olması hedeflenecek.
- **Veritabanı Entegrasyonu**: Flask-SQLAlchemy kullanılacak.

### 3.3. Backend ve API Geliştirme

- **Veri Yönetimi**: MySQL veritabanı bağlantısı sağlanacak ve veriler API üzerinden mobil ve web uygulamalarına iletilecek.
- **API Güvenliği**: JWT (JSON Web Tokens) kullanılacak. Kullanıcı doğrulama ve yetkilendirme işlemleri yapılacak.

### 3.4. Veri Kazıma ve Veri Entegrasyonu

- **Araçlar**: Beautiful Soup, Scrapy veya Selenium kullanılacak. IMDb veri kazıma işlemleri bu araçlarla yapılacak.
- **Yasal Uyumluluk**: IMDb verilerini kullanırken yasal çerçevede kalınmalı, mümkünse API tercih edilmeli.

## 4. Geliştirme Süreci ve Detaylı Adımlar

### 4.1. Planlama ve Gereksinim Analizi

- **Hedefler**: Kullanıcı deneyimi odaklı, hızlı, sade ve işlevsel bir uygulama geliştirmek.
- **İhtiyaçlar**: Kullanıcı araştırmaları, veri tabanı şeması, API dokümantasyonu, UI/UX tasarım mockupları.

### 4.2. Geliştirme Aşamaları

1. **Veritabanı Tasarımı**:
   - Kullanıcı, film, favori, beğeni ve mesaj tabloları oluşturulacak.
   - Posterler URL olarak saklanacak, veritabanı performansı için gerekli optimizasyonlar yapılacak.

2. **Mobil Uygulama Geliştirme (BeeWare)**:
   - **Arayüz Tasarımı**: Sade ve performans odaklı bileşenler kullanılacak.
   - **Veri Akışı**: API ile veri alışverişi sağlanacak.
   - **Test ve Optimizasyon**: BeeWare’in emülatörleri kullanılarak cihaz testleri yapılacak.

3. **Web Uygulama Geliştirme (Flask)**:
   - **Backend**: Kullanıcı işlemleri, film önerileri ve mesajlaşma için API geliştirilmesi.
   - **Frontend**: Basit HTML/CSS tasarımları ile hızlı ve etkileşimli bir arayüz oluşturulacak.

4. **API Geliştirme ve Entegrasyon**:
   - **API Katmanı**: Mobil ve web uygulamalarının veri erişimi için ortak bir API oluşturulacak.
   - **Güvenlik**: JWT ve diğer güvenlik önlemleri ile veri güvenliği sağlanacak.

5. **Test ve Hata Ayıklama**:
   - Performans testleri, yük testleri ve güvenlik testleri yapılacak.
   - Kullanıcı geri bildirimleri ile hata düzeltmeleri ve optimizasyonlar yapılacak.

## 5. Geliştirme İçin Gerekli Kaynaklar ve Potansiyel Giderler

### 5.1. Donanım ve Yazılım İhtiyaçları

- **Geliştirici Bilgisayarı**: Orta seviye bir bilgisayar yeterli olacaktır.
- **IDE**: Spyder ücretsizdir, ek maliyet oluşturmaz.
- **Veritabanı Sunucusu**: MySQL Community Edition ücretsizdir, ancak büyük veri işleme gereksinimleri doğarsa ücretli sürüme geçilebilir.
- **Mobil Test Cihazları**: Android ve iOS cihazlar gereklidir; emülatörler kullanılabilir, ancak gerçek cihaz testleri tercih edilir.

### 5.2. Maliyet Kalemleri

- **Hosting**: API ve veritabanı için bir sunucuya ihtiyaç olacak. AWS, DigitalOcean veya Heroku gibi hizmetler kullanılabilir. Maliyetler aylık 5-50 USD arasında değişebilir.
- **Domain ve SSL Sertifikası**: Web uygulaması için gerekli olabilir. Yıllık yaklaşık 20-100 USD maliyeti olabilir.
- **Apple Developer Lisansı**: iOS uygulaması yayınlamak için yıllık 99 USD.
- **Mobil Test Cihazları**: Geliştirme aşamasında test cihazları maliyeti (iPhone ve Android telefonlar) değişken olabilir.

## 6. Riskler ve Çözüm Yolları

- **Performans Sorunları**: Kod optimizasyonu ve test süreçleriyle minimize edilecek.
- **Veri Kazıma Yasal Riskleri**: IMDb API kullanılarak yasal riskler azaltılabilir.
- **Kullanıcı Gizliliği**: Güvenlik önlemleri, veri şifreleme ve kullanıcı izni politikaları ile sağlanacak.
