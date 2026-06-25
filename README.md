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

## Available Scan Profiles

| # | Scan Profile            | Description                                                                                            |
| - | ----------------------- | ------------------------------------------------------------------------------------------------------ |
| 1 | **Ping Scan**           | Discover live hosts without performing a port scan (`-sn`)                                             |
| 2 | **Fast Scan**           | Quickly scan the most common ports on the target (`-F`)                                                |
| 3 | **SYN Stealth Scan**    | Perform a stealthy TCP SYN scan to identify open ports (`-sS`)                                         |
| 4 | **Service Detection**   | Identify running services and their versions (`-sV`)                                                   |
| 5 | **OS Detection**        | Attempt to determine the target operating system (`-O`)                                                |
| 6 | **UDP Scan**            | Scan UDP ports and discover UDP-based services (`-sU`)                                                 |
| 7 | **Aggressive Scan**     | Comprehensive scan including OS detection, version detection, NSE scripts, and traceroute (`-A`)       |
| 8 | **Vulnerability Scan**  | Execute Nmap NSE vulnerability scripts against the target (`--script vuln`)                            |
| 9 | **Web Technology Scan** | Enumerate web technologies, HTTP headers, page titles, and common web resources using NSE HTTP scripts |
| 0 | **Exit**                | Exit the application                                                                                   |


> Scan options may vary based on your version. Run the tool to see the full live menu.

---

## 🚀 Demo

```
███████╗███╗   ███╗ █████╗ ██████╗    ███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
████╗  ██║████╗ ████║██╔══██╗██╔══██╗   ██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝
██╔██╗ ██║██╔████╔██║███████║██████╔╝   █████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝    ██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║        ███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝        ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝

                           Network Intelligence Suite


AVAILABLE SCANNING MODULES
------------------------------------------------------------

[1] Ping Scan               |  [2] Service Detection
[3] OS Detection            |  [4] Vulnerability Scan
[5] Aggressive Scan         |  [6] SYN Stealth Scan
[7] Web Tech Scan           |  [8] UDP Port Scan
[9] Fast Triage Scan        |

------------------------------------------------------------

[10] Exit Framework

------------------------------------------------------------

nmap-engine > Select a module [1-10]: 2

Target > scanme.nmap.org

[*] Starting Service Detection Scan...
[*] Command: nmap -sV scanme.nmap.org

PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH
80/tcp    open  http    Apache httpd

Service Info:
- SSH detected on port 22
- HTTP detected on port 80

[✓] Scan completed successfully.

nmap-engine > Press ENTER to return to menu...
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
│
├── main.py                    # Application entry point
├── LICENSE
├── README.md
│
├── core/
│   ├── __init__.py
│   └── base_scanner.py        # Base scanner class & shared logic
│
├── scans/
│   ├── __init__.py
│   ├── aggressive_scan.py     # Aggressive scan (-A)
│   ├── fast_scan.py           # Fast scan (-F)
│   ├── os_detection.py        # OS detection (-O)
│   ├── ping_scan.py           # Host discovery
│   ├── service_detection.py   # Service/version detection (-sV)
│   ├── syn_stealth_scan.py    # SYN stealth scan (-sS)
│   ├── udp_scan.py            # UDP scan (-sU)
│   ├── vuln_scanner.py        # NSE vulnerability scans
│   └── web_tech_scan.py       # Web enumeration & HTTP NSE scripts
│
└── utils/
    ├── __init__.py
    └── ui.py                  # Banner, colors, menus, output formatting
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
