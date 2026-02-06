@echo off
setlocal EnableDelayedExpansion

:: Pruefen, ob das Skript mit Administratorrechten laeuft
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Dieses Skript muss als Administrator ausgefuehrt werden.
    echo Versuche, es mit erhoehten Rechten zu starten...
    powershell -Command "Start-Process '%~dpnx0' -Verb RunAs"
    exit /b
)

:: Aktuelles Verzeichnis setzen und dorthin wechseln
set "CURRENT_DIR=%~dp0"
echo Aktuelles Verzeichnis: !CURRENT_DIR!
cd /d "%CURRENT_DIR%"

:: PATH zunaechst bereinigen (System32/SysWOW64 temporaer entfernen)
set "PATH=!PATH:C:\Windows\System32;=!"
set "PATH=!PATH:C:\Windows\SysWOW64;=!"

:: Basis-Systempfade wieder hinzufuegen
set "PATH=C:\Windows;!PATH!"
set "PATH=C:\Windows\System32;!PATH!"
set "PATH=C:\Windows\SysWOW64;!PATH!"

:: Entwicklungstools und Plattformen
set "PATH=C:\Program Files\nodejs\;!PATH!"
set "PATH=C:\Program Files\Git\cmd;!PATH!"
set "PATH=%USERPROFILE%\.dnx\bin;!PATH!"
set "PATH=%PROGRAMFILES%\Microsoft DNX\Dnvm\;!PATH!"
set "PATH=%PROGRAMFILES%\dotnet\;!PATH!"
set "PATH=%USERPROFILE%\AppData\Roaming\npm;!PATH!"
set "PATH=%USERPROFILE%\AppData\Local\Microsoft\WindowsApps;!PATH!"
set "PATH=%USERPROFILE%\AppData\Local\GitHubDesktop\bin;!PATH!"
set "PATH=%USERPROFILE%\scoop\shims;!PATH!"
set "PATH=%USERPROFILE%\scoop\apps\git\current\cmd;!PATH!"

:: SQL Server Tools
set "PATH=C:\Program Files\Microsoft SQL Server\110\Tools\Binn\;!PATH!"
set "PATH=C:\Program Files (x86)\Microsoft SQL Server\110\Tools\Binn\;!PATH!"
set "PATH=C:\Program Files\Microsoft SQL Server\110\DTS\Binn\;!PATH!"
set "PATH=C:\Program Files (x86)\Microsoft SQL Server\110\DTS\Binn\;!PATH!"
set "PATH=C:\Program Files (x86)\Microsoft SQL Server\120\Tools\Binn\;!PATH!"
set "PATH=C:\Program Files (x6)\Microsoft SQL Server\120\DTS\Binn\;!PATH!"
set "PATH=C:\Program Files (x86)\Microsoft SQL Server\130\Tools\Binn\;!PATH!"
set "PATH=C:\Program Files (x86)\Microsoft SQL Server\130\DTS\Binn\;!PATH!"
set "PATH=C:\Program Files (x86)\Microsoft SQL Server\140\Tools\Binn\;!PATH!"
set "PATH=C:\Program Files (x86)\Microsoft SQL Server\140\DTS\Binn\;!PATH!"
set "PATH=C:\Program Files (x86)\Microsoft SQL Server\150\Tools\Binn\;!PATH!"
set "PATH=C:\Program Files (x86)\Microsoft SQL Server\150\DTS\Binn\;!PATH!"
set "PATH=%PROGRAMFILES%\Microsoft SQL Server\130\Tools\Binn\;!PATH!"
set "PATH=%PROGRAMFILES%\Microsoft SQL Server\Client SDK\ODBC\130\Tools\Binn\;!PATH!"
set "PATH=%PROGRAMFILES%\Microsoft SQL Server\140\DTS\Binn\;!PATH!"
set "PATH=%PROGRAMFILES%\Microsoft SQL Server\140\Tools\Binn\;!PATH!"
set "PATH=%PROGRAMFILES%\Microsoft SQL Server\140\Tools\Binn\ManagementStudio\;!PATH!"
set "PATH=%PROGRAMFILES(X86)%\Microsoft SQL Server\150\DTS\Binn\;!PATH!"
set "PATH=%PROGRAMFILES%\Microsoft SQL Server\150\DTS\Binn\;!PATH!"

:: Java
set "PATH=C:\Program Files\Java\jdk1.8.0_121\bin;!PATH!"
set "PATH=C:\Program Files\Java\jdk1.8.0_161\bin;!PATH!"
set "PATH=C:\Program Files\Java\jdk1.9.0_121\bin;!PATH!"

:: Weitere Tools
set "PATH=C:\Program Files\Microsoft Web Platform Installer\;!PATH!"
set "PATH=C:\Program Files (x86)\Microsoft Web Platform Installer\;!PATH!"
set "PATH=C:\Program Files\Microsoft\Windows Performance Toolkit\;!PATH!"
set "PATH=C:\Program Files (x86)\Microsoft\Windows Performance Toolkit\;!PATH!"
set "PATH=C:\Program Files\Microsoft Service Fabric\bin\Fabric\Fabric.Code;C:\Program Files\Microsoft Service Fabric\bin\Fabric\Fabric.Data;C:\Program Files\Microsoft Service Fabric\bin\Fabric\Fabric.ExeHost;!PATH!"
set "PATH=C:\Program Files (x86)\Yarn\bin\;!PATH!"
set "PATH=C:\Program Files\Microsoft VS Code\bin;!PATH!"
set "PATH=C:\Program Files\CMake\bin;!PATH!"
set "PATH=C:\Program Files\Docker\Docker\Resources\bin;!PATH!"
set "PATH=C:\ProgramData\chocolatey\bin;!PATH!"
set "PATH=C:\Program Files (x86)\Heroku\bin;!PATH!"
set "PATH=C:\Program Files\Amazon\AWSCLI\bin\;!PATH!"
set "PATH=C:\Program Files (x86)\Amazon\AWSCLI\bin\;!PATH!"
set "PATH=C:\Ruby23-x64\bin;!PATH!"
set "PATH=C:\Strawberry\c\bin;!PATH!"
set "PATH=C:\Strawberry\perl\site\bin;!PATH!"
set "PATH=C:\Strawberry\perl\bin;!PATH!"

:: FFmpeg
set "PATH=C:\ffmpeg\bin;!PATH!"

echo.
echo Administrator-Rechte bestaetigt.
echo Aktuelles Verzeichnis: %CD%
echo Aktualisierter PATH:
echo !PATH!
echo.

:: Eingabeaufforderung mit dieser Umgebung im aktuellen Ordner oeffnen
cmd /k
