# 디버깅

상위 노트: [android-storage-systems](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems.md)

```bash
# 앱 저장소 확인
adb shell ls -la /data/data/com.example.app/

# 파일 내용 보기
adb shell cat /data/data/com.example.app/files/myfile.txt

# 파일 복사 (기기 → PC)
adb pull /data/data/com.example.app/files/myfile.txt

# 파일 복사 (PC → 기기)
adb push myfile.txt /data/data/com.example.app/files/

# 저장소 사용량
adb shell dumpsys diskstats

# MediaStore 확인
adb shell content query --uri content://media/external/images/media
```
