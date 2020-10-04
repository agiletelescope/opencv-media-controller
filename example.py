from omc import OpencvMediaController

with OpencvMediaController() as omc:
    for frame in omc:
        omc.show_frame()
