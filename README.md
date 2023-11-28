# YouTube Kanal Abone Sayısı Kontrolü

Bu Python projesi, belirli bir YouTube kanalının abone sayısını almak için YouTube Data API'yi kullanır. Proje, Google Developer Console üzerinden alınan bir API anahtarı ile çalışır.

## Nasıl Kullanılır

1. **API Anahtarı Oluşturun:**
    - [Google Developer Console](https://console.developers.google.com/) adresine gidin.
    - Yeni bir proje oluşturun ve YouTube Data API v3'ü etkinleştirin.
    - "Kimlik Bilgileri" bölümünde bir API anahtarı oluşturun.

2. **Proje Ayarlarını Yapın:**
    - `main.py` dosyasındaki `api_key` değişkenine oluşturduğunuz API anahtarını ekleyin.
    - `channel_id` değişkenine kontrol etmek istediğiniz YouTube kanalının ürün kimliğini ekleyin.

3. **Gerekli Kütüphaneyi Yükleyin:**
    ```bash
    pip install google-api-python-client
    ```

4. **Projeyi Çalıştırın:**
    ```bash
    python main.py
    ```

## Dikkat Edilmesi Gerekenler

- Bu proje, YouTube Data API'yi kullanır. Bu nedenle, API sınırlamalarına ve politikalarına dikkat edilmelidir.
- Projenin çalışabilmesi için internet bağlantısına ihtiyaç vardır.

## Katkıda Bulunma

- Bu proje açık kaynaklıdır. Her türlü katkı ve öneriye açıktır. Fork yapabilir ve pull request gönderebilirsiniz.


