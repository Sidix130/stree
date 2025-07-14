#!/usr/bin/env python3

import os
import sys
import argparse
from typing import Set

# Utilisation de Rich pour un affichage en couleur et stylisé
from rich.console import Console
from rich.tree import Tree
from rich.text import Text
from rich.syntax import Syntax # <-- CORRECTION: Le '=' a été supprimé ici

# --- CONFIGURATION ---
EXCLUDED_DIRS: Set[str] = {'.git', '__pycache__', 'node_modules', 'venv', '.vscode'}
EXCLUDED_FILES: Set[str] = {'.gitignore', 'LICENSE', 'package-lock.json', 'yarn.lock'}
console = Console()

def is_text_file(filepath: str) -> bool:
    """Détermine si un fichier est textuel en se basant sur son contenu."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            f.read(1024)  # Lire un petit échantillon suffit
        return True
    except (IOError):
        return False

def build_tree(directory: str, tree: Tree, level: int = 0, max_level: int = -1) -> None:
    """Construit récursivement l'arborescence du projet."""
    if max_level != -1 and level >= max_level:
        return

    try:
        # Lister les entrées et les trier (dossiers en premier)
        paths = sorted(
            [os.path.join(directory, path) for path in os.listdir(directory)],
            key=lambda p: (os.path.isfile(p), p.lower())
        )
    except PermissionError:
        tree.add(Text(f"⛔ Accès refusé", style="bold red"))
        return

    for path in paths:
        base_name = os.path.basename(path)
        
        # Exclure les dossiers et fichiers non désirés
        if base_name in EXCLUDED_DIRS or base_name in EXCLUDED_FILES:
            continue

        if os.path.isdir(path):
            # C'est un dossier, on crée une nouvelle branche
            branch = tree.add(f"📁 [bold cyan]{base_name}[/]", guide_style="bold blue")
            build_tree(path, branch, level + 1, max_level)
        else:
            # C'est un fichier
            if is_text_file(path):
                # Fichier texte : on affiche le nom et le contenu
                file_node = tree.add(f"📄 [green]{base_name}[/]")
                
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Détecter le type de fichier pour une meilleure coloration
                        lexer_name = "bash"
                        if path.endswith('.py'): lexer_name = "python"
                        if path.endswith('.json'): lexer_name = "json"
                        if path.endswith('.css'): lexer_name = "css"
                        if path.endswith('.html'): lexer_name = "html"
                        
                        # Utilise le composant Syntax de Rich pour une coloration syntaxique automatique
                        syntax = Syntax(
                            content, 
                            lexer_name, 
                            theme="monokai", 
                            line_numbers=False,
                            word_wrap=True
                        )
                        file_node.add(syntax)
                except Exception as e:
                    file_node.add(Text(f"[ERREUR LECTURE: {e}]", style="italic red"))
            else:
                # Fichier binaire : on affiche juste le nom
                tree.add(f"📦 [dim]{base_name} (binaire)[/]")

def main() -> None:
    """Fonction principale pour l'outil en ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Génère une arborescence d'un répertoire avec le contenu des fichiers texte.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        'directory',
        metavar='RÉPERTOIRE',
        nargs='?',
        default='.',
        help='Le répertoire cible à scanner (défaut: répertoire courant).'
    )
    parser.add_argument(
        '-o', '--output',
        metavar='FICHIER',
        help='Sauvegarde la sortie dans un fichier au format texte et HTML.'
    )
    parser.add_argument(
        '-L', '--level',
        metavar='NIVEAU',
        type=int,
        default=-1,
        help='Limite la profondeur de l\'affichage de l\'arborescence.'
    )
    args = parser.parse_args()

    target_dir = args.directory
    if not os.path.isdir(target_dir):
        console.print(f"[bold red]Erreur:[/bold red] Le répertoire '{target_dir}' n'existe pas.", style="red")
        sys.exit(1)
        
    # Créer l'arbre
    real_path = os.path.realpath(target_dir)
    tree_title = f"[bold]Arborescence de : [link file://{real_path}]{os.path.basename(real_path)}[/][/]"
    tree = Tree(tree_title, guide_style="bold blue")

    build_tree(real_path, tree, max_level=args.level)

    # Afficher ou sauvegarder
    if args.output:
        console.print(f"Génération de la structure dans les fichiers : [bold green]{args.output}.txt[/] et [bold green]{args.output}.html[/]")
        # Sauvegarder en format texte simple
        with open(f"{args.output}.txt", "w", encoding="utf-8") as f:
            # On utilise une console temporaire pour capturer le texte sans les couleurs
            text_console = Console(file=f, record=True, force_terminal=False, width=120)
            text_console.print(tree)
        # Sauvegarder en format HTML pour un rendu riche
        console.save_html(f"{args.output}.html", clear=False)
        console.print("✓ Terminé.")
    else:
        console.print(tree)

if __name__ == '__main__':
    main()
