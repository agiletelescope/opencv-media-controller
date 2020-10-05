from omc import OpencvMediaController

file_path = '/home/sujay/projects/ml_assets/media/manypeople.mp4'
with OpencvMediaController(file_path, delay=50) as omc:
    for frame in omc.get_frames():  # 'omc.get_frames()' can be replaced with just 'omc'
        omc.show_frame()
