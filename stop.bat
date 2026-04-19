@echo off
chcp 65001
taskkill /f /im python.exe
taskkill /f /im cmd.exe
echo 所有AI服务已全部关闭
pause