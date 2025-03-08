import os

def check_dataset_structure(dataset_path):
    missing_labels = []
    for folder in ['train', 'test']:
        folder_path = os.path.join(dataset_path, folder)
        images = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
        for image in images:
            label_file = os.path.splitext(image)[0] + '.txt'
            if not os.path.exists(os.path.join(folder_path, label_file)):
                missing_labels.append(image)
    
    if missing_labels:
        print("Les images suivantes n'ont pas de fichiers d'annotations :")
        for img in missing_labels:
            print(img)
    else:
        print("Toutes les images ont des fichiers d'annotations correspondants.")

dataset_path = r"..\TP2\D-Fire"
check_dataset_structure(dataset_path)
