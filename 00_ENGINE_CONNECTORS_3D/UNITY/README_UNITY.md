# Connettore Unity ➔ Mirror Mountain & Interdimensional Alphabet

Questo modulo collega **Unity** (2022 LTS / 6) con la scena WebXR di **Mirror Mountain** e **Interdimensional Alphabet**.

### Funzionalità:
1. **Ricezione Ordini Rituali (Porta 9002 TCP)**:
   - Riceve in tempo reale istruzioni per attivare il rituale *Divine Light Pray / Order Poem*.
   - Gestisce la transizione da buio cosmico VR all'accensione della luce dorata.
2. **Setup Sfera Immersiva 360° (528 Hz)**:
   - Configura skybox ed essenza di preghiera.
3. **Rig Avatar Servant of Humanity**:
   - Coordina l'ancoraggio e la visualizzazione del modello Avatar con il libro del Kybalion.
4. **Ingestione GLB da Interdimensional Alphabet**:
   - Punta direttamente alla cartella canonica `INTERDIMENSIONAL ALPHABET\01_ASHIA\ashia.glb`.

### Come utilizzarlo:
1. Trascina il file `UnityNexusBridge.cs` nella cartella `Assets/Scripts` del tuo progetto Unity.
2. Aggiungi il componente `UnityNexusBridge` a un GameObject vuoto nella scena principale.
3. Assegna nell'Inspector i riferimenti per la Croce Dorata, la Luce Cosmica e l'Avatar Servant.
4. Premi **Play** in Unity: il server TCP si attiverà automaticamente sulla porta `9002`.
