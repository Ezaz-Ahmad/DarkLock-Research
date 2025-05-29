# DarkLock-Research
A proof-of-concept ransomware simulation developed to demonstrate advanced skills in cybersecurity, malware analysis, and system programming. This project is strictly for educational and research purposes to deepen understanding of threat mechanisms and offensive security techniques.

## Overview
DarkLock-Research simulates ransomware behavior to showcase expertise in Python programming, encryption techniques, system persistence, and network propagation. It serves as a portfolio piece for cybersecurity roles focused on threat hunting, penetration testing, and malware reverse engineering. The project highlights the importance of understanding attack vectors to build better defenses.

## Features
- **File Encryption Simulation**: Simulates file encryption by renaming files with a `.locked` extension or uses Fernet symmetric encryption if the `cryptography` library is available.
- **System Persistence**: Adds the script to Windows startup via registry modifications to ensure execution on boot.
- **GUI Ransom Note**: Displays a persistent pop-up window using `tkinter` demanding a ransom with an unlock code input.
- **Network Propagation**: Scans local network for vulnerable devices on common ports (e.g., SMB 445) and simulates propagation.
- **Multi-Threading**: Executes encryption, sound alerts, and network scanning concurrently for increased impact.
- **Fallback Mechanisms**: Adapts to different environments with directory fallbacks and console mode if GUI libraries are unavailable.

## Technical Details
- **Language**: Python 3.x
- **Libraries Used**: `tkinter` (GUI), `cryptography` (encryption), `winreg` (persistence), `winsound` (alerts), `socket` (network scanning)
- **Target OS**: Primarily Windows, with partial support for other platforms
- **Key Components**:
  - Encryption thread for file locking
  - Registry manipulation for persistence
  - Network scanning for propagation
  - GUI-based user intimidation

## Installation & Setup
1. Clone the repository:
   ```
   git clone https://github.com/Ezaz-Ahmad/DarkLock-Research.git
   ```
2. Navigate to the project directory:
   ```
   cd DarkLock-Research
   ```
3. Install required dependencies (if using encryption):
   ```
   pip install cryptography
   ```
4. Run the script (for testing in a controlled, virtual environment):
   ```
   python ransomware_persistent.py
   ```

## Usage
- Execute the script in a safe, isolated environment (e.g., a virtual machine) to observe its behavior.
- Enter the hardcoded unlock code `2020745` to stop the simulation.
- Review the code and logs to understand the implemented attack techniques.

## Disclaimer
This project is a simulation created for educational and research purposes only. It is intended to demonstrate technical skills in cybersecurity and should not be used in any unauthorized or harmful manner. Always test in a controlled, ethical environment.

## Purpose for Cybersecurity
DarkLock-Research reflects my ability to understand and simulate complex malware behavior, a critical skill for offensive security and threat analysis. By building this POC, I’ve gained insights into encryption, persistence, and propagation techniques, which are essential for developing robust defensive strategies.
