@echo off
echo begin running
if exist .\zipaligned (
	rd /s /q .\zipaligned
)
md .\zipaligned

E:\softWhare\android_studio_sdk\build-tools\25.0.0\zipalign -v 4  .\%1.apk .\zipaligned\%1.apk

echo end running