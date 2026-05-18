Plant Disease Detection with Weather-Aware Deep Learning (TFLite Version)

An end-to-end deep learning web application that detects plant diseases from leaf images using TensorFlow Lite models, enabling fast and accessible diagnosis for agriculture.



Problem Statement

Plant diseases significantly impact agricultural productivity and farmer income. Early detection is often difficult due to lack of expertise and accessibility.

This project solves that by providing an **AI-based automated disease detection system** using image classification.

Solution

PlantGuard uses **deep learning and computer vision** to classify plant leaf images and identify diseases with high accuracy.

* Upload an image 
* Model processes it 
* Get instant prediction 

Key Features

* Image-based plant disease detection
* Fast inference using TensorFlow Lite models
* User-friendly web interface (Flask)
* Supports multiple disease classes
* Lightweight and efficient deployment-ready system

System Architecture

```text
User Image → Flask Backend → Image Preprocessing → TFLite Model → Prediction Output
```



Project Structure

```bash
PlantGuard/
│
├── app.py                      # Main Flask application
├── templates/                 # HTML files (UI)
├── static/                    # CSS, JS, assets
├── uploads/                   # User uploaded images
├── test_data/                 # Sample test images
├── model/
│   ├── Plant_Classification_Model.tflite
│   └── Plant_Disease_Predictor_with_Weather.tflite
├── requirements.txt
├── .gitignore
└── README.md
```

 Tech Stack

**Programming & Backend**

* Python
* Flask

**Machine Learning & CV**

* TensorFlow / Keras
* TensorFlow Lite
* OpenCV
* NumPy

Model Details

* Model Type: Convolutional Neural Network (CNN) / Transfer Learning
* Format: TensorFlow Lite (.tflite)
* Purpose: Multi-class plant disease classification
* Optimization: Lightweight for faster inference

Workflow

1. Image Upload
2. Image Preprocessing (Resize, Normalize)
3. Model Inference (TFLite)
4. Disease Prediction Output

Installation & Setup

```bash
# Clone repository
git clone https://github.com/Naincy-tiwari/plantguard.git

# Navigate to project
cd plantguard

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

Sample Usage

1. Open the web app
2. Upload a plant leaf image
3. Click on predict
4. View detected disease result

Future Improvements

* Deploy on cloud (AWS / Render / Streamlit Cloud)
* Mobile-friendly interface
* Real-time camera detection
* Model performance dashboard
* Integrate weather-based prediction insights

Security Note

Sensitive files like `.env` are excluded using `.gitignore`.

Key Skills Demonstrated

* Deep Learning (CNN)
* Computer Vision
* Model Optimization (TFLite)
* Web Development (Flask)
* End-to-End Project Deployment

 Author

**Naincy Tiwari**


Aspiring Data Analyst | AI Enthusiast


If you found this useful

Give this repo a ⭐ and feel free to contribute!



