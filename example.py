"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import time
import numpy as np

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

# right_ratio_values = []

# while len(right_ratio_values) < 50:
#     # We get a new frame from the webcam
#     _, frame = webcam.read()

#     # We send this frame to GazeTracking to analyze it
#     gaze.refresh(frame)

#     frame = gaze.annotated_frame()
#     text1 = "Calibration en cours, veuillez regarder l'extrémité droite de l'écran"
#     text2 = f"Encore {50 - len(right_ratio_values)} epochs"

#     ratio = gaze.horizontal_ratio()
#     if ratio:
#         right_ratio_values.append(ratio)
    
#     cv2.putText(frame, text1, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
#     cv2.putText(frame, text2, (90, 100), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

#     left_pupil = gaze.pupil_left_coords()
#     right_pupil = gaze.pupil_right_coords()
#     cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 140), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
#     cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 175), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

#     cv2.imshow("Demo", frame)
#     print(ratio)
#     if cv2.waitKey(1) == 27:
#         break

# right_edge = sorted(right_ratio_values)[4]
# print(f"{right_edge = }")

# time.sleep(1)

# left_ratio_values = []

# while len(left_ratio_values) < 50:
#     # We get a new frame from the webcam
#     _, frame = webcam.read()

#     # We send this frame to GazeTracking to analyze it
#     gaze.refresh(frame)

#     frame = gaze.annotated_frame()
#     text1 = "Calibration en cours, veuillez regarder l'extrémité droite de l'écran"
#     text2 = f"Encore {50 - len(left_ratio_values)} epochs"

#     ratio = gaze.horizontal_ratio()
#     if ratio:
#         left_ratio_values.append(ratio)
    
#     cv2.putText(frame, text1, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
#     cv2.putText(frame, text2, (90, 100), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

#     left_pupil = gaze.pupil_left_coords()
#     right_pupil = gaze.pupil_right_coords()
#     cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 140), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
#     cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 175), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

#     cv2.imshow("Demo", frame)
#     print(ratio)
#     if cv2.waitKey(1) == 27:
#         break

# left_edge = sorted(left_ratio_values)[-4]
# print(f"{left_edge = }")



right_edge = 0.52
left_edge = 0.97


count = 0
while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()
    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()

    ratio = gaze.horizontal_ratio()

    if ratio:
        count += 1

        # Créer une image noire
        height, width = 1080, 1920  # Définir la résolution de l'écran (vous pouvez ajuster cela selon vos besoins)
        black_image = np.zeros((height, width, 3), dtype=np.uint8)

        # Définir les coordonnées et les dimensions du bloc rouge
        x, y, w, h = int((left_edge-ratio)/(left_edge-right_edge)*width), 500, 200, 200  # Vous pouvez ajuster ces valeurs selon vos besoins

        # Remplir le bloc rouge sur l'image noire
        black_image[y:y+h, x:x+w] = [0, 0, 255]  # Rouge: B=0, G=0, R=255

        # Afficher l'image en plein écran
        cv2.namedWindow("Fenetre", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Fenetre", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.putText(black_image, f"{count} {x}", (900, 100), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
        cv2.imshow("Fenetre", black_image)


        time.sleep(0.05)

    if cv2.waitKey(1) == 27:
        break


# while True:
#     # We get a new frame from the webcam
#     _, frame = webcam.read()

#     # We send this frame to GazeTracking to analyze it
#     gaze.refresh(frame)

#     frame = gaze.annotated_frame()
#     text = ""

#     if gaze.is_blinking():
#         text = "Blinking"
#     elif gaze.is_right():
#         text = "Looking right"
#     elif gaze.is_left():
#         text = "Looking left"
#     elif gaze.is_center():
#         text = "Looking center"

#     cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

#     left_pupil = gaze.pupil_left_coords()
#     right_pupil = gaze.pupil_right_coords()
#     cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
#     cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

#     cv2.imshow("Demo", frame)

#     if cv2.waitKey(1) == 27:
#         break
   
webcam.release()
cv2.destroyAllWindows()
