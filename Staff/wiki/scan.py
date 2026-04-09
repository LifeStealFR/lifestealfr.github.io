import os

# Configuration
WIKI_DIR = os.path.dirname(os.path.abspath(__file__))
SIDEBAR_FILE = os.path.join(WIKI_DIR, '_sidebar.md')

def get_sidebar_content(current_dir, level=0):
    content = []
    indent = "  " * level
    
    # Récupérer et trier le contenu
    try:
        items = sorted(os.listdir(current_dir))
    except OSError:
        return []

    # 1. On traite d'abord les FICHIERS du dossier actuel
    for item in items:
        path = os.path.join(current_dir, item)
        if os.path.isfile(path) and item.endswith('.md'):
            # On ignore les fichiers de configuration Docsify et le README racine
            if item.startswith('_') or (level == 0 and item.lower() == 'readme.md'):
                continue
            
            name = item.replace('.md', '').replace('-', ' ').replace('_', ' ').title()
            rel_link = os.path.relpath(path, WIKI_DIR).replace('\\', '/')
            content.append(f"{indent}* [{name}]({rel_link})")

    # 2. On traite ensuite les SOUS-DOSSIERS (Récursivité)
    for item in items:
        path = os.path.join(current_dir, item)
        if os.path.isdir(path) and not item.startswith('.'):
            folder_name = item.replace('-', ' ').replace('_', ' ').title()
            content.append(f"{indent}* **{folder_name}**")
            # Appel récursif pour le contenu du sous-dossier (niveau + 1)
            content.extend(get_sidebar_content(path, level + 1))
            
    return content

def generate_sidebar():
    # En-tête du sidebar
    full_sidebar = ["* [🏠 Accueil](README.md)", ""]
    
    # Génération récursive
    full_sidebar.extend(get_sidebar_content(WIKI_DIR))
    
    # Écriture finale
    with open(SIDEBAR_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(full_sidebar))
    
    print(f"✅ Sidebar généré avec une structure récursive stricte.")

if __name__ == "__main__":
    generate_sidebar()
