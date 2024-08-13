import os

def remove_empty_files(directory):
    # Vérifie si le répertoire existe
    if not os.path.isdir(directory):
        print(f"Le répertoire {directory} n'existe pas.")
        return

    # Parcourt tous les fichiers dans le répertoire
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Vérifie si c'est un fichier et non un répertoire
        if os.path.isfile(file_path):
            # Vérifie si le fichier est vide
            if os.path.getsize(file_path) == 0:
                try:
                    os.remove(file_path)
                    print(f"Fichier supprimé : {file_path}")
                except Exception as e:
                    print(f"Erreur lors de la suppression du fichier {file_path}: {e}")

if __name__ == "__main__":
    directory_to_clean = '.'  # Changez ce chemin pour le répertoire à nettoyer
    remove_empty_files(directory_to_clean)
