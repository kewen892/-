@echo off
chcp 65001 >nul
cls
echo ==============================================
echo    漫剧AI自动化工具 全套服务启动器
echo ==============================================
echo    Web前端      ： http://localhost:8066
echo    文本大模型    ： http://localhost:8067
echo    AI绘图       ： http://localhost:8068
echo ==============================================
echo.
echo 全部服务启动中...请勿关闭本窗口
echo.

:: 启动前端网页（绝对路径）
start cmd /k "cd /d C:\Users\Kewen-pc\manju-Tool\web && python -m http.server 8066"

:: 启动 2. 文本大模型API 8067
start "文本大模型服务(8067)" cmd /k "cd /d ai-api && python main.py"

:: 启动 3. AI绘图服务 8068
start "AI绘图服务(8068)" cmd /k "cd /d ai-image && python image_server.py"

echo 正在打开浏览器...
start http://localhost:8066

echo.
echo 启动完成！
pause