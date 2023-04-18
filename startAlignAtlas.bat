::Batchfile to start AlignAtlas.py
::Also checks for dependant packages each time
::ASSUMES pip is installed
::ASSUMES the DEFAULT execution alias of "python3" is setup in windows.
@echo off
cls
echo Beginning.
echo.

::  ==== Check for Python Installation ==== 
echo Checking Python version.
python --version | find "Python 3" >NUL 2>NUL

:: if Python 3 not found, it's a bad python version
if errorlevel 1 goto errorBadPython


:: ==== Launch python script ==== 
:launch
echo Launching AlignAtlas.
echo.
echo.
python3 AlignAtlas.py
goto end


::Error msg if python is outdated or not installed
:errorBadPython
echo.
echo.
echo Error^: ERROR: Python is not version 3 or is not installed.
goto end


:: ==== End of Script ==== 
:end
echo.
echo.
echo Press any button to close this window...
:: Pause for user input
pause > nul