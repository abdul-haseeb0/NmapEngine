# 🔍 NmapEngine — Python-Powered Nmap Automation Engine

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Nmap-Required-green?style=for-the-badge&logo=linux&logoColor=white" />
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
</p>

> **Stop memorizing Nmap flags. Just pick a scan and fire.**

NmapEngine is a Python-powered Nmap automation engine that eliminates repetitive command-line usage by providing predefined scan profiles with a clean, menu-driven interface. Select your scan type, enter your target, and let the engine do the rest — no flags, no syntax headaches.

---

## ✨ Features

- 🎯 **Predefined Scan Profiles** — Common Nmap scans pre-configured and ready to use
- 📋 **Interactive Menu System** — Navigate scans with simple numbered selections
- 🌐 **Flexible Targeting** — Supports single IPs, subnet ranges (CIDR), and IP ranges
- ⚡ **One-Click Execution** — No manual flag entry; scans launch instantly after target input
- 🖨️ **Clean Output** — Nmap results displayed in a readable, structured format
- 🔄 **Session Loop** — Run multiple scans in one session without restarting the tool

---

## 📋 Available Scan Profiles

| # | Scan Type | Description |
|---|-----------|-------------|
| 1 | **Ping Scan** | Detect which hosts are online without port scanning (`-sn`) |
| 2 | **Host Discovery** | Identify live hosts across a network range (`-Pn`) |
| 3 | **Regular Scan** | Standard port scan across common ports (`-sS`) |
| 4 | **Quick Scan** | Fast scan of top 100 ports (`--top-ports 100`) |
| 5 | **Service & Version Detection** | Detect open services and their versions (`-sV`) |
| 6 | **OS Detection** | Attempt to identify the operating system (`-O`) |
| 7 | **Aggressive Scan** | Full fingerprinting: OS, version, scripts, traceroute (`-A`) |
| 8 | **Vulnerability Scan** | Run Nmap NSE vuln scripts (`--script vuln`) |
| 0 | **Exit** | Quit the program |

> Scan options may vary based on your version. Run the tool to see the full live menu.

---

## 🚀 Demo

```
============================================================
        NmapEngine - Nmap Automation Engine
============================================================

 [1]  Ping Scan
 [2]  Host Discovery
 [3]  Regular Scan
 [4]  Quick Scan
 [5]  Service & Version Detection
 [6]  OS Detection
 [7]  Aggressive Scan
 [8]  Vulnerability Scan
 [0]  Exit

============================================================
Select a scan type: 2

Enter target IP / subnet / range: 192.168.1.0/24

[*] Running Host Discovery on 192.168.1.0/24 ...

Starting Nmap 7.94 ...
Nmap scan report for 192.168.1.1
Host is up (0.0023s latency).
...
============================================================
Scan complete. Select another scan or [0] to exit.
```

---

## 🛠️ Requirements

- Python **3.8+**
- [Nmap](https://nmap.org/download.html) installed and available in system `PATH`
- `python-nmap` library

---

## 📦 Installation

**1. Clone the repository**
```bash
git clone https://github.com/abdul-haseeb0/NmapEngine.git
cd NmapEngine
```

**2. Install Python dependencies**
```bash
pip install -r requirements.txt
```

**3. Ensure Nmap is installed**

- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt install nmap
  ```
- **macOS:**
  ```bash
  brew install nmap
  ```
- **Windows:** Download from [nmap.org](https://nmap.org/download.html) and add to PATH

---

## ▶️ Usage

```bash
python nmapengine.py
```

> **Note:** Some scan types (e.g., OS Detection, SYN Scan) require **root/administrator privileges**.

```bash
# Linux / macOS
sudo python nmapengine.py

# Windows (run terminal as Administrator)
python nmapengine.py
```

### Supported Target Formats

| Format | Example |
|--------|---------|
| Single IP | `192.168.1.1` |
| IP Range | `192.168.1.1-50` |
| Subnet (CIDR) | `192.168.1.0/24` |
| Hostname | `example.com` |

---

## 📁 Project Structure

```
NmapEngine/
├── nmapengine.py       # Main entry point & menu engine
├── scans.py            # Predefined scan profile definitions
├── utils.py            # Helper functions (input validation, output formatting)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ⚙️ How It Works

1. The tool launches and displays the **interactive scan menu**
2. User selects a **scan number** from the menu
3. User enters a **target** (IP, range, or subnet)
4. NmapEngine constructs the appropriate `nmap` command and executes it via Python
5. Output is parsed and displayed in a clean, readable format
6. The menu loops — allowing the user to run additional scans or exit

---

## 🔒 Legal & Ethical Disclaimer

> ⚠️ **This tool is intended for authorized network testing and educational purposes only.**
> Scanning networks or systems without explicit permission from the owner is **illegal** and unethical.
> The author assumes no responsibility for any misuse of this tool.
> Always ensure you have proper authorization before scanning any network.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/new-scan-profile`
3. Commit your changes: `git commit -m 'Add new scan profile'`
4. Push to the branch: `git push origin feature/new-scan-profile`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Abdul Haseeb**
- GitHub: [@abdul-haseeb0](https://github.com/abdul-haseeb0)

---

<p align="center">
  Made with ❤️ and Python | Happy Scanning (ethically)!
</p>
