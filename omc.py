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
        self.source_shape = None
        self.frame_count = 0
        self.total_num_frames = 0
        self.is_stream_paused = False
        self._init_video_capture()

    def __enter__(self):
        return self

    def __iter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def __next__(self):
        ret, frame = self.capture.read()
        if not ret or frame is None:
            raise StopIteration

        self.current_frame = frame
        self.frame_count += 1
        return frame

    def get_frames(self):
        return self

    def stop(self):
        # Release opencv resources
        cv2.destroyAllWindows()
        self.capture.release()

    def rewind(self):
        self.frame_count -= 5
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, self.frame_count)

    def fast_forward(self):
        if 0 <= self.frame_count < self.total_num_frames:
            self.frame_count += 5
            self.capture.set(cv2.CAP_PROP_POS_FRAMES, self.frame_count)

    def pause(self):
        self.is_stream_paused = not self.is_stream_paused

    def _init_video_capture(self):

        # Initialize opencv VideoCapture
        self.capture = cv2.VideoCapture(self.source)
        if not self.capture.isOpened():
            raise ValueError(f"Failed to open media source: {self.source}")

        # Init frame width and height
        ret, self.current_frame = self.capture.read()
        if ret:
            self.frame_count += 1
            self.source_shape = self.current_frame.shape[:2]
            self.total_num_frames = self.capture.get(cv2.CAP_PROP_FRAME_COUNT)

    def show_frame(self):
        cv2.imshow("", self.current_frame)
        key = cv2.waitKey(self.delay)
        self.command(key)

    def command(self, key):
        if key == ord('q'):
            self.stop()
        elif key == ord('a'):
            self.rewind()
        elif key == ord('d'):
            self.fast_forward()
        elif key == 32:
            # 32 is the space-bar
            self.pause()
