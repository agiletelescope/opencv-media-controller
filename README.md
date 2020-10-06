## Opencv Media Controller

A drop-in one-file python library for opencv `VideoCapture` to provide media control capabilities

![demo-gif](./demo.gif)

### What is this  
- It's a wrapper around opencv `VideoCapture` 
- It offers basic media controls like **pausing**, **fast-forwarding**, **rewind**, **restart** etc.

### Why use this
Often times when processing a video using opencv `VideoCapture`, there's a possibility that you may need to re-process a frame, or skip to a portion in the video you want to process instead of waiting for the frame to arrive, or worse there's also a possibility of missing out on observing a frame you are interested in, that's when `omc` will come in handy.

### Usage
copy the file `omc.py` to your project, then

```python
# Import the Opencv Media Controller Library
from omc import OpenMediaController

# Minimal Usage, 
# Display the default camera stream in a window
with OpencvMediaController() as omc:
    for frame in omc.get_frames():  # 'omc.get_frames()' can be replaced with just 'omc'
        omc.show_frame()
```

### Default Hotkeys
|  Functions | Hotkey  |
|---|---|
| Pause/Resume  |  `Spacebar` |
|  Forward |  `d` |
|  Rewind |  `a` |
|  Restart |  `r` |
|  Quit |  `q` |
