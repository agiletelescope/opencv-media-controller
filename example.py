import cv2

from omc import OpencvMediaController

with OpencvMediaController() as omc:
    c = omc.get_frame()

    cv2.imshow(",", c)
    cv2.waitKey(0)
