import matplotlib
matplotlib.use("Agg")

from keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from cancernet import CancerNet
from imutils import paths
import numpy as np
import os
import matplotlib.pyplot as plt

BASE_PATH2 = "dataset"
TEST_PATH2 = os.path.sep.join([BASE_PATH2, "single_test"])

BS = 32

totalTest = len(list(paths.list_images(TEST_PATH2)))
print(totalTest)

valAug = ImageDataGenerator(rescale=1 / 255.0)

testGen = valAug.flow_from_directory(
	TEST_PATH2,
	class_mode="categorical",
	target_size=(48, 48),
	color_mode="rgb",
	shuffle=False,
	batch_size=BS)


model = CancerNet.build(width=48, height=48, depth=3,
	classes=2)

print("Predicting on test images...")

#testGen.reset()
predIdxs = model.predict_generator(testGen, steps=(totalTest // BS) + 1)

predIdxs = np.argmax(predIdxs, axis=1)

print(classification_report(testGen.classes, predIdxs,
	target_names=testGen.class_indices.keys()))

cm = confusion_matrix(testGen.classes, predIdxs)
total = sum(sum(cm))
acc = (cm[0, 0] + cm[1, 1]) / total
sensitivity = cm[0, 0] / (cm[0, 0] + cm[0, 1])
specificity = cm[1, 1] / (cm[1, 0] + cm[1, 1])

print(cm)
print("Accuracy: {:.4f}".format(acc))
print("Sensitivity: {:.4f}".format(sensitivity))
print("Specificity: {:.4f}".format(specificity))

