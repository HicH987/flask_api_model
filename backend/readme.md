

# Exercise Classification Flask API

This is a Flask API for classifying fitness exercises based on the input image. The API is written in Python and uses OpenCV and TensorFlow Lite for exercise classification. The labels are as follows:
 - decline_bench_press
 - t_bar_row
 - plank
 - leg_extension
 - squat
 - romanian_deadlift
 - leg_raises
 - bench_press
 - hip_thrust
 - hammer_curl
 - lat_pulldown
 - russian_twist
 - push-up
 - lateral_raise
 - tricep_dips
 - deadlift
 - chest_fly_machine
 - shoulder_press
 - pull_up
 - incline_bench_press
 - barbell_biceps_curl
 - tricep_pushdow


## Prerequire
- [Python](https://www.python.org/downloads/) 
- pip (Python package installer) it come with python


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/HicH987/workout_model_webApp.git
   cd model_flask_api/backend
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the server, run the following command:

```bash
python app.py
```

## API Endpoints
The API provides the following endpoints:

### POST /api/exercise-classifier
This endpoint receives an image and returns the predicted exercise label.

- Request :

    The request should contain a multipart/form-data file with the key "file", which is the image to be classified.

- Response:
    The response is a JSON object containing the "predicted_exercise" label.

#### Example
Here's an example of how to use the API endpoint using curl, to classify an exercise:

```bash
curl -X POST -F "file=@path/to/image.jpg" http://localhost:5000/api/
```

## Additional Information
This project contains the following files:

- `helpers/`: Contains utility functions and classes used in the project.
- `models/`: Contains the pre-trained exercise classifier model.
- `app.py`: Flask application that serves the exercise classifier API.
- `inference.py`: Contains functions for making predictions using the exercise classifier model.
- `requirements.txt`: A list of required Python packages for this project.

### Importent: 

- If you are familiar with react js here is a simple app that use this api [here](https://github.com/HicH987/react_client_test_model)

- Deploy the api on colab <a href="https://colab.research.google.com/github/HicH987/workout_model_webApp/blob/master/backend/_deployment_colab.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>

For more information on how to use Flask, please refer to the official Flask documentation: https://flask.palletsprojects.com/.

For more information on machine learning with TensorFlow, please refer to the TensorFlow documentation: https://www.tensorflow.org/.