"""
==============================================================================
BLENDER NEXUS CONNECTOR — MIRROR MOUNTAIN & INTERDIMENSIONAL ALPHABET
==============================================================================
Ascolta comandi su Porta 9001 TCP e connette Blender direttamente a:
  - C:\\Users\\autor\\Desktop\\INTERDIMENSIONAL ALPHABET\\01_ASHIA
  - Nexus Command (:8090)
  - Mirror Mountain OS
==============================================================================
"""

import bpy
import socket
import threading
import json
import os
import tempfile
import urllib.request
import base64

PORT = 9001
ALPHABET_DIR = r"C:\Users\autor\Desktop\INTERDIMENSIONAL ALPHABET"
ASHIA_GLB = os.path.join(ALPHABET_DIR, "01_ASHIA", "ashia.glb")

def apply_material_preset(obj, preset_name):
    """Applica un materiale PBR canonico dell'Impero."""
    mat = bpy.data.materials.get(preset_name)
    if not mat:
        mat = bpy.data.materials.new(name=preset_name)
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        bsdf = nodes.get("Principled BSDF")
        if bsdf:
            if preset_name == "GOLD_FIRST_CROSS":
                # Oro Puro Riflettente per la Prima Croce
                bsdf.inputs["Base Color"].default_value = (1.0, 0.766, 0.336, 1.0)
                bsdf.inputs["Metallic"].default_value = 0.95
                bsdf.inputs["Roughness"].default_value = 0.15
            elif preset_name == "OBSIDIAN_RUBINICK":
                # Ossidiana Nera Specchiata
                bsdf.inputs["Base Color"].default_value = (0.02, 0.02, 0.03, 1.0)
                bsdf.inputs["Metallic"].default_value = 0.1
                bsdf.inputs["Roughness"].default_value = 0.05
            elif preset_name == "AETHER_CYAN_CRYSTAL":
                # Cristallo Ciano Fluorescente
                bsdf.inputs["Base Color"].default_value = (0.0, 0.95, 1.0, 1.0)
                bsdf.inputs["Metallic"].default_value = 0.2
                bsdf.inputs["Roughness"].default_value = 0.1
                if "Emission Color" in bsdf.inputs:
                    bsdf.inputs["Emission Color"].default_value = (0.0, 0.8, 0.9, 1.0)
                    bsdf.inputs["Emission Strength"].default_value = 2.0

    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)
    print(f"[BLENDER] Materiale {preset_name} applicato a {obj.name}")

def export_glb_to_alphabet(target_letter="01_ASHIA", filename="ashia.glb"):
    """Esporta la mesh selezionata o l'intera scena direttamente in Interdimensional Alphabet."""
    dest_dir = os.path.join(ALPHABET_DIR, target_letter)
    os.makedirs(dest_dir, exist_ok=True)
    out_path = os.path.join(dest_dir, filename)

    bpy.ops.export_scene.gltf(
        filepath=out_path,
        export_format="GLB",
        use_selection=True if bpy.context.selected_objects else False,
        export_apply=True
    )
    print(f"[BLENDER] GLB Esportato con successo in: {out_path}")
    return out_path

def handle_socket_command(cmd_raw):
    try:
        data = json.loads(cmd_raw)
        action = data.get("action", "")
        print(f"[BLENDER NEXUS] Ricevuto ordine: {action}")

        if action == "APPLY_MATERIAL_PRESET":
            preset = data.get("material_preset", "GOLD_FIRST_CROSS")
            for obj in bpy.context.selected_objects:
                apply_material_preset(obj, preset)
            return {"status": "OK", "action": action, "material": preset}

        elif action == "EXPORT_TO_ALPHABET" or action == "SCRITTURA_EXPORT":
            letter = data.get("letter", "01_ASHIA")
            filename = data.get("filename", "ashia.glb")
            path = export_glb_to_alphabet(letter, filename)
            return {"status": "OK", "path": path, "byte_size": os.path.getsize(path)}

        elif action == "REFINE_GEOMETRY":
            for obj in bpy.context.selected_objects:
                if obj.type == 'MESH':
                    bpy.context.view_layer.objects.active = obj
                    bpy.ops.object.shade_smooth()
            return {"status": "OK", "message": "Shade smooth applicato"}

        return {"status": "UNKNOWN_ACTION", "action": action}
    except Exception as e:
        return {"status": "ERROR", "error": str(e)}

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        server.bind(("127.0.0.1", PORT))
        server.listen(5)
        print(f"=== [BLENDER NEXUS BRIDGE] In ascolto su 127.0.0.1:{PORT} ===")
        while True:
            conn, addr = server.accept()
            try:
                raw = conn.recv(4096).decode("utf-8")
                if raw:
                    res = handle_socket_command(raw)
                    conn.sendall(json.dumps(res).encode("utf-8"))
            finally:
                conn.close()
    except Exception as e:
        print(f"[BLENDER BRIDGE FATAL] {e}")
    finally:
        server.close()

# Avvia il server socket in un thread daemon non bloccante
t = threading.Thread(target=start_server, daemon=True)
t.start()
