# 🔍 ReconSpect

**ReconSpect** is a lightweight, Zphisher-inspired interactive CLI tool built with Python for automated reconnaissance and OSINT (Open Source Intelligence) gathering. Designed primarily for Kali Linux and Linux-based security environments.

---

### 🚀 Features
- Interactive CLI Menu with cyber-style banners and color-coded logs.
- IP Geolocation and ISP information lookup.
- Subdomain and DNS reconnaissance via public security logs.
- Fast, dependency-light, and easy to use.

---

### 📦 Installation & Setup

Clone the repository and run the setup commands based on your operating system:

#### 1. Kali Linux / Ubuntu / Debian / WSL
```bash
sudo apt update && sudo apt install git python3 python3-pip -y
git clone https://github.com/tajim879/ReconSpect.git
cd ReconSpect
pip3 install -r requirements.txt --break-system-packages
python3 recon.py
