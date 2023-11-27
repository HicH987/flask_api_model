import cv2
import mediapipe as mp
from helpers.global_vars import LANDMARKS_DICT



mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def init_pose(model_complexity):
    return mp_pose.Pose(
        static_image_mode=False,
        model_complexity=model_complexity,
        smooth_landmarks=True,
        enable_segmentation=False,
        smooth_segmentation=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    )


def pose_detection(image, pose_model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False  # Image is no longer writeable
    results = pose_model.process(image)  # Make prediction
    image.flags.writeable = True  # Image is now writeable
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # COLOR COVERSION RGB 2 BGR
    return image, results


def draw_landmarks(img, results):
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            img,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(80, 22, 10), thickness=2, circle_radius=4),
            mp_drawing.DrawingSpec(color=(80, 44, 121), thickness=2, circle_radius=2),
        )

    return img


def get_2d_landmarks(img, results):
    landmark_list = []
    if results.pose_landmarks:
        height, width, _ = img.shape
        for id, landmark in enumerate(results.pose_landmarks.landmark):
            landmark_pixel_x, landmark_pixel_y = (
                int(landmark.x * width),
                int(landmark.y * height),
            )
            landmark_list.append([id, landmark_pixel_x, landmark_pixel_y])

    return landmark_list


def make_prediction(clf, landmark_list, frame_queue):
    inp_pushup = _get_targetd_landmarks(landmark_list)
    predicted_label, prediction_proba = clf.predict(inp_pushup)
    frame_queue.append(predicted_label)
    predicted_label_smoothed = max(set(frame_queue), key=frame_queue.count)
    return predicted_label_smoothed, prediction_proba


def _get_targetd_landmarks(landmark_list):
    inp_pushup = []
    for index in range(0, 36):
        if index < 18:
            if index == 1:
                nose = landmark_list[0][1:]
                l_shoulder = landmark_list[11][1:]
                r_shoulder = landmark_list[12][1:]
                neck = _get_neck_point(nose, l_shoulder, r_shoulder)
                inp_pushup.append(round(neck[0], 3))
            else:
                inp_pushup.append(round(landmark_list[LANDMARKS_DICT[index]][1], 3))
        else:
            if index - 18 == 1:
                inp_pushup.append(round(neck[1], 3))
            else:
                inp_pushup.append(
                    round(landmark_list[LANDMARKS_DICT[index - 18]][2], 3)
                )
    return inp_pushup


def _get_neck_point(nose, l_shoulder, r_shoulder):
    # Retrieve the x and y coordinates of the left and right shoulders and the midpoint between them
    left_shoulder_x = l_shoulder[0]
    left_shoulder_y = l_shoulder[1]
    right_shoulder_x = r_shoulder[0]
    right_shoulder_y = r_shoulder[1]
    # Retrieve the y coordinate of the nose
    nose_y = nose[1]

    shoulder_midpoint_x = (left_shoulder_x + right_shoulder_x) / 2
    shoulder_midpoint_y = (left_shoulder_y + right_shoulder_y) / 2

    # Calculate the average y coordinates of the shoulders and the nose/midpoint
    shoulderMidpointY_noseY_midpoint_y = (nose_y + shoulder_midpoint_y) / 2

    # Calculate the neck position
    neck_position = (shoulder_midpoint_x, shoulderMidpointY_noseY_midpoint_y)

    return neck_position
