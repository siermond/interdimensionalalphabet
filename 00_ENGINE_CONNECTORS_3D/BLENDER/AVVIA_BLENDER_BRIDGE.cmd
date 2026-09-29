@echo off
chcp 65001 >nul 2>&1
title BLENDER NEXUS BRIDGE (PORT 9001)
color 0E

echo ================================================================
echo   BLENDER NEXUS BRIDGE -- CONNETTORE MIRROR MOUNTAIN
echo ================================================================
echo.

set "SCRIPT=%~dp0blender_nexus_sync.py"

:: Cerca eseguibile blender
where blender >nul 2>&1
if not errorlevel 1 (
    echo [OK] Blender trovato nel PATH di sistema.
    blender --python "%SCRIPT%"
    goto :fine
)

if exist "C:\Program Files\Blender Foundation\Blender 4.2\blender.exe" (
    echo [OK] Trovato Blender 4.2 in Program Files.
    "C:\Program Files\Blender Foundation\Blender 4.2\blender.exe" --python "%SCRIPT%"
    goto :fine
)

if exist "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" (
    echo [OK] Trovato Blender 4.1 in Program Files.
    "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" --python "%SCRIPT%"
    goto :fine
)

if exist "C:\Program Files\Blender Foundation\Blender 4.0\blender.exe" (
    echo [OK] Trovato Blender 4.0 in Program Files.
    "C:\Program Files\Blender Foundation\Blender 4.0\blender.exe" --python "%SCRIPT%"
    goto :fine
)

echo [INFO] Blender non trovato nei percorsi standard.
echo Puoi avviare Blender normalmente e trascinare lo script:
echo   "%SCRIPT%"
echo nella Text Editor di Blender e premere 'Run Script'.
echo.
pause

:fine
