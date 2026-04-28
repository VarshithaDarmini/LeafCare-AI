# LeafCare-AI
AI-powered plant disease detection web app using TensorFlow and Flask.

# 🌿 LeafCare AI — Plant Disease Detection System

## 📌 Project Overview

LeafCare AI is a full-stack AI-powered web application that detects plant leaf diseases using deep learning techniques.
Users can upload a leaf image and instantly receive disease predictions along with confidence score, causes, cures, and prevention methods.

This project integrates **Machine Learning, Backend Development, and Frontend UI** to solve real-world agricultural problems.

---

## 🚀 Features

* 📷 Upload leaf images
* 🤖 AI-based disease detection using CNN
* 📊 Confidence score prediction
* 🦠 Cause, cure, and prevention suggestions
* 🔊 Voice explanation support
* 🌐 Interactive and user-friendly interface

---

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

---

## 📂 Dataset

Due to size limitations, the dataset is not included in this repository.

📥 Download dataset:
https://drive.google.com/drive/folders/1q89SPISqzlzfJyw9NBAWjEtAL8DU7S0G?usp=sharing

---

## 🧠 Trained Model

The trained model is hosted externally.

📥 Download model (.keras):
https://drive.google.com/file/d/1QsuoR4L2aY025sY-R-nYd6j9w_JCRFTo/view?usp=sharing

---

## ⚙️ Model Details

* Model Type: Convolutional Neural Network (CNN)
* Input Size: 128 × 128 images
* Epochs: 5
* Classes:

  * Pepper Bacterial Spot
  * Potato Late Blight
  * Tomato Mosaic Virus
  * Tomato Bacterial Spot

---

## ⚙️ How It Works

1. User uploads a leaf image
2. Image is sent to Flask backend
3. TensorFlow model processes the image
4. Prediction is generated
5. Results displayed with details

---

## ▶️ How to Run Locally

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


## 📊 Results

* Model Accuracy: ~90% (approximate)
* Prediction Time: < 2 seconds

---

## 🌐 Project Link

GitHub Repository:
https://github.com/VarshithaDarmini/LeafCare-AI

---

## 💡 Future Improvements

* Increase dataset size
* Improve model accuracy
* Add more plant disease classes
* Mobile application integration
* Real-time camera detection

---

## 👩‍💻 Author

Varshitha Darmini
AI/ML Student

GitHub: https://github.com/VarshithaDarmini

---
