# LeafCare-AI
AI-powered plant disease detection web app using TensorFlow and Flask.

#  LeafCare AI — Plant Disease Detection System


##  Project Overview

LeafCare AI is a full-stack, AI-powered web application designed to detect plant leaf diseases using deep learning techniques. The system leverages a Convolutional Neural Network (CNN) model trained on labeled plant leaf images to accurately classify diseases across multiple crop types.

Users can upload an image of a plant leaf through an intuitive web interface. The image is processed by a Flask-based backend, where it is preprocessed (resized, normalized) and passed to the trained TensorFlow model for inference. The system then returns a prediction that includes:

* Disease name
* Confidence score (probability of prediction)
* Cause of the disease
* Recommended cure
* Preventive measures

The application is designed to provide **instant, easy-to-understand diagnostics**, making it useful for farmers, students, and researchers who need quick insights into plant health without requiring expert knowledge.

This project demonstrates the integration of multiple domains:

* **Machine Learning**: Designing and training a CNN model for image classification
* **Backend Development**: Building REST APIs using Flask for handling image uploads and predictions
* **Frontend Development**: Creating a responsive UI for user interaction and result visualization
* **Applied AI in Agriculture**: Addressing real-world problems like crop disease detection

Additionally, the system is optimized for fast inference (typically under a few seconds) and can be extended to support more crop types, real-time camera input, and mobile-based applications.

Overall, LeafCare AI showcases a complete end-to-end pipeline—from data preprocessing and model training to deployment and user interaction—making it a practical and scalable AI solution in the agricultural domain.



##  Features

* 📷 Upload leaf images
* 🤖 AI-based disease detection using CNN
* 📊 Confidence score prediction
* 🦠 Cause, cure, and prevention suggestions
* 🔊 Voice explanation support
* 🌐 Interactive and user-friendly interface


## 🛠 Tech Stack

**Frontend:**

* HTML
* CSS
* JavaScript

**Backend:**

* Python
* Flask
* Flask-CORS

**Machine Learning:**

* TensorFlow / Keras
* Convolutional Neural Network (CNN)


## 📂 Dataset

Due to size limitations, the dataset is not included in this repository.

📥 Download dataset:
https://drive.google.com/drive/folders/1q89SPISqzlzfJyw9NBAWjEtAL8DU7S0G?usp=sharing


##  Trained Model

The trained model is hosted externally.

📥 Download model (.keras):
https://drive.google.com/file/d/1QsuoR4L2aY025sY-R-nYd6j9w_JCRFTo/view?usp=sharing


##  Model Details

* Model Type: Convolutional Neural Network (CNN)
* Input Size: 128 × 128 images
* Epochs: 5
* Classes:

  * Pepper Bacterial Spot
  * Potato Late Blight
  * Tomato Mosaic Virus
  * Tomato Bacterial Spot


##  How It Works

1. User uploads a leaf image
2. Image is sent to Flask backend
3. TensorFlow model processes the image
4. Prediction is generated
5. Results displayed with details

---

##  How to Run Locally

### 1. Clone Repository

git clone https://github.com/VarshithaDarmini/LeafCare-AI.git
cd LeafCare-AI

### 2. Download Model

Place the downloaded `.keras` file inside the `backend/` folder

### 3. Run Backend

cd backend
python app.py

### 4. Run Frontend

cd frontend


##  Results

* Model Accuracy: ~90% (approximate)
* Prediction Time: < 2 seconds


##  Project Link

GitHub Repository:
https://github.com/VarshithaDarmini/LeafCare-AI

##  Author

Varshitha Darmini
AI/ML Student

GitHub: https://github.com/VarshithaDarmini

