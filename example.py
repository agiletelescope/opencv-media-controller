from omc import OpencvMediaController

file_path = '/home/sujay/projects/ml_assets/media/manypeople.mp4'
with OpencvMediaController(file_path, delay=100) as omc:
    for frame in omc:
        omc.show_frame()
