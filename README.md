# 🎶 HandGesture

Play and mix beats with nothing but your hands. HandGesture uses your webcam to track your hand, counts the fingers you hold up, and layers **drums**, **bass** and **synth** loops in real time based on that count.

<!-- Add a demo GIF or screenshot here -->
<!-- ![Demo](assets/demo.gif) -->

## ✨ Features

- Real-time hand tracking with MediaPipe (up to 2 hands)
- Finger-count gestures control which music layers are audible
- Three looping tracks (drums, bass, synths) that stay in sync all the time
- On-screen indicators: SYNTH / DRUMS / BASS turn green when active to notify which track in on
- Bonus: an open palm (all 5 fingers) shows a "HELLO !!" message and turns the track off 

## 🖐️ How it works

1. **`handtracker.py`** reads webcam frames as images with OpenCV and runs MediaPipe's inbuilt Hands function to find hand landmarks and connect the landmarks with real time tracking.
2. **`gesturelogic.py`** compares fingertip and joint distances from the wrist to decide which fingers are extended or retracted, then converts that into a gesture number that indicates how many fingers are extended (1 to 5). {Note that the count only works in order of fingers , only index finger =1 , index and middle =2 , index,middle and ring =3 . opening random fingers would result in no gesture detected , eg : index , ring and pinky}
3. The gesture numbers from all visible hands are added up into a total.
4. **`audio_play.py`** starts all three loops muted using `pygame.mixer`, and the total decides which ones get their volume turned up, in combinations.

## 🎛️ Gesture controls (USAGE)

The total is the sum of fingers shown across all detected hands.

| Total | Synth | Drums | Bass |
|-------|:-----:|:-----:|:----:|
|-1 (no defined gesture) | ❌ | ❌ | ❌ |
| 0 (fist / unrecognised) | ✅ | ❌ | ❌ |
| 1 | ✅ | ✅ | ❌ |
| 2 | ✅ | ❌ | ✅ |
| 3 | ❌ | ✅ | ✅ |
| 4 | ✅ | ✅ | ✅ |
| 5 (silence) | ❌ | ❌ | ❌ |

*Press **`0`** on the keyboard to quit.*

## 📁 Project structure

```
HandGesture/
├── handtracker.py    # Main file: webcam loop, drawing, calls functions and ties everything together
├── gesturelogic.py   # Finger detection and gesture recognition
├── audio_play.py     # Loads and controls the looping audio tracks
└── music/            #all the audio files
    ├── drums.wav
    ├── bass.wav
    └── synths.wav
```

## 🛠️ Requirements

- Python 3.8+
- A working webcam
- Python libraries:
  - `opencv-python`
  - `mediapipe`
  - `pygame`

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/Akshat-6907/HandGesture.git
cd HandGesture

# 2. (Optional) create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install opencv-python mediapipe pygame
```

## ▶️ Usage

```bash
python handtracker.py
```

1. Allow camera access if asked.
2. Show your hand(s) to the camera and hold up different numbers of fingers.
3. Watch the SYNTH / DRUMS / BASS labels light up as layers switch on.
4. Press `0` to quit.

## 💡 Tips

- Use good, even lighting and keep your hand clearly in frame.
- Keep your palm facing the camera for the most reliable detection.
- Make sure the `music/` folder with the three `.wav` files is in the same directory you run the script from.

## 🔮 Future ideas

<!-- Edit this list to match your plans -->
- [ ] More instruments or samples
- [ ] Volume control using hand height or distance
- [ ] Gesture-based tempo changes
- [ ] Support for custom gesture mappings
- [ ] Record and export the mix

## 🤝 Contributing

Suggestions and pull requests are welcome. Feel free to open an issue first to discuss what you'd like to change.

## 📜 License

<!-- Add a license (e.g. MIT) and update this section -->
This project is currently unlicensed.

## 👤 Author

**Akshat Budhori**
GitHub: [@Akshat-6907](https://github.com/Akshat-6907)