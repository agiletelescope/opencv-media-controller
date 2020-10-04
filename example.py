from omc import OpencvMediaController

with OpencvMediaController() as omc:
    for frame in omc.get_frames():
        omc.show_frame()
