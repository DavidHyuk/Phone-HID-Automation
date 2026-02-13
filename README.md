# 🚀 XIAO RP2040 Based Android Setup Automation Project

This project uses the **Seeed Studio XIAO RP2040** board to create an HID (Human Interface Device) automation tool that automatically performs 'Developer Mode Activation', 'Disabling Auto Blocker', and 'Enabling USB Debugging' on Android devices.

---

## 🛠 1. Hardware Specifications and Preparation
### 📍 Board Configuration
* **Board:** Seeed Studio XIAO RP2040
* **B (BOOT) Button:** Force enter bootloader mode (press and hold while connecting)
* **R (RESET) Button:** Software reset (double-tap quickly to enter bootloader)

### 📍 Initial Environment Setup
1.  **Install CircuitPython:** While holding the `B` button, connect to PC and drop the `.uf2` file into the `RPI-RP2` drive.
2.  **Libraries:** You must copy the `adafruit_hid` library folder into the `CIRCUITPY/lib/` directory.

---

## ⚡ 2. Main Shortcuts and Control Guide (Android HID)
Standard shortcuts used when a physical keyboard is connected to an Android device.

| Function | Shortcut (Keycode) | Notes |
| :--- | :--- | :--- |
| **Open Settings** | `Win + I` | Most reliable way to enter settings |
| **Go to Home Screen** | `Win (GUI)` | Escape to home screen from any screen |
| **Go Back (Back)** | `Win + Left Arrow` or `ESC` | Return to previous screen |
| **Invoke Search** | `Ctrl + F` | Immediately activate search bar within settings |
| **Toggle Switch Control** | `Space` | On/Off when focus is on the switch |
| **Select Item** | `Enter` | Enter menu or click button |

---

## 🔧 3. Troubleshooting - Essential Reading

> **⚠️ The Most Important "10-Second Rule"**
> Always include `time.sleep(10)` at the top of your `code.py`. If automation runs as soon as you plug the board in, you will lose the chance to modify or delete the code on your PC.

### ❓ `CIRCUITPY` Drive is Not Visible (Storage Hidden)
This happens if you've hidden the drive via `boot.py` or the file system is corrupted.
1.  **Force Mount:** Unplug the board, hold the `B` button, and reconnect to show `RPI-RP2`, then re-flash the `.uf2` file.
2.  **Flash Nuke:** If the above fails, use `flash_nuke.uf2` to completely wipe the NAND flash before reinstalling.

### ❓ Key Inputs are Missed or Menu Positions are Misaligned
1.  **Adjust Delay:** If key inputs are faster than Android animation speeds, they will be lost. Increase the `delay` in the `send()` function to `0.15`–`0.2` seconds.
2.  **Loss of Focus:** If the toggle switch doesn't trigger, press `Tab` one more time before hitting `Space` to ensure the blue border focus is on the 'switch button' itself, not just the 'entire item'.
3.  **Language Input:** If the phone's input method is set to a non-English language (e.g., Korean), `Settings` might be typed as garbled text. Force switch to English in the code (e.g., `Shift + Space`) or set the phone's system language to English.

### ❓ Interrupting Infinite Loops on MacBook
If the board starts typing uncontrollably on your MacBook:
1.  Run Terminal: `screen /dev/tty.usbmodem* 115200`
2.  Immediately hit `Ctrl + C` repeatedly to stop Python execution (wait for the `>>>` prompt).
3.  Use the command `os.remove('boot.py')` to disable stealth mode.

---

## 🚀 4. Operation and Deployment

### 📂 Efficient File Management
* **code.py:** The main script containing the actual automation logic.
* **boot.py:** Used to hide the board from being recognized as a 'Storage Device' when connected to a smartphone (use only after final completion).

### ⌨️ MacBook Auto-Copy Script (`copy_code.sh`)
```bash
#!/bin/bash
# Needs chmod +x copy_code.sh permission
cp code.py /Volumes/CIRCUITPY/ && sleep 1 && diskutil eject /Volumes/CIRCUITPY
```
