from data_loader import DataLoader
from model import build_cnn_model
from train import train_and_evaluate
from sklearn.model_selection import train_test_split
def main():
    """Execute the Amharic character recognition pipeline."""
    # Load data
    train_loader = DataLoader("dataset/train")
    X_train_full, y_train_full = train_loader.load_data()
    
   # test_loader = DataLoader("dataset/test")
    #X_test, y_test = test_loader.load_data()
    
    # Split train into train/validation
    X_train, X_test, y_train, y_test = train_test_split(
        X_train_full, y_train_full, test_size=0.2, random_state=42
    )
    
    # Build model
    num_classes = train_loader.num_classes
    model = build_cnn_model(num_classes)
    
    # Train and evaluate
    datagen = train_loader.get_datagen()
    model = train_and_evaluate(model, datagen, X_train, y_train,X_test, y_test)
    
    # Save model
    model.save("amharic_cnn.h5")
    print("Model saved as 'amharic_cnn.h5'")

if __name__ == "__main__":
    main()