import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# 1. 초기화 및 안전 대기 (맥북 수정용 골든타임)
print("Safety delay 5s...")
time.sleep(5)

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

def send(key, times=1, delay=0.1):
    """지정한 키를 횟수만큼 누르는 함수"""
    for _ in range(times):
        kbd.send(key)
        time.sleep(delay)

def slow_write(text, delay=0.1):
    """글자를 하나씩 천천히 입력하는 함수"""
    for char in text:
        layout.write(char)
        time.sleep(delay)

def back_home(times=1):
    """안드로이드 뒤로 가기 (Win + Left Arrow)"""
    for _ in range(times):
        kbd.press(Keycode.GUI, Keycode.LEFT_ARROW)
        time.sleep(0.1)
        kbd.release_all()
        time.sleep(0.5)

def run_automation():
    print("Full Automation Sequence Starting...")

    # [1단계] 설정창 진입 및 'build number' 검색
    # Win + I로 세팅화면 진입
    kbd.send(Keycode.GUI, Keycode.I)
    time.sleep(2.0)

    # Ctrl + F로 검색화면에 포커스 -> 1초 대기
    kbd.send(Keycode.CONTROL, Keycode.F)
    time.sleep(1.0)

    # build number 키보드 입력 후 1초 대기
    slow_write("build number", 0.1)
    time.sleep(1.0)

    # tab 3번 0.2초 간격으로 누름 -> 엔터
    send(Keycode.TAB, 3, 0.2)
    send(Keycode.ENTER, 1, 1.0)

    # 키보드 아래 방향으로 5번 0.5초 간격으로 내려옴
    send(Keycode.DOWN_ARROW, 5, 0.5)

    # 엔터 7번 연타 (0.5초 간격) - 개발자 모드 활성화
    send(Keycode.ENTER, 7, 0.5)

    # 오른쪽 화살표 2번 눌러 OK에 포커스 맞추고 엔터
    send(Keycode.RIGHT_ARROW, 2, 0.2)
    send(Keycode.ENTER, 1, 1.0)

    # [2단계] Auto Blocker 설정
    # win + 왼쪽 화살표로 이전 화면 진입 (2번)
    back_home(2)
    time.sleep(1.0)

    # ctrl + F로 Auto Blocker 검색
    kbd.send(Keycode.CONTROL, Keycode.F)
    time.sleep(1.0)
    slow_write("Auto Blocker", 0.1)
    time.sleep(1.0)

    # tab 3번 누른 뒤 엔터
    send(Keycode.TAB, 3, 0.5)
    send(Keycode.ENTER, 1, 1.0)

    # 아래 방향으로 화살표 6번 누르고 엔터 (여유롭게 내려가기)
    send(Keycode.DOWN_ARROW, 6, 0.5)
    time.sleep(1.5)
    send(Keycode.ENTER, 1, 1.0)

    # 탭 한번 누르고 스페이스
    send(Keycode.TAB, 1, 0.5)
    time.sleep(2.0)
    send(Keycode.SPACE, 1, 0.5)

    # 오른쪽 방향 두번 누르고 엔터
    send(Keycode.RIGHT_ARROW, 2, 0.2)
    send(Keycode.ENTER, 1, 2.0)

    # [3단계] USB Debugging 설정
    # Win 키 눌러서 바탕화면으로 나감
    kbd.send(Keycode.GUI)
    time.sleep(1.0)

    # Ctrl + F로 검색창 열기 (글로벌 검색)
    kbd.send(Keycode.CONTROL, Keycode.F)
    time.sleep(1.0)

    # USB debugging 입력
    slow_write("USB debugging", 0.15)
    time.sleep(1.0)

    # Tab 6번 누른 후 엔터 (검색 결과에서 선택)
    send(Keycode.TAB, 6, 0.3)
    send(Keycode.ENTER, 1, 2.0)

    # 아래 방향 화살표 9번 누름 (매우 여유롭게 내려가기) -> Space
    send(Keycode.TAB, 9, 0.5)
    time.sleep(1.0)
    send(Keycode.SPACE, 1, 0.5)

    # 오른쪽 화살표 2번 -> 엔터
    send(Keycode.RIGHT_ARROW, 2, 0.5)
    send(Keycode.ENTER, 1, 1.0)

    print("All tasks completed successfully!")

# 실행 시작
try:
    run_automation()
except Exception as e:
    print(f"Error: {e}")
