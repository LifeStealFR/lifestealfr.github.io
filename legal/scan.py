import os

# On définit explicitement les dossiers par rapport à la racine du repo
REPO_ROOT = os.getcwd()
WIKI_REL_PATH = "legal"
WIKI_DIR = os.path.join(REPO_ROOT, WIKI_REL_PATH)
SIDEBAR_FILE = os.path.join(WIKI_DIR, '_sidebar.md')

def get_sidebar_content(current_dir, level=0):
    content = []
    indent = "  " * level
    
    if not os.path.exists(current_dir):
        return []

    items = sorted(os.listdir(current_dir))

    # 1. FICHIERS du dossier actuel
    for item in items:
        path = os.path.join(current_dir, item)
        if os.path.isfile(path) and item.endswith('.md'):
            # On ignore les fichiers de config et le README racine
            if item.startswith('_') or (level == 0 and item.lower() == 'readme.md'):
                continue
            
            name = item.replace('.md', '').replace('-', ' ').replace('_', ' ').title()
            # Calcul du lien relatif par rapport au dossier WIKI_DIR pour Docsify
            rel_link = os.path.relpath(path, WIKI_DIR).replace('\\', '/')
            content.append(f"{indent}* [{name}]({rel_link})")

    # 2. SOUS-DOSSIERS (Récursivité)
    for item in items:
        path = os.path.join(current_dir, item)
        if os.path.isdir(path) and not item.startswith('.'):
            folder_name = item.replace('-', ' ').replace('_', ' ').title()
            # On vérifie s'il y a des fichiers .md dedans avant d'ajouter le dossier
            sub_content = get_sidebar_content(path, level + 1)
            if sub_content:
                content.append(f"{indent}* **{folder_name}**")
                content.extend(sub_content)
            
    return content

def generate_sidebar():
    print(f"🔍 Scan du dossier : {WIKI_DIR}")
    
    # En-tête du sidebar
    full_sidebar = ["* [🏠 Accueil](README.md)", ""]
    
    # Génération
    content = get_sidebar_content(WIKI_DIR)
    
    if not content:
        print("⚠️ Aucun fichier Markdown trouvé !")
        return

    full_sidebar.extend(content)
    
    # Écriture
    with open(SIDEBAR_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(full_sidebar))
    
    print(f"✅ Terminé ! {len(content)} entrées dans {SIDEBAR_FILE}")

if __name__ == "__main__":
    generate_sidebar()
