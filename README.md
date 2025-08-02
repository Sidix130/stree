# 🦅 CTEE (Content Tree)

Un outil `tree` amélioré. `ctee` est une commande qui affiche l'arborescence d'un répertoire et le contenu des fichiers texte, avec coloration syntaxique.

Parfait pour créer une documentation lisible de n'importe quel projet de code : explorer, partager ou analyser une architecture.

---

## ✨ Caractéristiques

* **Arborescence visuelle**  : structure claire et hiérarchique.
* **Aperçu de contenu**    : déplie les fichiers texte directement dans l'arbre.
* **Coloration syntaxique**: via la bibliothèque Python `rich`.
* **Filtrage intelligent** : ignore les binaires, images et dossiers comme `.git` ou `node_modules`.
* **Sortie flexible**       : affichage dans le terminal ou export en `.txt` / `.html`.
* **Deux versions**         : Python (recommandée) et Bash (portabilité maximale).

---

## 🚀 Exemple de sortie (Python)

```plaintext
Arborescence de : mon-projet/
├── 📁 css
│   ├── 📄 style.css
│   │   └── body {
│       font-family: 'Arial', sans-serif;
│       color: #333;
│   }
│   └── 📄 responsive.css
│       └── @media (max-width: 768px) {
│           header h1 {
│           font-size: 1.8rem;
│           }
│       }
├── 📁 documentation
│   └── 📄 README.md
│       └── # Mon Projet
│           Ceci est un projet de démonstration...
├── 📁 images
│   ├── 📦 logo.png (binaire)
│   └── 📦 background.jpg (binaire)
├── 📁 js
│   ├── 📄 main.js
│   │   └── document.addEventListener('DOMContentLoaded', function() {
│           console.log('Application chargée !');
│       });
│   └── 📄 utils.js
│       └── function add(a, b) {
│           return a + b;
│       }
└── 📄 index.html
    └── <!DOCTYPE html>
        <html lang="fr">
        <head>
        <title>Mon Projet</title>
        </head>
        </html>
```

---

## 🛠️ Installation & utilisation

### Version Python (recommandée)

**Pré-requis** : Python 3 et `pip`.

1. Installer `rich` :

   ```bash
   pip install rich
   ```
2. Rendre le script exécutable et l’installer :

   ```bash
   chmod +x ctee.py
   sudo mv ctee.py /usr/local/bin/ctee
   ```

**Exemples** :

```bash
# Afficher l'arbre du répertoire courant
ctee

# Arbre d'un projet spécifique
ctee /chemin/vers/projet

# Limiter la profondeur à 2 niveaux
ctee -L 2

# Exporter en snapshot.txt et snapshot.html
ctee -o snapshot
```

### Version Bash (portabilité)

**Pré-requis** : `file`, `find`, `sed` (outils standard Linux).

1. Rendre le script exécutable et l’installer :

   ```bash
   chmod +x ctee.sh
   sudo mv ctee.sh /usr/local/bin/ctee.sh
   ```

**Exemples** :

```bash
# Afficher l'arbre
ctee.sh

# Sauvegarder la sortie
ctee.sh > snapshot.txt
```

---

## 🧭 Philosophie du projet

Ce dépôt explore jusqu'où un simple script Bash peut aller pour un parsing complexe, et quand Python devient nécessaire pour une meilleure expérience.

* **ctee.sh** : approche puriste, puissance du shell.
* **ctee.py** : approche pragmatique, écosystème riche.

Découvrez, améliorez et choisissez la version adaptée à votre workflow !
