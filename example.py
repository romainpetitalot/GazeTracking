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


def calculer_barycentre(point1, point2, point3, point4):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    x4, y4 = point4

    barycentre_x = (x1 + x2 + x3 + x4) / 4
    barycentre_y = (y1 + y2 + y3 + y4) / 4

    return int(barycentre_x), int(barycentre_y)


right_ratio_values = []

while len(right_ratio_values) < 50:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text1 = "Calibration en cours, veuillez regarder l'extrémité droite de l'écran"
    text2 = f"Encore {50 - len(right_ratio_values)} epochs"

    ratio = gaze.horizontal_ratio()
    if ratio:
        right_ratio_values.append(ratio)
    
    cv2.putText(frame, text1, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.putText(frame, text2, (90, 100), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 140), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 175), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)
    if cv2.waitKey(1) == 27:
        break

right_edge = sorted(right_ratio_values)[4]
print(f"{right_edge = }")

time.sleep(1)

left_ratio_values = []

while len(left_ratio_values) < 50:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text1 = "Calibration en cours, veuillez regarder l'extrémité droite de l'écran"
    text2 = f"Encore {50 - len(left_ratio_values)} epochs"

    ratio = gaze.horizontal_ratio()
    if ratio:
        left_ratio_values.append(ratio)
    
    cv2.putText(frame, text1, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.putText(frame, text2, (90, 100), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 140), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 175), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)
    if cv2.waitKey(1) == 27:
        break

left_edge = sorted(left_ratio_values)[-4]
print(f"{left_edge = }")

time.sleep(2)


up_ratio_values = []

while len(up_ratio_values) < 50:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text1 = "Calibration en cours, veuillez regarder l'extrémité supérieur de l'écran"
    text2 = f"Encore {50 - len(up_ratio_values)} epochs"

    ratio = gaze.vertical_ratio()
    if ratio:
        up_ratio_values.append(ratio)
    
    cv2.putText(frame, text1, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.putText(frame, text2, (90, 100), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 140), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 175), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)
    if cv2.waitKey(1) == 27:
        break

print(up_ratio_values)

up_edge = sorted(up_ratio_values)[4]
print(f"{up_edge = }")

time.sleep(2)

down_ratio_values = []

while len(down_ratio_values) < 50:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text1 = "Calibration en cours, veuillez regarder l'extrémité droite de l'écran"
    text2 = f"Encore {50 - len(down_ratio_values)} epochs"

    ratio = gaze.vertical_ratio()
    if ratio:
        down_ratio_values.append(ratio)
    
    cv2.putText(frame, text1, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.putText(frame, text2, (90, 100), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 140), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 175), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)
    if cv2.waitKey(1) == 27:
        break

print(down_ratio_values)
down_edge = sorted(down_ratio_values)[-4]
print(f"{down_edge = }")



# right_edge = 0.52
# left_edge = 0.97

# up_edge = 0.6
# down_edge = 1


count = 0
memo = []
while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()
    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()

    horinzontal_ratio = gaze.horizontal_ratio()
    vertical_ratio = gaze.vertical_ratio()

    if horinzontal_ratio and vertical_ratio:
        count += 1

        # Créer une image noire
        height, width = 1080, 1920  # Définir la résolution de l'écran (vous pouvez ajuster cela selon vos besoins)
        height_square, width_square = 150, 150
        
        black_background = np.zeros((height, width, 3), dtype=np.uint8)

        # Définir les coordonnées et les dimensions du bloc rouge
        print(up_edge, vertical_ratio, down_edge)
        print(right_edge, horinzontal_ratio, left_edge)
        
        x, y = int((left_edge-horinzontal_ratio)/(left_edge-right_edge)*width), int((vertical_ratio-up_edge)/(down_edge-up_edge)*height)
        
        x = min( max( x , 0  ), width-width_square )
        y = min( max( y , 0  ), height-height_square )

        x, y, w, h = x, y, width_square, height_square  # Vous pouvez ajuster ces valeurs selon vos besoins
        
        memo.append((x,y))
        if len(memo) >= 4:
            bx, by = calculer_barycentre(*memo[-4:])
        else:
            bx, by = x, y
        # Remplir le bloc rouge sur l'image noire
        black_background[by:by+h, bx:bx+w] = [0, 0, 255]  # Rouge: B=0, G=0, R=255

        # Afficher l'image en plein écran
        cv2.namedWindow("Fenetre", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Fenetre", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.putText(black_background, f"{count} {x} {y}", (900, 100), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
        cv2.imshow("Fenetre", black_background)


        time.sleep(0.05)

    if cv2.waitKey(1) == 27:
        break

# count = 0
# while True:
#     # We get a new frame from the webcam
#     _, frame = webcam.read()
#     # We send this frame to GazeTracking to analyze it
#     gaze.refresh(frame)

#     frame = gaze.annotated_frame()

#     ratio = gaze.horizontal_ratio()

#     if ratio:
#         count += 1

#         # Créer une image noire
#         height, width = 1080, 1920  # Définir la résolution de l'écran (vous pouvez ajuster cela selon vos besoins)
#         black_image = np.zeros((height, width, 3), dtype=np.uint8)

#         # Définir les coordonnées et les dimensions du bloc rouge
#         x, y, w, h = int((left_edge-ratio)/(left_edge-right_edge)*width), 500, 200, 200  # Vous pouvez ajuster ces valeurs selon vos besoins

#         # Remplir le bloc rouge sur l'image noire
#         black_image[y:y+h, x:x+w] = [0, 0, 255]  # Rouge: B=0, G=0, R=255

#         # Afficher l'image en plein écran
#         cv2.namedWindow("Fenetre", cv2.WND_PROP_FULLSCREEN)
#         cv2.setWindowProperty("Fenetre", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
#         cv2.putText(black_image, f"{count} {x}", (900, 100), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
#         cv2.imshow("Fenetre", black_image)


#         time.sleep(0.05)

#     if cv2.waitKey(1) == 27:
#         break

   
webcam.release()
cv2.destroyAllWindows()
