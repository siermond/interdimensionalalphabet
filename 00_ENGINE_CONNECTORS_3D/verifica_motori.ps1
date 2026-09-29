$endpoints = @(
  @{ Name='NEXUS COMMAND DAEMON'; Host='127.0.0.1'; Port=8090; Type='HTTP/WS' },
  @{ Name='BLENDER NEXUS BRIDGE'; Host='127.0.0.1'; Port=9001; Type='TCP Socket' },
  @{ Name='UNITY PRAY SPHERE';    Host='127.0.0.1'; Port=9002; Type='TCP Socket' },
  @{ Name='UNREAL REMOTE CONTROL';Host='127.0.0.1'; Port=30010; Type='HTTP REST' },
  @{ Name='ELEVEN HASHEM TREASURY';Host='127.0.0.1'; Port=8000; Type='HTTP API' },
  @{ Name='OLLAMA LOCAL BRAIN';   Host='127.0.0.1'; Port=11434; Type='HTTP' }
)

Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "  INTERDIMENSIONAL ALPHABET -- VERIFICA MATRICE MOTORI 3D" -ForegroundColor Yellow
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""

foreach ($ep in $endpoints) {
  try {
    $client = New-Object System.Net.Sockets.TcpClient
    $async = $client.BeginConnect($ep.Host, $ep.Port, $null, $null)
    $success = $async.AsyncWaitHandle.WaitOne(800, $false)
    if ($success -and $client.Connected) {
      Write-Host ("  [ONLINE]  " + $ep.Name.PadRight(24) + " (Porta " + $ep.Port + " - " + $ep.Type + ")") -ForegroundColor Green
      $client.EndConnect($async)
      $client.Close()
    } else {
      Write-Host ("  [STANDBY] " + $ep.Name.PadRight(24) + " (Porta " + $ep.Port + " - " + $ep.Type + ")") -ForegroundColor DarkYellow
      $client.Close()
    }
  } catch {
    Write-Host ("  [STANDBY] " + $ep.Name.PadRight(24) + " (Porta " + $ep.Port + " - " + $ep.Type + ")") -ForegroundColor DarkYellow
  }
}

Write-Host ""
Write-Host "Cartella Madre Connettori: C:\Users\autor\Desktop\INTERDIMENSIONAL ALPHABET\00_ENGINE_CONNECTORS_3D" -ForegroundColor Cyan
Write-Host ""
