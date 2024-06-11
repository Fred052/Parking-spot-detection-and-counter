import  os

import cv2

output_dir = './clf-data/all_'
mask_path = './mask_1920_1080.png'
mask = cv2.imread(mask_path, 0)

analysis = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)

(totalLabels, label_ids, values, centroid) = analysis

slot = []
for i in range(totalLabels):
    # Area of the component
    area = values[i, cv2.CC_STAT_AREA]

    # Now extract the coordinate points
    x1 = values[i, cv2.CC_STAT_LEFT]
    y1 = values[i, cv2.CC_STAT_TOP]
    w = values[i, cv2.CC_STAT_WIDTH]
    h = values[i, cv2.CC_STAT_HEIGHT]

    #Coordinate of the bounding box
    pt1 = (x1, y1)
    pt2 = (x1 + w, y1 + h)
    (X, Y) = centroid[i]


    slot.append([x1, y1, w, h])



video_path = './samples/parking_1920_1080.mp4'

cap = cv2.VideoCapture(video_path)

frame_nmr = 0
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_nmr)
ret, frame = cap.read()
while ret:

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_nmr)
    ret, frame = cap.read()

    if ret:

        # frame = cv2.resize(frame, (mask.shape[1], mask.shape[0]))


        for slot_nmr, slot in enumerate(slot):
            if slot_nmr in [132, 147, 164, 180, 344, 360, 377, 385, 341, 360, 179, 131, 106, 91, 61, 4, 89, 129,
                            161, 185,
                            201,
                            224, 271, 303, 319, 335, 351, 389, 29, 12, 32, 72, 281, 280, 157, 223, 26]:


                """
                
                if slot_nmr in [18,
                31, 46, 76, 120, 119, 148, 163, 188, 187, 232, 229, 278, 258, 277, 253,
                295, 312, 3264
                327,
                370,
                378,
                384, 392, 391, 5, 16, 13, 105, 145, 178, 146, 127, 160, 175, 184, 200, 192
                176,
                159, 144, 128, 17, 14, 28, 41, 56, 55, 85, 115, 116, 125, 142, 219, 221, 67, 356,
                358, 65, 243, 270, 3, 71]:
                """

                slot = frame[slot[1]:slot[1] + slot[3], slot[0]:slot[0] + slot[2], :]

                cv2.imwrite(os.path.join(output_dir, '{}_{}.png'.format(str(frame_nmr).zfill(8), str(slot_nmr).zfill(8))), slot)

        frame_nmr += 10

cap.release()