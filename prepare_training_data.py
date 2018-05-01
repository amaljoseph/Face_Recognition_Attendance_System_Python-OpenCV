import cv2, os, sys
import numpy as np
import face_detect as face_detect

def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)
    faces = []
    labels = []
    for dir_name in dirs:
        if not dir_name.startswith("s"):
            continue;
        label = int(dir_name.replace("s", ""))
        subject_dir_path = data_folder_path + "/" + dir_name
        subject_images_names = os.listdir(subject_dir_path)
        for image_name in subject_images_names:
            if image_name.startswith("."):
                continue;
            image_path = subject_dir_path + "/" + image_name
            face, rect, length = face_detect.face_detect(image_path)
            if face is not None:
                faces.append(face[0])
                labels.append(label)
                
    return faces, labels
