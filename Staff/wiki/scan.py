import os

# Le dossier où se trouve ton wiki (relatif à la racine du repo GitHub)
WIKI_DIR = 'Staff/wiki'
SIDEBAR_FILE = os.path.join(WIKI_DIR, '_sidebar.md')

def generate_sidebar():
    with open(SIDEBAR_FILE, 'w', encoding='utf-8') as f:
        # Lien d'accueil par défaut
        f.write('*[🏠 Accueil du Wiki](README.md)\n\n')
        
        # On parcourt UNIQUEMENT le dossier Staff/wiki
        for root, dirs, files in os.walk(WIKI_DIR):
            # On trie pour avoir un bel ordre alphabétique
            dirs.sort()
            files.sort()
            
            # On calcule à quelle "profondeur" on est dans les dossiers
            rel_dir = os.path.relpath(root, WIKI_DIR)
            
            # Si on est à la racine de Staff/wiki (rel_dir == '.')
            if rel_dir == '.':
                depth = 0
            else:
                depth = rel_dir.count(os.sep) + 1
                indent = '  ' * (depth - 1)
                
                # On écrit le nom du dossier comme catégorie
                folder_name = os.path.basename(root).replace('-', ' ').title()
                f.write(f'{indent}* **{folder_name}**\n')
            
            # Indentation pour les fichiers dans ce dossier
            file_indent = '  ' * depth if rel_dir != '.' else ''
            
            # Ajout des fichiers Markdown
            for file in files:
                # On ne prend que les .md et on ignore sidebar et l'accueil principal
                if file.endswith('.md') and file not in ['_sidebar.md']:
                    if rel_dir == '.' and file.lower() == 'readme.md':
                        continue # On a déjà ajouté l'Accueil manuellement tout en haut
                        
                    # On crée le chemin pour Docsify (ex: reglements/regles-ig.md)
                    rel_path = os.path.relpath(os.path.join(root, file), WIKI_DIR).replace('\\', '/')
                    
                    # On nettoie le nom du fichier pour faire joli
                    name = file.replace('.md', '').replace('-', ' ').title()
                    
                    # On écrit la ligne dans le menu
                    f.write(f'{file_indent}* [{name}]({rel_path})\n')

if __name__ == "__main__":
    generate_sidebar()
