using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using UnityEngine;

/// <summary>
/// UNITY NEXUS BRIDGE — MIRROR MOUNTAIN & INTERDIMENSIONAL ALPHABET
/// Ascolta su Porta 9002 TCP ordini da Nexus Command e carica GLB da 01_ASHIA.
/// </summary>
public class UnityNexusBridge : MonoBehaviour
{
    [Header("Configurazione Nexus")]
    public int port = 9002;
    public string alphabetDir = @"C:\Users\autor\Desktop\INTERDIMENSIONAL ALPHABET";
    public string defaultCategory = "01_ASHIA";
    public string defaultGlbName = "ashia.glb";

    [Header("Riferimenti Scena VR")]
    public Transform goldenCrossAnchor;
    public Light cosmicBeamLight;
    public GameObject servantOfHumanityAvatar;
    public GameObject kybalionBook;

    private TcpListener server;
    private Thread listenerThread;
    private bool isRunning = false;
    private string pendingCommand = null;

    void Start()
    {
        StartServer();
    }

    void StartServer()
    {
        try
        {
            server = new TcpListener(IPAddress.Loopback, port);
            server.Start();
            isRunning = true;
            listenerThread = new Thread(ListenLoop);
            listenerThread.IsBackground = true;
            listenerThread.Start();
            Debug.Log($"[UNITY NEXUS] In ascolto su 127.0.0.1:{port}");
        }
        catch (Exception ex)
        {
            Debug.LogError($"[UNITY NEXUS ERROR] {ex.Message}");
        }
    }

    void ListenLoop()
    {
        while (isRunning)
        {
            try
            {
                using (TcpClient client = server.AcceptTcpClient())
                using (NetworkStream stream = client.GetStream())
                {
                    byte[] buffer = new byte[4096];
                    int bytesRead = stream.Read(buffer, 0, buffer.Length);
                    if (bytesRead > 0)
                    {
                        string json = Encoding.UTF8.GetString(buffer, 0, bytesRead);
                        lock (this)
                        {
                            pendingCommand = json;
                        }
                        byte[] response = Encoding.UTF8.GetBytes("{\"status\":\"OK\",\"engine\":\"UNITY\"}");
                        stream.Write(response, 0, response.Length);
                    }
                }
            }
            catch (SocketException) { break; }
            catch (Exception ex)
            {
                Debug.LogWarning($"[UNITY NEXUS] Warning: {ex.Message}");
            }
        }
    }

    void Update()
    {
        string cmdToExecute = null;
        lock (this)
        {
            if (pendingCommand != null)
            {
                cmdToExecute = pendingCommand;
                pendingCommand = null;
            }
        }

        if (!string.IsNullOrEmpty(cmdToExecute))
        {
            ExecuteCommand(cmdToExecute);
        }
    }

    void ExecuteCommand(string json)
    {
        Debug.Log($"[UNITY NEXUS ORDER] {json}");

        if (json.Contains("TRIGGER_ORDER_POEM_KYBALION_RITUAL") || json.Contains("ORDER_POEM"))
        {
            TriggerOrderPoemSequence();
        }
        else if (json.Contains("BUILD_360_PRAY_SPHERE"))
        {
            SetupPraySphere360();
        }
        else if (json.Contains("LOAD_ASHIA"))
        {
            LoadAshiaGlb();
        }
    }

    public void TriggerOrderPoemSequence()
    {
        Debug.Log("[UNITY] Avvio Sequenza Rituale: Order Poem -> First Cross -> Servant of Humanity");
        
        // 1. Oscurità VR
        RenderSettings.ambientIntensity = 0.05f;

        // 2. Discesa Croce Dorata
        if (goldenCrossAnchor != null)
        {
            goldenCrossAnchor.gameObject.SetActive(true);
            goldenCrossAnchor.position = new Vector3(0, 5.0f, 3.0f);
        }

        // 3. Fascio di Luce Cosmica
        if (cosmicBeamLight != null)
        {
            cosmicBeamLight.enabled = true;
            cosmicBeamLight.intensity = 4.0f;
            cosmicBeamLight.color = new Color(1.0f, 0.85f, 0.4f);
        }

        // 4. Manifestazione Servant of Humanity + Kybalion
        if (servantOfHumanityAvatar != null)
        {
            servantOfHumanityAvatar.SetActive(true);
        }
        if (kybalionBook != null)
        {
            kybalionBook.SetActive(true);
        }
    }

    public void SetupPraySphere360()
    {
        Debug.Log("[UNITY] Configurazione Sfera 360° di Preghiera Immersiva (528 Hz)");
        RenderSettings.ambientLight = new Color(0.1f, 0.4f, 0.6f);
    }

    public void LoadAshiaGlb()
    {
        string fullPath = Path.Combine(alphabetDir, defaultCategory, defaultGlbName);
        if (File.Exists(fullPath))
        {
            Debug.Log($"[UNITY] File GLB trovato in {fullPath}. Procedo con istanziazione.");
            // Utilizzare glTFast o UnityGLTF per il caricamento runtime
        }
        else
        {
            Debug.LogWarning($"[UNITY] File non trovato: {fullPath}");
        }
    }

    void OnDestroy()
    {
        isRunning = false;
        if (server != null) server.Stop();
        if (listenerThread != null) listenerThread.Abort();
    }
}
