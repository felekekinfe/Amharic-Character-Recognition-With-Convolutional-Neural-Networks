import matplotlib.pyplot as plt
import tensorflow as tf

def train_and_evaluate(model, datagen, X_train, y_train,X_test, y_test):
    """Train the CNN model and evaluate its performance.

    Args:
        model (Sequential): Compiled Keras model.
        datagen (ImageDataGenerator): Data augmentation generator.
        X_train (np.array): Training images, shape (samples, 64, 64, 1).
        y_train (np.array): Training labels, one-hot encoded.
        X_val (np.array): Validation images.
        y_val (np.array): Validation labels.
        X_test (np.array): Test images.
        y_test (np.array): Test labels.

    Returns:
        Sequential: Trained Keras model.
    """
    train_generator=datagen.flow(
        X_train,y_train,batch_size=32,color_mode='grayscale',
        
    )
    history = model.fit(
        train_generator,
        epochs=50,
        validation_data=(X_test, y_test),
        callbacks=[tf.keras.callbacks.EarlyStopping(patience=10)]
    )
    
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print(f"Test Accuracy: {test_acc:.4f}")
    
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Model Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()
    
    return model