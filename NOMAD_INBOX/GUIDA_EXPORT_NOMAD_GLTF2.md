# GUIDA OPERATIVA: ESPORTAZIONE DA NOMAD SCULPT IN glTF 2.0 (.glb)

Per alimentare Mirror Mountain, l'Interdimensional Alphabet e i motori 3D (Blender, Unity, Unreal), Nomad Sculpt deve esportare secondo lo standard **glTF 2.0 Binary**.

---

### 📲 ISTRUZIONI PASSO-PASSO IN NOMAD SCULPT:

1. **Apri il Menu Progetto**:
   - Tocca l'icona della **Cartella / File** in alto a sinistra.

2. **Seleziona la scheda Export**:
   - Scorri fino alla sezione **Export** (Esporta).

3. **Scegli il Formato**:
   - Tocca **glTF**.

4. **Configura i Parametri glTF 2.0**:
   - Tipo di formato: **Binary (.glb)** *(NON selezionare .gltf separato con cartella texture)*.
   - Spunta su: **Vertex Colors** (conserva i colori dipinti a mano).
   - Spunta su: **PBR (Roughness / Metalness)** (conserva la lucentezza e le proprietà metalliche).
   - Spunta su: **Normals** (ottimizza le ombre e la resa volumetrica).

5. **Salvataggio / Destinazione**:
   - Fai tap su **Export glTF**.
   - Salva o trasferisci il file sul computer dentro:
     `C:\Users\autor\Desktop\NOMAD_INBOX\`
     *(oppure direttamente in C:\Users\autor\Desktop\INTERDIMENSIONAL ALPHABET\01_ASHIA\ashia.glb)*.

---

### ⚙️ SPECIFICHE CANONICHE DELL'IMPERO:
- **Standard Tecnico**: glTF 2.0 Binary (`.glb`)
- **Magic Header Binario**: `0x46546c67` (`glTF` in ASCII)
- **Versione**: `2` (uint32 a offset 4)
- **Frequenza di Risonanza**: 528 Hz
- **Risoluzione Poligonale Consigliata per VR**: 50.000 – 300.000 vertici per fluidità a 90 FPS
