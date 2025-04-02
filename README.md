
# 🌟 **Amharic Hand written Letter Recognition System**

## 📖 Overview
Welcome to the **Amharic Hand written Letter Recognition System**! This project uses a **Convolutional Neural Network (CNN)** built with **TensorFlow** to classify Amharic characters from images. Amharic, the official language of Ethiopia, uses the unique Ge'ez script. Our system recognizes 22 Amharic letters, each in all 7 of their forms, totaling **154 unique characters**. 

This system is a powerful tool for:
- 📝 **Optical Character Recognition (OCR)** for Amharic texts
- 📚 **Language learning tools**
- 🖼️ **Digitizing handwritten Amharic documents**

With this project, you get a complete pipeline, from data preprocessing to model training and prediction, all tailored for recognizing Amharic characters.

---

## ✨ Features
- **Data Preprocessing**: Seamlessly preprocesses Amharic character images for prediction.
- **CNN Model**: Custom-built Convolutional Neural Network for classifying Amharic characters using **TensorFlow**.
- **Training & Evaluation**: Tools to train and evaluate the model.
- **Prediction**: Predict Amharic characters from new images.

---

## 🗂️ Project Structure

Here’s how the project is organized:

```
📁 dataset/
    └── train/
        ├── ሀ/    # Images of ሀ
        ├── ሁ/    # Images of ሁ
        ├── ሂ/    # Images of ሂ
        ├── ሃ/    # Images of ሃ
        ├── ሄ/    # Images of ሄ
        ├── ህ/    # Images of ህ
        ├── ሆ/    # Images of ሆ
        ├── ለ/    # Images of ለ
        ├── ሉ/    # Images of ሉ
        ├── ሊ/    # Images of ሊ
        ├── ላ/    # Images of ላ
        ├── ሌ/    # Images of ሌ
        ├── ል/    # Images of ል
        ├── ሎ/    # Images of ሎ
        ├── ...   # (Folders for the remaining letters)
```

- **`dataset/`**: Contains your training data.
- **`model_construction/`**: Includes the CNN model architecture.
- **`src/`**: Core scripts for data loading, training, prediction, and preprocessing.
- **`trash/`**: Miscellaneous or temporary files.
- **`.gitignore`**: Specifies files to ignore in version control.
- **`h.py`**: Helper functions (if any).
- **`word_list.txt`**: List of Amharic words or labels (if applicable).
- **`README.md`**: The file you're reading!

---

## 🛠️ Requirements
To get started, make sure you have these dependencies installed:

- 🐍 **Python 3.8 or higher**
- 🧠 **TensorFlow** (for model training and inference)
- 🔢 **NumPy** (for numerical operations)
- 🖼️ **OpenCV** or **Pillow** (for image processing)
- 📊 **Matplotlib** (for optional visualizations)

To install these dependencies, run:
```bash
pip install tensorflow numpy opencv-python pillow matplotlib
```

---

## 📂 Dataset

### 🌐 **Source**
The dataset was sourced from a post or user on the platform **X**. Initially, all Amharic character images were in a single folder, with filenames indicating the character (e.g., `eh_1.jpg` for the Amharic letter **ሀ**).

### 🛠️ **Dataset Preparation**
We organized the dataset into a structured format by:
1. **Grouping Images**  
   A script sorted images based on the character name in the filename. For example, images like `eh_1.jpg` were placed in the `eh/` folder.
   
2. **Renaming to Amharic**  
   The folders were renamed to their corresponding Amharic characters. For example, `eh/` became `ሀ/`, and `le/` became `ለ/`.

3. **Supported Characters**  
   This project supports the following 22 Amharic letters, each in all 7 forms (e.g., for **ሀ**: ሀ, ሁ, ሂ, ሃ, ሄ, ህ, ሆ):
   - **ሀ, ለ, መ, ረ, ሰ, ቀ, በ, ቨ, ተ, ቸ, ኀ, ነ, አ, ከ, ወ, ዘ, ደ, ጀ, ገ, ጸ, ፈ, ፐ**

   This gives us a total of **154 unique characters**.

4. **Final Structure**
   The dataset structure looks like this:

   ```
   dataset/
   └── train/
       ├── ሀ/    # Images of ሀ
       ├── ሁ/    # Images of ሁ
       ├── ...   # Images for all 154 characters
   ```

   All images are resized to **64x64 pixels** for consistency.

---

## 🚀 Usage

### 1. 📥 **Prepare the Dataset**
Ensure your dataset is in the `dataset/train/` directory, with subfolders named using Amharic characters. The dataset should follow the structure:
- **ሀ/**, **ሁ/**, **ለ/**, etc. (for all 154 characters).

If your images are in a single folder:
- **Group** the images into folders based on the character name.
- **Rename** the folders to Amharic characters.

### 2. 🖼️ **Preprocess the Data**
The preprocessing script prepares the images for prediction. This script is triggered **before** making predictions and resizes the images into a consistent format (64x64 pixels).

Run the preprocessing script:
```bash
python src/preprocessing.py
```

### 3. 🏋️ **Train the Model**
Train the CNN model with the following command:
```bash
python src/train.py
```
This will save the trained model as `amharic_cnn.h5` (a TensorFlow saved model file).

### 4. 🔍 **Make Predictions**
To make predictions on new images, run the prediction script. This will use the trained model to classify Amharic characters from the input image:
```bash
python src/predictor.py --image_path path/to/your/image.png
```
This will output the predicted Amharic character (from the 154 supported characters).

---

## 🤝 **Contributing**
We welcome your contributions! Here’s how you can help:
1. 🍴 **Fork** the repository.
2. 🌿 **Create** a branch for your feature or fix.
3. 📨 **Submit a pull request** with a clear description of your changes.

---

## 📜 **License**
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 📬 **Contact**
If you have questions or suggestions, feel free to open an issue or contact the project maintainer at [GitHub Repository](https://github.com/felekekinfe/Amharic-Character-Recognition-With-Convolutional-Neural-Networks).

