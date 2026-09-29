@echo off
chcp 65001 >nul 2>&1
title NOMAD SCULPT -> INTERDIMENSIONAL ALPHABET / MIRROR MOUNTAIN
color 0B

echo ================================================================
echo   NOMAD SCULPT INBOX -- INGESTIONE SCULTURA IN MIRROR MOUNTAIN
echo ================================================================
echo.

set "INBOX=C:\Users\autor\Desktop\NOMAD_INBOX"
set "ASHIA_DIR=C:\Users\autor\Desktop\INTERDIMENSIONAL ALPHABET\01_ASHIA"
set "DEST_GLB=%ASHIA_DIR%\ashia.glb"

:: Cerca file .glb in NOMAD_INBOX
set "TROVATO="
for %%F in ("%INBOX%\*.glb") do (
    set "TROVATO=%%F"
    goto :processa
)

:non_trovato
echo [INFO] Nessun file .glb trovato in NOMAD_INBOX.
echo.
echo Come procedere:
echo   1. Esporta la tua scultura da Nomad Sculpt in formato .glb
echo   2. Salvala o incollala dentro:
echo      C:\Users\autor\Desktop\NOMAD_INBOX\
echo      (oppure direttamente in C:\Users\autor\Desktop\INTERDIMENSIONAL ALPHABET\01_ASHIA\ashia.glb)
echo   3. Riesegui questo script per la validazione automatica.
echo.
pause
exit /b 0

:processa
echo [1/3] File rilevato: "%TROVATO%"
echo [2/3] Trasferimento in Interdimensional Alphabet (01_ASHIA)...
copy /y "%TROVATO%" "%DEST_GLB%" >nul
if errorlevel 1 (
    echo [ERRORE] Impossibile copiare il file in 01_ASHIA.
    pause
    exit /b 1
)

echo [OK] Scultura posizionata in: %DEST_GLB%

echo.
echo [3/3] Verifica Intestazione glTF (Header Check)...
powershell -NoProfile -Command ^
  "$b = [System.IO.File]::ReadAllBytes('%DEST_GLB%'); ^
   if ($b.Length -ge 12 -and $b[0] -eq 0x67 -and $b[1] -eq 0x6C -and $b[2] -eq 0x54 -and $b[3] -eq 0x46) { ^
     $v = [System.BitConverter]::ToUInt32($b, 4); ^
     if ($v -eq 2) { ^
       Write-Host '[CONFORME] Magic glTF e Versione validi: glTF 2.0 Binary (.glb).' -ForegroundColor Green; ^
       $mb = [math]::Round($b.Length / 1MB, 2); ^
       Write-Host ('Dimensione scultura: ' + $mb + ' MB (' + $b.Length + ' byte)') -ForegroundColor Cyan; ^
     } else { ^
       Write-Host ('[AVVISO] Versione glTF: ' + $v + ' (Atteso standard glTF 2.0).') -ForegroundColor Yellow; ^
     } ^
   } else { ^
     Write-Host '[ATTENZIONE] Il file non presenta la firma glTF binaria.' -ForegroundColor Yellow; ^
   }"

echo.
echo ================================================================
echo   STATO SORGENTE PRONTO IN MIRROR MOUNTAIN:
echo   - Categoria Tecnica: 01_ASHIA [ TASTO GLB #01 ]
echo   - Scultura 3D: INTERDIMENSIONAL ALPHABET\01_ASHIA\ashia.glb
echo   - Esperienza Rituale: Divine Light Pray --^> ORDER POEM
echo   - Sequenza VR: Croce Dorata dal Cielo --^> Luce --^> Servant + Kybalion
echo   - Economia Interna: Attivazione $ANGELIC (risorsa interna)
echo   - Canale Esterno: Separato (Timeless Memory / OpenSea / ETH)
echo ================================================================
echo.
echo Ora puoi aprire INTERDIMENSIONAL ALPHABET oppure il Voice Cockpit!
pause
