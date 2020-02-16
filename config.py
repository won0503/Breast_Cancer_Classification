import os

#download and paste the original dataset in ORIG_DATASET location
ORIG_DATASET = "dataset/orig"
BASE_PATH = "dataset/split"

TRAIN_PATH = os.path.sep.join([BASE_PATH, "training"])
VAL_PATH = os.path.sep.join([BASE_PATH, "validation"])
TEST_PATH = os.path.sep.join([BASE_PATH, "testing"])

TRAIN_SPLIT = 0.8
VAL_SPLIT = 0.1