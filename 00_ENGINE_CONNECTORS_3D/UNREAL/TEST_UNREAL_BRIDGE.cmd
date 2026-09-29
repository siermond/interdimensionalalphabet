@echo off
chcp 65001 >nul 2>&1
title TEST CONNESSIONE UNREAL ENGINE (PORTA 30010)
color 0D

echo ================================================================
echo   TEST CONNESSIONE UNREAL REMOTE CONTROL (127.0.0.1:30010)
echo ================================================================
echo.

powershell -NoProfile -Command ^
  "try { ^
     $req = [System.Net.WebRequest]::Create('http://127.0.0.1:30010/remote/info'); ^
     $req.Timeout = 2000; ^
     $resp = $req.GetResponse(); ^
     Write-Host '[OK] Unreal Remote Control Server RISPONDE su porta 30010!' -ForegroundColor Green; ^
     $resp.Close(); ^
   } catch { ^
     Write-Host '[INFO] Unreal Remote Control (30010) in standby.' -ForegroundColor Yellow; ^
     Write-Host 'Per attivarlo in Unreal: Edit -> Project Settings -> Plugins -> Remote Control Web Server -> Enable.' -ForegroundColor Gray; ^
   }"

echo.
pause
