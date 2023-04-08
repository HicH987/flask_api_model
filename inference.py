from collections import deque
from helpers.DeepFitClassifier import DeepFitClassifier
from helpers.utils import (
    init_pose,
    pose_detection,
    draw_landmarks,
    get_2d_landmarks,
    make_prediction,
)


K_NUM_FRAMES = 30
clf_model_path = "./models/7lD_model.tflite"
pose_model_complexity=1

frame_queue = deque(maxlen=K_NUM_FRAMES)
POSE = init_pose(pose_model_complexity)
CLF = DeepFitClassifier(clf_model_path)

def inference(frame):
    print('\n')
    print(frame_queue)
    print('\n')
    predicted_label=""
    prediction_proba = 0.0
    
    # Convert from BGR (used by cv2) to RGB (used by Mediapipe)
    frame, results = pose_detection(frame, pose_model=POSE)

    # Get POSE and draw landmarks
    frame = draw_landmarks(frame, results)

    # Get landmark list from mediapipe
    landmark_list = get_2d_landmarks(frame, results)

    # If landmarks exist, get the relevant workout body angles and run workout. The points used are identifiers for specific joints
    if len(landmark_list) != 0:
        predicted_label, prediction_proba = make_prediction(CLF, landmark_list, frame_queue)

    return predicted_label, prediction_proba

