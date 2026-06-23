# 🎬 Crunchyroll Account Checker & Validator (GUI)

A powerful, user-friendly, and multi-threaded **Crunchyroll Account Checker** written in Python. Safely manage, validate, and organize your premium accounts without losing track of your login credentials. 

  <img width="1536" height="1024" alt="ChatGPT Image 23  Juni 2026, 20_47_21" src="https://github.com/user-attachments/assets/b4811f5a-35c3-4fd9-acdf-c926595cf160" />

---

## 🚀 Features

* **User-Friendly GUI:** Sleek and simple Graphical User Interface built with Python.
* **Flexible Proxy Management:** * Use your own custom proxies.
    * Run proxy-less (No proxies).
    * **Auto-Fetch Proxies:** Automatically scrape and export ~2,000 fresh proxies directly from *ProxyScrape*.
* **Discord Webhook Integration:** Receive real-time validation results directly on your Discord server so you can access your working accounts on your phone.
* **Advanced Error Handling (Round System):** Failed checks or network errors are automatically collected and re-tested in a subsequent "Round" to ensure 100% accurate results.
* **High Performance:** Multi-threaded architecture for lightning-fast validation.

---

## 🛠️ How to Use

### Method 1: The Easy Way (Recommended)
1. Download the repository as a ZIP file and extract it.
2. Double-click and open the **`start.bat`** file.
3. The script will automatically install all required dependencies via `pip` and launch the main application.

### Method 2: Manual / Secure Execution
If your operating system or antivirus flags the `.bat` file and you prefer to run it manually, follow these steps:
1. Open the project folder.
2. Click on the address bar at the top of your file explorer, type **`cmd`**, and press `Enter`.
3. Navigate to the distribution folder by typing:
   ```bash
   cd dist 

 

   python check.py
