@echo off
cd /d %~dp0

echo ====================================
echo   Iniciando IA Web...
echo ====================================

call venv\Scripts\activate

start http://127.0.0.1:8000

python manage.py runserver

pause