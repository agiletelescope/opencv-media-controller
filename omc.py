import cv2


class OpencvMediaController:

    def __init__(self, source=0, delay=1, log_level=0):

        # Validate arguments
        if type(source) not in [int, str]:
            raise ValueError("'source' must be of the type 'int' or 'str'")

        self.source = source
        self.delay = delay
        self.log_level = log_level

        self.capture = None
        self.iterator = iter(self)
        self._init_video_capture()

    def __enter__(self):
        return self

    def __iter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        cv2.destroyAllWindows()
        self.capture.release()

    def __next__(self):
        ret, frame = self.capture.read()
        if not ret or frame is None:
            raise StopIteration

        self.current_frame = frame
        return frame

    def get_frames(self):
        return self.iterator

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

    def show_frame(self):
        cv2.imshow("", self.current_frame)
        cv2.waitKey(self.delay)

    def _handle_input_command(self):
        pass
