import os

# Configuration : Dossiers à ignorer
IGNORED_DIRS = {'.git', '.github', 'assets', 'images', 'img'}
# Fichiers à ignorer
IGNORED_FILES = {'_sidebar.md', '_navbar.md', 'index.html', 'generate_sidebar.py', '.nojekyll', 'CNAME'}

def get_clean_name(name):
    """Transforme 'types-de-ticket.md' en 'Types De Ticket'"""
    name = os.path.splitext(name)[0]  # Enlève .md
    name = name.replace('-', ' ').replace('_', ' ') # Enlève tirets
    return name.title() # Met des majuscules

def generate_markdown(start_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        # On parcourt les dossiers
        for root, dirs, files in os.walk(start_path):
            # Filtrer les dossiers cachés et ignorés
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in IGNORED_DIRS]
            files = [file for file in files if not file.startswith('.') and file not in IGNORED_FILES]
            
            # Trier pour avoir un ordre constant
            dirs.sort()
            files.sort()

            # Calculer la profondeur pour l'indentation
            depth = root.replace(start_path, '').count(os.sep)
            indent = '  ' * depth
            
            # Nom du dossier courant (pour le titre)
            folder_name = os.path.basename(root)
            
            # Si on n'est pas à la racine, on affiche le nom du dossier
            if root != start_path:
                clean_folder = get_clean_name(folder_name)
                f.write(f'{indent}* **{clean_folder}**\n')
                indent += '  ' # On décale pour le contenu du dossier

            # Ajouter les fichiers
            for file in files:
                if file.endswith('.md'):
                    # Chemin relatif pour le lien
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, start_path).replace('\\', '/')
                    
                    # Nom d'affichage
                    display_name = get_clean_name(file)
                    
                    # Cas spécial : Si c'est README.md, on l'appelle "Introduction" ou le nom du dossier
                    if file.lower() == 'readme.md':
                        if root == start_path:
                            display_name = "Accueil"
                        else:
                            display_name = "Introduction"

                    f.write(f'{indent}* [{display_name}]({rel_path})\n')

if __name__ == "__main__":
    print("Génération de l'arborescence...")
    generate_markdown('.', '_sidebar.md')
    print("Terminé ! Le fichier _sidebar.md a été mis à jour.")
