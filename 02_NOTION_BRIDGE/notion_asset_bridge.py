import os
import glob
from pathlib import Path
from dotenv import load_dotenv
from notion_client import Client

# Load environment variables from .env file
load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

CATALOG_PATH = Path(r"C:\Users\autor\Desktop\Catalog\INTERDIMENSIONAL_ASSETS")

def get_local_assets():
    """Scans the local Catalog for heavy assets and returns metadata."""
    assets = []
    if not CATALOG_PATH.exists():
        print(f"Error: Catalog path {CATALOG_PATH} does not exist.")
        return assets

    for root, _, files in os.walk(CATALOG_PATH):
        for file in files:
            file_path = Path(root) / file
            # Get relative path for easier reading
            rel_path = file_path.relative_to(CATALOG_PATH)
            size_mb = file_path.stat().st_size / (1024 * 1024)
            
            assets.append({
                "name": file,
                "folder": str(rel_path.parent),
                "extension": file_path.suffix.lower(),
                "size_mb": round(size_mb, 2),
                "full_path": str(file_path)
            })
    return assets

def sync_to_notion():
    if not NOTION_TOKEN or not DATABASE_ID:
        print("Error: NOTION_TOKEN or NOTION_DATABASE_ID not found in .env file.")
        return

    print("Initialize Notion Client...")
    notion = Client(auth=NOTION_TOKEN)

    print("Scanning local Catalog...")
    local_assets = get_local_assets()
    print(f"Found {len(local_assets)} assets in {CATALOG_PATH}")

    # TODO: Fetch existing records from Notion to avoid duplicates
    # For now, this is a skeleton structure. Once the user provides the DB structure,
    # we will map the local_assets to Notion properties.
    
    print("\n[READY] The bridge is prepared. Awaiting Notion Database connection...")

if __name__ == "__main__":
    sync_to_notion()
