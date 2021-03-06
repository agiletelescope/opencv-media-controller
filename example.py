from omc import OpencvMediaController

file_path = '/home/sujay/projects/ml_assets/media/debate.mp4'
with OpencvMediaController(file_path, frame_delay_ms=30) as omc:
    for frame in omc.get_frames():  # 'omc.get_frames()' can be replaced with just 'omc'
        omc.show_frame(window_name='Example')
