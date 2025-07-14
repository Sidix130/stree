# Stree.py

Absolument. Voici une proposition pour le fichier `README.md`.

Il est conçu pour être "cool mais pro" : il commence de manière directe et attrayante, il explique clairement la valeur, il montre des exemples concrets, et il termine avec des instructions claires et une structure professionnelle.

---

### Le Fichier `README.md`

```markdown
# 🦅 CTEE (Content Tree)

Un `tree` qui ne vous laisse pas tomber. `ctee` est un outil en ligne de commande qui affiche l'arborescence d'un répertoire, mais qui va plus loin en affichant également le contenu des fichiers texte, avec une coloration syntaxique.

C'est l'outil parfait pour créer rapidement une "base de données" lisible de n'importe quel projet de code, que ce soit pour documenter, partager ou simplement analyser une architecture.

---

## ✨ Caractéristiques Principales

*   **Arborescence Visuelle :** Affiche une structure de répertoires claire et hiérarchique.
*   **Aperçu du Contenu :** Déplie le contenu des fichiers texte directement dans l'arbre.
*   **Coloration Syntaxique :** Utilise la puissance de la bibliothèque `rich` pour une lisibilité maximale (Python).
*   **Détection Intelligente :** Ignore automatiquement les fichiers binaires, les images, et les dossiers non pertinents comme `.git` ou `node_modules`.
*   **Sortie Flexible :** Affichez le résultat dans votre terminal ou exportez-le en fichiers `.txt` et `.html` propres.
*   **Deux Versions, Deux Philosophies :** Disponible en version **Python** (recommandée) pour la puissance et en version **Bash** pour la portabilité maximale.

---

## 🚀 Output Exemple (Version Python)

Voici ce que `ctee.py` produit. C'est clair, coloré et incroyablement utile.

```
    Arborescence de : mon-projet/
    ├── 📁 css
    │ ├── 📄 style.css
    │ │ └── body {
    │ │ font-family: 'Arial', sans-serif;
    │ │ color: #333;
    │ │ }
    │ └── 📄 responsive.css
    │ └── @media (max-width: 768px) {
    │ header h1 {
    │ font-size: 1.8rem;
    │ }
    │ }
    ├── 📁 documentation
    │ └── 📄 README.md
    │ └── # Mon Projet
    │ Ceci est un projet de démonstration...
    ├── 📁 images
    │ ├── 📦 logo.png (binaire)
    │ └── 📦 background.jpg (binaire)
    ├── 📁 js
    │ ├── 📄 main.js
    │ │ └── document.addEventListener('DOMContentLoaded', function() {
    │ │ console.log('Application chargée !');
    │ │ });
    │ └── 📄 utils.js
    │ └── function add(a, b) {
    │ return a + b;
    │ }
    └── 📄 index.html
    └── <!DOCTYPE html>
    <html lang="fr">
    <head>
    <title>Mon Projet</title>
    </head>
    </html>
```

---

## 🛠️ Installation et Utilisation

Ce projet propose deux implémentations. La version Python est recommandée pour un usage quotidien.

### Version Python (Recommandée)

**Pré-requis :**
Vous devez avoir Python 3 et `pip` installés.

1.  **Installez la dépendance `rich` :**
    ```bash
    pip install rich
    ```

2.  **Rendez le script exécutable et placez-le dans votre PATH :**
    ```bash
    chmod +x ctee.py
    sudo mv ctee.py /usr/local/bin/ctee
    ```

**Utilisation :**
```bash
# Affiche l'arbre du répertoire courant
ctee

# Affiche l'arbre d'un répertoire spécifique
ctee /chemin/vers/votre/projet

# Limite la profondeur de l'affichage à 2 niveaux
ctee -L 2

# Sauvegarde la sortie dans des fichiers snapshot.txt et snapshot.html
ctee -o snapshot
```

### Version Bash (Pour la portabilité)

Cette version ne nécessite aucune dépendance autre que les outils standards de tout système Linux (`file`, `find`, `sed`).

1.  **Rendez le script exécutable et placez-le dans votre PATH :**
    ```bash
    chmod +x ctee.sh
    sudo mv ctee.sh /usr/local/bin/ctee.sh
    ```

**Utilisation :**
```bash
# Affiche l'arbre du répertoire courant
ctee.sh

# Sauvegarde la sortie dans un fichier
ctee.sh > snapshot.txt
```

---

##  philosophie du Projet

Ce dépôt est né d'une exploration : jusqu'où peut-on pousser un script `bash` pour une tâche de parsing complexe, et à quel moment un langage de plus haut niveau comme Python devient-il non seulement plus pratique, mais nécessaire ?

*   **`ctee.sh`** représente l'approche puriste, un témoignage de la puissance brute du shell.
*   **`ctee.py`** représente l'approche pragmatique, qui tire parti d'un écosystème riche pour offrir une expérience utilisateur supérieure.

N'hésitez pas à explorer les deux, à les améliorer et à choisir celui qui correspond le mieux à votre workflow.
```
