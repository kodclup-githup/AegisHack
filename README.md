# AegisHack - Işık Hızında Çoklu Protokol Saldırı Aracı

![AegisHack Banner](https://img.shields.io/badge/AegisHack-Ultra%20Fast-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)

## ⚠️ YASAL UYARI

**Bu araç yalnızca eğitim ve yetkili test amaçlı geliştirilmiştir. İzinsiz kullanım YASAKTIR!**

- ✅ Sadece size ait olan sistemlerde kullanın
- ✅ Yerel test ortamında eğitim amaçlı kullanın  
- ✅ Yetkili penetrasyon testlerinde kullanın
- ❌ İzinsiz sistemlere saldırı yapmayın
- ❌ Yasadışı aktivitelerde kullanmayın

**Yasal sorumluluk kullanıcıya aittir. Geliştirici hiçbir yasal sorumluluk kabul etmez.**

## 🚀 AegisHack vs Hydra - Nesiller Ötesi Teknoloji

AegisHack, geleneksel brute force araçlarından **kat kat daha güçlü** ve **birkaç nesil ilerisinde** bir teknolojidir:

### 🔥 Hydra'dan Üstün Özellikler:

| Özellik | Hydra | AegisHack |
|---------|-------|-----------|
| **Thread Sayısı** | Max 64 | **200+ Ultra Fast** |
| **Protokol Desteği** | 50+ | **Gelişmiş 12+ Protokol** |
| **CAPTCHA Bypass** | ❌ | ✅ **Akıllı Bypass** |
| **WAF Bypass** | ❌ | ✅ **Gelişmiş Evasion** |
| **Real IP Change** | ❌ | ✅ **VPN/Proxy Rotation** |
| **Threat Detection** | ❌ | ✅ **Real-time Bypass** |
| **Wordlist Yönetimi** | Basit | ✅ **Akıllı Wordlist** |
| **Hız** | Orta | ✅ **Işık Hızı** |

### ⚡ Ultra Güçlü Özellikler:

- **🔥 Işık Hızında Multi-Threading (200+ threads)**
- **🔄 Gerçek IP Değiştirme (VPN/Proxy rotation)**
- **🛡️ CAPTCHA/WAF Algılama ve Bypass**
- **📁 Gerçek Wordlist Dosyaları (küçük/orta/büyük)**
- **🎯 Advanced Evasion Techniques**
- **⚡ Real-time Threat Detection Bypass**
- **🌐 Proxy Rotation ve Stealth Mode**
- **📊 Ultra Detaylı Raporlama**

## 🎯 Desteklenen Protokoller

- **HTTP/HTTPS** - Web Form Attacks
- **FTP** - File Transfer Protocol
- **SSH** - Secure Shell (Paramiko)
- **Telnet** - Remote Access
- **MySQL** - Database Server
- **SMTP** - Email Server
- **POP3** - Email Retrieval
- **IMAP** - Email Access
- **RDP** - Remote Desktop
- **VNC** - Virtual Network Computing
- **SNMP** - Network Management

## 📋 Sistem Gereksinimleri

- **Python 3.7+**
- **RAM: Minimum 2GB (Önerilen 4GB+)**
- **İşlemci: Multi-core (Önerilen)**
- **İnternet Bağlantısı**

## 🛠️ Kurulum Adımları

### 📱 Termux (Android) Kurulumu

```bash
# 1. Termux'u güncelleyin
pkg update && pkg upgrade -y

# 2. Python ve git kurun
pkg install python git -y

# 3. Pip'i güncelleyin
pip install --upgrade pip

# 4. Projeyi klonlayın
git clone https://github.com/kodclup-githup/AegisHack.git

# 5. Proje dizinine girin
cd AegisHack

# 6. Gerekli paketleri kurun
pip install -r requirements.txt

# 7. Aracı çalıştırın
python AegisCrack.py
```

### 🐧 Linux Kurulumu

```bash
# 1. Sistemi güncelleyin
sudo apt update && sudo apt upgrade -y

# 2. Python ve pip kurun
sudo apt install python3 python3-pip git -y

# 3. Projeyi klonlayın
git clone https://github.com/kodclup-githup/AegisHack.git

# 4. Proje dizinine girin
cd AegisHack

# 5. Gerekli paketleri kurun
pip3 install -r requirements.txt

# 6. Aracı çalıştırın
python3 AegisCrack.py
```

### 🪟 Windows Kurulumu

```cmd
# 1. Python'u indirin ve kurun (python.org)
# 2. Command Prompt'u yönetici olarak açın

# 3. Git'i kurun (git-scm.com) veya GitHub Desktop kullanın

# 4. Projeyi klonlayın
git clone https://github.com/kodclup-githup/AegisHack.git

# 5. Proje dizinine girin
cd AegisHack

# 6. Gerekli paketleri kurun
pip install -r requirements.txt

# 7. Aracı çalıştırın
python AegisCrack.py
```

### 🔧 Manuel Paket Kurulumu (Sorun Yaşanırsa)

```bash
# Temel paketler
pip install requests paramiko mysql-connector-python colorama

# Opsiyonel paketler
pip install socks pysocks python-nmap
```

## 🚀 Kullanım Kılavuzu

### 1️⃣ Temel Kullanım

```bash
python AegisCrack.py
```

### 2️⃣ Adım Adım Kullanım

1. **Etik Kullanım Onayı**: "EVET" yazarak onaylayın
2. **Protokol Seçimi**: 1-11 arası protokol seçin
3. **Hedef Bilgileri**: IP/Domain ve port girin
4. **Wordlist Seçimi**: Küçük/Orta/Büyük liste seçin
5. **Ultra Seçenekler**: Gelişmiş özellikleri aktifleştirin
6. **Saldırıyı Başlatın**: "EVET" yazarak başlatın

### 3️⃣ Ultra Seçenekler

- **Thread Sayısı**: 1-200 arası (Önerilen: 50-100)
- **Ultra Fast Mode**: Maksimum hız için aktifleştirin
- **Real IP Change**: VPN/Proxy rotation için
- **CAPTCHA Bypass**: CAPTCHA algılama ve bypass
- **WAF Bypass**: Web Application Firewall bypass
- **Proxy Rotation**: Proxy listesi kullanımı

## 📊 Wordlist Dosyaları

Araç otomatik olarak 3 farklı boyutta wordlist oluşturur:

### 📁 Kullanıcı Listeleri:
- **usernames_small.txt** (5 kullanıcı)
- **usernames_medium.txt** (16 kullanıcı)  
- **usernames_large.txt** (36 kullanıcı)

### 🔐 Parola Listeleri:
- **passwords_small.txt** (5 parola)
- **passwords_medium.txt** (16 parola)
- **passwords_large.txt** (44 parola)

## 🛡️ Güvenlik Özellikleri

### 🔍 Algılama Sistemleri:
- **CAPTCHA Detection**: Otomatik CAPTCHA algılama
- **WAF Detection**: Web Application Firewall algılama
- **Rate Limiting**: Hız sınırı algılama
- **Threat Detection**: Gerçek zamanlı tehdit algılama

### 🚀 Bypass Teknikleri:
- **User-Agent Rotation**: Rastgele User-Agent değiştirme
- **Header Manipulation**: HTTP header manipülasyonu
- **Cookie Manipulation**: Çerez manipülasyonu
- **Referrer Spoofing**: Referrer sahtecilik
- **IP Rotation**: Gerçek IP değiştirme

## 📈 Performans Optimizasyonu

### ⚡ Ultra Fast Mode:
- **Delay**: 0.001 saniye
- **Timeout**: 1 saniye
- **Max Threads**: 200+
- **Rate**: 1000+ deneme/saniye

### 🎯 Normal Mode:
- **Delay**: 0.01 saniye
- **Timeout**: 3 saniye
- **Max Threads**: 50
- **Rate**: 100+ deneme/saniye

## 📋 Çıktı Formatları

### 📊 Gerçek Zamanlı İzleme:
```
[⚡PROGRESS] 45.2% | Attempts: 452/1000 | Success: 2 | Rate: 125.3/s | Threads: 50 🛡️🔄
```

### 📄 JSON Raporu:
```json
{
  "target": "192.168.1.100:22",
  "protocol": "ssh",
  "successful_credentials": [
    ["admin", "123456"],
    ["root", "password"]
  ],
  "security_features": {
    "captcha_bypass": true,
    "waf_bypass": true,
    "proxy_rotation": true
  }
}
```

## 🔧 Sorun Giderme

### ❌ Yaygın Hatalar:

1. **ModuleNotFoundError**: 
   ```bash
   pip install -r requirements.txt
   ```

2. **Permission Denied**:
   ```bash
   sudo python3 AegisCrack.py  # Linux
   # Veya yönetici olarak çalıştırın (Windows)
   ```

3. **Connection Timeout**:
   - Hedef IP/port kontrolü yapın
   - Firewall ayarlarını kontrol edin
   - VPN/Proxy ayarlarını kontrol edin

4. **Thread Hatası**:
   - Thread sayısını azaltın (10-50 arası)
   - RAM kullanımını kontrol edin

## 🎓 Eğitim Amaçlı Kullanım

### 📚 Öğrenme Hedefleri:
- **Brute Force Saldırıları**: Nasıl çalışır ve nasıl korunulur
- **Protokol Güvenliği**: Farklı protokollerin zafiyetleri
- **Güvenlik Testleri**: Penetrasyon testi teknikleri
- **Savunma Mekanizmaları**: CAPTCHA, WAF, Rate Limiting

### 🏠 Test Ortamı Kurulumu:
```bash
# Yerel test sunucusu (örnek)
# FTP Server
sudo apt install vsftpd

# SSH Server  
sudo apt install openssh-server

# Web Server
sudo apt install apache2

# MySQL Server
sudo apt install mysql-server
```

## 📞 Destek ve Katkı

### 🐛 Hata Bildirimi:
- GitHub Issues kullanın
- Detaylı hata açıklaması yapın
- Sistem bilgilerini ekleyin

### 🤝 Katkıda Bulunma:
- Fork yapın
- Feature branch oluşturun
- Pull request gönderin

### 📧 İletişim:
- **GitHub**: [kodclup](https://github.com/kodclup-githup)
- **Repository**: [AegisHack](https://github.com/kodclup/AegisHack)

## 📜 Lisans

Bu proje eğitim amaçlı geliştirilmiştir. MIT Lisansı altında dağıtılmaktadır.

## 🔄 Güncellemeler

### v1.0.0 (2024):
- ✅ İlk sürüm yayınlandı
- ✅ 12 protokol desteği
- ✅ Ultra fast mode
- ✅ CAPTCHA/WAF bypass
- ✅ Real IP change

### Gelecek Güncellemeler:
- 🔄 Daha fazla protokol desteği
- 🔄 AI tabanlı bypass teknikleri
- 🔄 GUI arayüz
- 🔄 Mobil uygulama

---

**⚠️ Dikkat: Bu araç sadece eğitim ve yetkili test amaçlı kullanılmalıdır. Yasadışı kullanımdan doğacak sorumluluk kullanıcıya aittir.**

**🎯 AegisHack - Nesiller Ötesi Güçlü!**
