import os
import shutil

import PyInstaller.__main__

script_name = 'src/main.py'
executable_name = 'SnakeSprint'

data_files = [
    ('assets/sounds/sfx-impact.mp3', 'assets/sounds'),
    ('assets/sounds/sfx-fail.wav', 'assets/sounds'),
    ('assets/images/me.jpg', 'assets/images'),
    ('src/ui_menus.py', 'src'),
    ('src/ui_buttons.py', 'src'),
    ('src/utils.py', 'src'),
    ('src/particle.py', 'src'),
    ('src/config.py', 'src')
]

# Limpar pastas build e dist
folders_to_clean = ['build', 'dist']
for folder in folders_to_clean:
    if os.path.exists(folder):
        shutil.rmtree(folder)

# Adicionar os outros arquivos --add-data
add_data_options = []
for source, destination in data_files:
    # Adicionar o caminho correto para o PyInstaller
    add_data_options.append('--add-data')
    add_data_options.append(f'{source};{destination}')

# Executa o PyInstaller com as opções
PyInstaller.__main__.run([
    '--onefile',
    '--noconsole',
    '--name', executable_name,
    *add_data_options,
    script_name
])
