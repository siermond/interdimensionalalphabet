"""
==============================================================================
UNREAL ENGINE 5 NEXUS CONNECTOR — MIRROR MOUNTAIN
==============================================================================
Interagisce con Unreal Engine 5 via Editor Python Scripting e Remote Control
Web Server (Porta 30010) per:
  - Ingestione GLB da INTERDIMENSIONAL ALPHABET\\01_ASHIA
  - Attivazione Sequencer per la cinematica "Order Poem / First Cross"
  - Regia Luci Volumetriche nel buio VR
  - Render cinematico 9:16 (YouTube Shorts) e 16:9 (Trailer Impero)
==============================================================================
"""

import os
import json
import urllib.request

try:
    import unreal
    IN_UNREAL_ENGINE = True
except ImportError:
    IN_UNREAL_ENGINE = False

ALPHABET_DIR = r"C:\Users\autor\Desktop\INTERDIMENSIONAL ALPHABET"
ASHIA_GLB = os.path.join(ALPHABET_DIR, "01_ASHIA", "ashia.glb")
REMOTE_CONTROL_URL = "http://127.0.0.1:30010/remote/object/call"

def import_ashia_glb_to_unreal(destination_path="/Game/InterdimensionalAlphabet/Ashia"):
    """Importa ashia.glb nel Content Browser di Unreal Engine 5."""
    if not IN_UNREAL_ENGINE:
        print("[UNREAL REMOTE] Questo comando richiede l'ambiente Unreal Engine.")
        return False

    if not os.path.exists(ASHIA_GLB):
        unreal.log_warning(f"File GLB non trovato in: {ASHIA_GLB}")
        return False

    task = unreal.AssetImportTask()
    task.filename = ASHIA_GLB
    task.destination_path = destination_path
    task.destination_name = "Ashia_First_Cross_Mesh"
    task.replace_existing = True
    task.automated = True
    task.save = True

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    unreal.log(f"[UNREAL NEXUS] Mesh importata con successo in {destination_path}/Ashia_First_Cross_Mesh")
    return True

def trigger_order_poem_cinematic(sequence_path="/Game/Cinematics/LS_Order_Poem_First_Cross"):
    """Avvia la riproduzione del Level Sequencer per il rituale della Prima Croce."""
    if not IN_UNREAL_ENGINE:
        print("[UNREAL REMOTE] Invio comando Remote Control HTTP...")
        payload = json.dumps({
            "objectPath": "/Game/Cinematics.Cinematics_C",
            "functionName": "PlayOrderPoemRitual"
        }).encode("utf-8")
        try:
            req = urllib.request.Request(REMOTE_CONTROL_URL, data=payload, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=2.0) as resp:
                print(f"[UNREAL HTTP OK] {resp.read().decode('utf-8')}")
                return True
        except Exception as e:
            print(f"[UNREAL HTTP INFO] Remote Control non risponde su 30010 ({e})")
            return False

    seq = unreal.load_asset(sequence_path)
    if seq:
        player, _ = unreal.LevelSequencePlayer.create_level_sequence_player(unreal.EditorLevelLibrary.get_editor_world(), seq, unreal.MovieSceneSequencePlaybackSettings())
        player.play()
        unreal.log("[UNREAL NEXUS] Sequencer Order Poem avviato!")
        return True
    else:
        unreal.log_warning(f"Sequencer non trovato: {sequence_path}")
        return False

if __name__ == "__main__":
    if IN_UNREAL_ENGINE:
        unreal.log("=== UNREAL NEXUS CONNECTOR ATTIVO ===")
        import_ashia_glb_to_unreal()
    else:
        print("Script test connettore Unreal Engine 5 (Standby).")
        trigger_order_poem_cinematic()
