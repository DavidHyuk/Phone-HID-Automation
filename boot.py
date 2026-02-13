import storage
import usb_hid

# 1. USB 드라이브 기능을 완전히 끕니다. (폰이 메모리로 인식 못 하게 함)
storage.disable_usb_drive()

# 2. USB 키보드(HID) 기능만 명시적으로 켭니다.
usb_hid.enable((usb_hid.Device.KEYBOARD,))

print("Storage disabled, HID enabled.")