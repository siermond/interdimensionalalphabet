import os
from pathlib import Path
from datetime import datetime

CATALOG_PATH = Path(r"C:\Users\autor\Desktop\Catalog\INTERDIMENSIONAL_ASSETS")
OBSIDIAN_DB_PATH = Path(r"C:\Users\autor\Desktop\Thot Brain\INTERDIMENSIONAL_ASSETS_DATABASE.md")

def get_local_assets():
    """Scans the local Catalog for heavy assets and returns metadata."""
    assets = []
    if not CATALOG_PATH.exists():
        print(f"Error: Catalog path {CATALOG_PATH} does not exist.")
        return assets

    for root, _, files in os.walk(CATALOG_PATH):
        for file in files:
            file_path = Path(root) / file
            rel_path = file_path.relative_to(CATALOG_PATH)
            size_mb = file_path.stat().st_size / (1024 * 1024)
            mod_time = datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d %H:%M')
            
            assets.append({
                "name": file,
                "folder": str(rel_path.parent),
                "extension": file_path.suffix.lower(),
                "size_mb": round(size_mb, 2),
                "last_modified": mod_time,
                "full_path": str(file_path)
            })
    return assets

def write_obsidian_database(assets):
    """Generates a Markdown file representing a database in Obsidian."""
    
    # Sort assets by folder, then by name
    assets.sort(key=lambda x: (x["folder"], x["name"]))
    
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    md_content = f"""---
aliases: [Asset Database, Interdimensional Assets]
tags: [database, assets, catalog, interdimensional-alphabet]
---
# 📦 Interdimensional Assets Database

*Ultimo aggiornamento automatico: {now}*

Questo database è sincronizzato in automatico con la cartella `Desktop\\Catalog\\INTERDIMENSIONAL_ASSETS`.
**Non modificare i nomi dei file direttamente qui**, utilizza questo file come pannello di controllo (Notion-style) per appuntare note e stati.

| Nome File | Cartella (Categoria) | Tipo | Peso (MB) | Ultima Modifica | Stato | Note |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
"""

    for a in assets:
        # Default status based on folder
        status = "🟢 PRONTO"
        if "INBOX" in a["folder"].upper():
            status = "🟠 IN LAVORAZIONE (NOMAD)"
        elif "BLENDER" in a["folder"].upper():
            status = "🔵 IN RIGGING/RENDER"
            
        md_content += f"| **{a['name']}** | `{a['folder']}` | `{a['extension']}` | {a['size_mb']} MB | {a['last_modified']} | {status} | ... |\n"
        
    md_content += "\n\n---\n*Generato da `interdimentional alphabet/02_ASSET_BRIDGE/obsidian_asset_bridge.py`*\n"
    
    with open(OBSIDIAN_DB_PATH, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    print(f"OK! Obsidian Database generato con successo!")
    print(f"File: {OBSIDIAN_DB_PATH}")
    print(f"Totale Asset tracciati: {len(assets)}")

if __name__ == "__main__":
    local_assets = get_local_assets()
    if local_assets:
        write_obsidian_database(local_assets)
    else:
        print("Nessun asset trovato nel Catalogo o cartella inesistente.")
