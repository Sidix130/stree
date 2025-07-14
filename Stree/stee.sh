#!/bin/bash
# ctee.sh - Un "super tree" qui affiche le contenu des fichiers texte.
# Version 3.0 - Approche simplifiée et directe.

set -euo pipefail

# --- CONFIGURATION ---
EXCLUDED_EXTENSIONS='.(png|jpg|jpeg|gif|bmp|ico|webp|svg|mp3|wav|ogg|flac|mp4|mkv|avi|mov|webm|pdf|doc|docx|xls|xlsx|ppt|pptx|odt|zip|tar|gz|bz2|7z|rar|pyc|pyo|o|so|a|dll|exe|class|ttf|otf|woff|woff2|db|sqlite3)$'
# On va utiliser find pour l'exclusion, c'est plus puissant.
EXCLUDED_DIRS=('.git' '__pycache__' 'node_modules' 'venv' '.vscode')
EXCLUDED_FILES=('.gitignore' 'LICENSE' 'package-lock.json' 'yarn.lock')

# --- FONCTION DE TRAITEMENT ---
process_path() {
    local full_path="$1"
    local prefix="$2"
    local base_name
    base_name=$(basename "$full_path")

    echo -e "${prefix}${base_name}"

    # Si c'est un fichier, on tente d'afficher son contenu
    if [ -f "$full_path" ]; then
        # Détection binaire simple et directe
        if ! file -b --mime-type "$full_path" | grep -q "text"; then
            return
        fi

        # Affichage du contenu avec une indentation fixe et simple
        # On utilise une pipe pour ne pas avoir de sous-shell complexe
        sed 's/^/    └── /' "$full_path"
    fi
}

# --- SCRIPT PRINCIPAL ---
main() {
    local start_dir="${1:-.}"

    if [ ! -d "$start_dir" ]; then
        echo "ERREUR: Le répertoire '$start_dir' n'existe pas." >&2
        exit 1
    fi

    local full_start_dir
    full_start_dir=$(realpath "$start_dir")
    echo -e "$(basename "$full_start_dir")/"

    # Construction de la commande find avec les exclusions
    local find_cmd="find \"${full_start_dir}\" -mindepth 1"
    
    # Exclure les répertoires
    for dir in "${EXCLUDED_DIRS[@]}"; do
        find_cmd+=" -not ( -path \"*/${dir}/*\" -o -name \"${dir}\" )"
    done
    
    # Exclure les fichiers
    for file in "${EXCLUDED_FILES[@]}"; do
        find_cmd+=" -not -name \"${file}\""
    done

    # Exclure les extensions
    find_cmd+=" -not -iregex '.*${EXCLUDED_EXTENSIONS}'"

    # La magie est ici : on utilise 'sed' pour créer les préfixes d'arborescence
    eval "$find_cmd" | sed -e "s/[^-][^\\/]*\\//  │  /g" -e "s/\\/\\([^\\/]*\\)$/  ├── \\1/" | while read -r line; do
        echo "$line"
        # EXTRACTION DU CHEMIN ET AFFICHAGE CONTENU
        # Cette partie devient très complexe en bash pur pour garder la structure.
        # La version python est supérieure pour cette tâche.
        # On va se concentrer sur l'affichage de l'arborescence pour l'instant.
    done
}

# Pour le moment, revenons à une version qui DOIT afficher l'arbre, on règlera le contenu après.

# --- VERSION 3.1 - On se concentre sur l'arbre ---

generate_tree_only() {
    local directory="$1"
    local prefix="$2"

    # Lister les enfants, dossiers en premier
    local children=$(ls -1 --group-directories-first "$directory")
    if [ -z "$children" ]; then
        return
    fi
    
    local count=$(echo "$children" | wc -l)
    local i=0

    while IFS= read -r entry; do
        i=$((i+1))
        local connector="├── "
        local new_prefix="│   "

        if [ $i -eq $count ]; then
            connector="└── "
            new_prefix="    "
        fi

        echo "${prefix}${connector}${entry}"

        local full_path="${directory}/${entry}"
        if [ -d "$full_path" ]; then
            generate_tree_only "$full_path" "${prefix}${new_prefix}"
        elif [ -f "$full_path" ]; then
            # Affichage CONTENU - ON REFAIT CETTE PARTIE SIMPLEMENT
             if file -b --mime-type "$full_path" | grep -q "text"; then
                # On utilise paste et sed pour un formatage propre
                 paste <(printf '%s\\n' "└──") <(sed 's/^/ /' "$full_path") | sed "s/^/${prefix}${new_prefix} /"
             fi
        fi

    done <<< "$children"
}


# --- SCRIPT PRINCIPAL v3.1 ---

START_DIR="${1:-.}"
if [[ ! -d "$START_DIR" ]]; then
    echo "ERREUR: Le répertoire '$START_DIR' n'existe pas." >&2
    exit 1
fi

FULL_PATH=$(realpath "$START_DIR")
echo -e "$(basename "$FULL_PATH")/"
generate_tree_only "$FULL_PATH" ""
