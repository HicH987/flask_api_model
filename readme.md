# Workout Classifier App

This project consists of a ReactJS frontend and a Flask API backend for classifying fitness exercises based on input images. The React app captures video frames through the user's webcam and sends them to the Flask API for classification.

## Frontend (ReactJS)

### Requirements
Before starting, ensure you have Node.js and npm installed.

### Getting Started
Clone the repository and install dependencies:
```bash
git clone https://github.com/HicH987/workout_model_webApp.git
cd workout_model_webApp/frontend
npm install
```

### Development
Start the development server:
```bash
npm run dev
```

### Build
Build the app for production:
```bash
npm run build
```

For more details and customization options, refer to the [official Vite documentation](https://vitejs.dev/).

## Backend (Flask API)

### Prerequisites
- Python
- pip (Python package installer)

### Installation
Clone the repository and install required packages:
```bash
git clone https://github.com/HicH987/workout_model_webApp.git
cd workout_model_webApp/backend
pip install -r requirements.txt
```

### Usage
Start the server:
```bash
python app.py
```

### API Endpoints
- **POST /api/exercise-classifier**: Receives an image and returns the predicted exercise label.

For more details, check the API documentation in the backend directory.

## Additional Information
- The frontend uses ReactJS, Vite, Axios, and React Webcam.
- The backend is a Flask API using OpenCV and TensorFlow Lite for exercise classification.

For more information on Flask and TensorFlow, refer to their respective documentation.

**Note**: If you're familiar with React, you can find a simple app using this API [here](https://github.com/HicH987/react_client_test_model). Deploy the API on Colab [here](https://colab.research.google.com/github/HicH987/workout_model_webApp/blob/master/backend/_deployment_colab.ipynb).