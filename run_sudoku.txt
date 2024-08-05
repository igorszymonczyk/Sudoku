@echo off
:menu
cls
echo Wybierz opcje:
echo 1. Uruchom program Python
echo 2. Generuj raport
echo 3. Stworz backup
echo 4. Wyjdz
echo.
set /p choice="Wprowadz numer opcji i nacisnij Enter: "

if "%choice%"=="1" goto runPython
if "%choice%"=="2" goto generateReport
if "%choice%"=="3" goto createBackup
if "%choice%"=="4" goto exit

echo Nieprawidlowy wybor
pause
goto menu

:runPython
python "C:\Users\Szymo\Desktop\studia\semestr 3\jezyki skryptowe\Projekt\Sudoku.py"
goto menu

:generateReport
python "C:\Users\Szymo\Desktop\studia\semestr 3\jezyki skryptowe\Projekt\raport.py"
goto menu

:createBackup
copy "C:\Users\Szymo\Desktop\studia\semestr 3\jezyki skryptowe\Projekt\Sudoku.py" "C:\Users\Szymo\Desktop\studia\semestr 3\jezyki skryptowe\Projekt\backup_sudoku.py"
echo Backup wykonany
pause
goto menu

:exit
exit