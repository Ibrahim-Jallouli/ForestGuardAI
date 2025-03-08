import tensorflow as tf
from ultralytics import YOLO

def configure_gpu():
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        try:
            tf.config.set_visible_devices(gpus[0], 'GPU')
            tf.config.experimental.set_memory_growth(gpus[0], True)
            print("Project is running on GPU:", tf.config.experimental.get_device_details(gpus[0])['device_name'])
        except RuntimeError as e:
            print("Error during GPU configuration:", e)
    else:
        print("No GPU detected. Project is running on CPU.")

def main():
    # Configurer le GPU
    configure_gpu()

    # Charge le modèle préentraîné YOLOv8 
    model = YOLO('yolov8s.pt')

    # Entraîner le modèle
    model.train(
        data='dfire.yaml',  
        epochs=20,          
        imgsz=512,          
        batch=4,            
        device='cuda',      
        workers=1
    )

if __name__ == '__main__':
    main()
