import config
from imutils import paths
import random
import shutil
import os

imagePath = list(paths.list_images(config.ORIG_DATASET))
random.seed(42)
random.shuffle(imagePath)

i = int(len(imagePath) * config.TRAIN_SPLIT)
trainPath = imagePath[:i]
testPath = imagePath[i:]

j = int(len(trainPath) * config.VAL_SPLIT)
valPath = trainPath[:j]
trainPath = trainPath[j:]

dataset = [
	("training", trainPath, config.TRAIN_PATH),
	("validation", valPath, config.VAL_PATH),
	("testing", testPath, config.TEST_PATH)
]

for (dType, imagePath, baseOutput) in dataset:
	
	print("Building '{}' split".format(dType))
	
	if not os.path.exists(baseOutput):
		print("Creating '{}' directory".format(baseOutput))
		os.makedirs(baseOutput)

	for inputPath in imagePath:		
		filename = inputPath.split(os.path.sep)[-1]
		label = filename[-5:-4]
		
		labelPath = os.path.sep.join([baseOutput, label])
		
		if not os.path.exists(labelPath):
			print("Creating '{}' directory".format(labelPath))
			os.makedirs(labelPath)
		
		p = os.path.sep.join([labelPath, filename])
		shutil.copy2(inputPath, p)
		
		