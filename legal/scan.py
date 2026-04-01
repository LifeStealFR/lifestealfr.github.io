import os

# Détecte AUTOMATIQUEMENT le dossier exact où se trouve scan.py (Staff/wiki)
# Ça évite tous les bugs de chemins ou de majuscules sur GitHub Actions !
WIKI_DIR = os.path.dirname(os.path.abspath(__file__))
SIDEBAR_FILE = os.path.join(WIKI_DIR, '_sidebar.md')

def generate_sidebar():
    # On ouvre le fichier (ou on le crée)
    with open(SIDEBAR_FILE, 'w', encoding='utf-8') as f:
        # Lien d'accueil (ATTENTION : l'espace après l'étoile '* ' est obligatoire en Markdown)
        f.write('*[🏠 Accueil](README.md)\n\n')
        
        # On parcourt les sous-dossiers à partir de là où se trouve scan.py
        for root, dirs, files in os.walk(WIKI_DIR):
            
            # On ignore les dossiers système cachés (comme .git ou .github)
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            # Tri alphabétique
            dirs.sort()
            files.sort()
            
            # Calcul de la position actuelle par rapport au dossier source
            rel_dir = os.path.relpath(root, WIKI_DIR)
            
            if rel_dir == '.':
                depth = 0
            else:
                depth = rel_dir.count(os.sep) + 1
                # 2 espaces par niveau de profondeur pour Docsify
                indent = '  ' * (depth - 1) 
                
                # Nom du dossier affiché dans le menu
                folder_name = os.path.basename(root).replace('-', ' ').title()
                f.write(f'{indent}* **{folder_name}**\n')
            
            # Indentation pour les fichiers (décalés sous leur dossier)
            file_indent = '  ' * depth if rel_dir != '.' else ''
            
            # Ajout des fichiers Markdown
            for file in files:
                if file.endswith('.md') and file not in ['_sidebar.md']:
                    # On ne remet pas l'accueil principal
                    if rel_dir == '.' and file.lower() == 'readme.md':
                        continue 
                        
                    # On crée le lien parfait pour Docsify
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, WIKI_DIR).replace('\\', '/')
                    
                    # On nettoie le nom (ex: "commandes-admin.md" devient "Commandes Admin")
                    name = file.replace('.md', '').replace('-', ' ').title()
                    
                    # On écrit la ligne
                    f.write(f'{file_indent}* [{name}]({rel_path})\n')
                    
    print(f"✅ Menu généré avec succès dans : {SIDEBAR_FILE}")

if __name__ == "__main__":
    generate_sidebar()
