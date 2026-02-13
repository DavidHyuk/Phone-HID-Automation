#!/bin/bash

# 1. CIRCUITPY 드라이브 존재 여부 확인
if [ -d "/Volumes/CIRCUITPY" ]; then
    echo "🚀 Copying code.py to CIRCUITPY..."
    cp code.py /Volumes/CIRCUITPY/
    
    # 잠시 대기 (파일 쓰기 완료 보장)
    sleep 1
    
    # 2. 안전하게 추출
    echo "✅ Copy complete. Ejecting..."
    diskutil eject /Volumes/CIRCUITPY
    echo "🎉 Now you can unplug the board."
else
    echo "❌ Error: /Volumes/CIRCUITPY not found. Check the connection or boot mode."
fi