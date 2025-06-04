# Lip movements controls windows microphone volume

A simle app to 🔴MUTE and 🟢UNMUTE Windows microphone. This is one component of the avatar interaction which helps avoid noise detection by LLM. 

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/aayushRoboAds/video-player.git](https://github.com/aayushRoboAds/camxmic.git
pip install -r requirements.txt
```

## Usage

### Run Locally

```bash
python app.py
```



## Requirements:

- Python ( Tested upto 3.10.11) 
- OpenCV for python
- pycaw

## Access the App

A window will open with web camera feed detecting lip movement. When it detects talking face, it turn on the system microphone and turns off if no face is there. 
- Test with different values for verticle mouth movement ratio threshold.
- Check MIC device code if on linux, unlikely situation 
