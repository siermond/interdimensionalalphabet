# Connettore Blender ➔ Mirror Mountain & Interdimensional Alphabet

Questo modulo collega **Blender** con l'infrastruttura di **Mirror Mountain** e **Interdimensional Alphabet**.

### Funzionalità:
1. **Esportazione Diretta in Interdimensional Alphabet**:
   - Salva automaticamente le sculture selezionate in formato `.glb` direttamente in `INTERDIMENSIONAL ALPHABET\01_ASHIA\ashia.glb` (o in qualsiasi lettera specificata).
2. **Preset Materiali Canonici PBR**:
   - `GOLD_FIRST_CROSS`: Oro puro riflettente per la Prima Croce.
   - `OBSIDIAN_RUBINICK`: Ossidiana nera profonda.
   - `AETHER_CYAN_CRYSTAL`: Cristallo ciano con emissione energetica.
3. **Socket Server TCP (Porta 9001)**:
   - Riceve in tempo reale istruzioni dal `nexus_vr_daemon.py` e da Mirror Mountain OS.

### Come utilizzarlo:
- **Metodo Automatico**: Esegui `AVVIA_BLENDER_BRIDGE.cmd`.
- **Metodo Manuale**: Apri Blender, vai nella vista *Scripting*, apri `blender_nexus_sync.py` e clicca su **Run Script** (Play).
