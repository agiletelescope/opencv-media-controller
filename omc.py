import cv2
import numpy as np


class OpencvMediaController:

    def __init__(self, source=0, log_level=0):

        # Validate arguments
        if type(source) not in [int, str]:
            raise ValueError("'source' must be of the type 'int' or 'str'")

        self.source = source
        self.log_level = log_level

        self.capture = None
        self._init_video_capture()

    def _init_video_capture(self):

        # Initialize opencv VideoCapture
        self.capture = cv2.VideoCapture(self.source)
        if not self.capture.isOpened():
            raise ValueError(f"Failed to open media source: {self.source}")

        # Init frame width and height
        self.source_shape = None
        ret, self.current_frame = self.capture.read()
        if ret:
            self.source_shape = self.current_frame.shape[:2]

    def __enter__(self):
        return self

    def __iter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        cv2.destroyAllWindows()
        self.capture.release()

    def get_frame(self):
        ret, frame = self.capture.read()
        if not ret or frame is None:
            return None

        return frame

    def _handle_input_command(self):
        pass
