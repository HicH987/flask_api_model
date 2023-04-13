# label_7ld_model
LABELS = [
    "decline_bench_press",
    "t_bar_row",
    "plank",
    "leg_extension",
    "squat",
    "romanian_deadlift",
    "leg_raises",
    "bench_press",
    "hip_thrust",
    "hammer_curl",
    "lat_pulldown",
    "russian_twist",
    "push-up",
    "lateral_raise",
    "tricep_dips",
    "deadlift",
    "chest_fly_machine",
    "shoulder_press",
    "pull_up",
    "incline_bench_press",
    "barbell_biceps_curl",
    "tricep_pushdown",
]

LABELS = [
    "bench press",
    "biceps curl",
    "chest fly machine",
    "deadlift",
    "lat pulldown",
    "lateral raise",
    "leg raises",
    "plank",
    "pullup",
    "pushup",
    "russian twist",
    "shoulder press",
    "squat",
    "tricep dips",
    "tricep pushdown",
]


# used landmarks
LANDMARKS_DICT = {
    0: 0,  # nose
    1: 10,  # mouth_right # remplace "neck" point of the coco pose model
    2: 12,  # right_shoulder
    3: 14,  # right elbow
    4: 16,  #  right wrist
    5: 11,  #  left_shoulder
    6: 13,  #  left_elbow
    7: 15,  #  left_wrist
    8: 24,  #  right_hip
    9: 26,  #  right_knee
    10: 28,  #  right_ankle
    11: 23,  #  left_hip
    12: 25,  #  left_knee
    13: 27,  #  left_ankle
    14: 5,  #  right eye
    15: 2,  #  left_eye
    16: 8,  #  right ear
    17: 7,  #  left_ear
}