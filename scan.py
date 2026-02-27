import os

def generate_sidebar():
    with open('_sidebar.md', 'w', encoding='utf-8') as f:
        # On parcourt les dossiers 'staff' et 'player'
        for folder in ['staff', 'player']:
            if not os.path.exists(folder): continue
            
            f.write(f'* **{folder.upper()}**\n')
            
            for root, dirs, files in os.walk(folder):
                files.sort()
                depth = root.count(os.sep)
                indent = '  ' * (depth + 1)
                
                # Noms des sous-dossiers
                if root != folder:
                    folder_name = os.path.basename(root).replace('-', ' ').title()
                    f.write(f'{indent}* **{folder_name}**\n')
                    indent += '  '

                # Ajout des fichiers
                for file in files:
                    if file.endswith('.md') and file not in ['_sidebar.md', 'README.md' if root=='.' else '']:
                        path = os.path.join(root, file).replace('\\', '/')
                        name = file.replace('.md', '').replace('-', ' ').title()
                        if name.lower() == 'readme': name = "Introduction"
                        f.write(f'{indent}* [{name}]({path})\n')

if __name__ == "__main__":
    generate_sidebar()
