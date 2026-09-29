@echo off
chcp 65001 >nul 2>&1
title TEST CONNESSIONE UNITY (PORTA 9002)
color 0B

echo ================================================================
echo   TEST CONNESSIONE UNITY NEXUS BRIDGE (127.0.0.1:9002)
echo ================================================================
echo.

powershell -NoProfile -Command ^
  "try { ^
     $client = New-Object System.Net.Sockets.TcpClient('127.0.0.1', 9002); ^
     Write-Host '[OK] Unity Nexus Bridge RISPONDE su porta 9002!' -ForegroundColor Green; ^
     $stream = $client.GetStream(); ^
     $msg = [System.Text.Encoding]::UTF8.GetBytes('{\"action\":\"PING_UNITY\"}'); ^
     $stream.Write($msg, 0, $msg.Length); ^
     $client.Close(); ^
   } catch { ^
     Write-Host '[INFO] Porta 9002 non attiva. Assicurati che Unity sia aperto con il componente UnityNexusBridge attivo.' -ForegroundColor Yellow; ^
   }"

echo.
pause
