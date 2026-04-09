import os

# Détection du répertoire courant
WIKI_DIR = os.path.dirname(os.path.abspath(__file__))
SIDEBAR_FILE = os.path.join(WIKI_DIR, '_sidebar.md')

def generate_sidebar():
    lines = []
    # 1. Lien d'accueil obligatoire
    lines.append('* [🏠 Accueil](README.md)\n')

    # On utilise os.walk pour scanner les fichiers
    for root, dirs, files in os.walk(WIKI_DIR):
        # Ignorer les dossiers cachés (.git, .github, etc.)
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        dirs.sort()
        files.sort()

        # Calcul du chemin relatif par rapport à la racine du wiki
        rel_path = os.path.relpath(root, WIKI_DIR)
        
        # Définition du niveau d'indentation (Docsify utilise 2 ou 4 espaces)
        level = 0 if rel_path == '.' else rel_path.count(os.sep) + 1
        indent = '  ' * level

        # Si on est dans un sous-dossier, on affiche le nom du dossier en gras
        if rel_path != '.':
            folder_name = os.path.basename(root).replace('-', ' ').replace('_', ' ').title()
            lines.append(f'{indent}* **{folder_name}**')
            # On augmente l'indentation pour les fichiers à l'intérieur
            indent += '  '

        # Ajout des fichiers .md
        for file in files:
            if file.endswith('.md') and not file.startswith('_'):
                # On ignore le README.md à la racine car déjà mis en Accueil
                if rel_path == '.' and file.upper() == 'README.MD':
                    continue
                
                # Nettoyage du nom pour l'affichage
                display_name = file.replace('.md', '').replace('-', ' ').replace('_', ' ').title()
                
                # Construction du lien relatif propre (URL friendly)
                file_link = os.path.join(rel_path, file).replace('\\', '/')
                if file_link.startswith('./'):
                    file_link = file_link[2:]
                
                lines.append(f'{indent}* [{display_name}]({file_link})')

    # Écriture propre dans le fichier
    with open(SIDEBAR_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
        
    print(f"✅ Wiki scanné : {len(lines)} entrées générées dans _sidebar.md")

if __name__ == "__main__":
    generate_sidebar()
