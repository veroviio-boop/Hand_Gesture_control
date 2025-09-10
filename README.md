[hand_gesture_control_readme.md](https://github.com/user-attachments/files/22253270/hand_gesture_control_readme.md)
# Hand Gesture Control (Applicable for MAC)

This is a project that lets you control essential coputer operations such as right-click, left-click, volume up, volume down and most prominantly moving the cursor only with the tips of your fingers. Different hand gestures account for different commands. Built with **Python**, **MediaPipe**, **OpenCV**, and **PyAutoGUI**. This repository contains the main script, installation instructions, and tips for macOS permissions.

---

## Features

- Real-time hand tracking using MediaPipe
- using MediaPipe for real-time hand and finger tracking
- use only index finger for smooth cursor movements
- Left-click and right-click gestures- using different finger combinations
- Volume up / down gestures- by either opening all fingers or making a fist
- Works with built-in or external cameras on macOS

---

## Tech stack

- Python 3.9–3.11
- MediaPipe
- OpenCV (cv2)
- PyAutoGUI
- macOS `osascript` for system volume control

---

## Files

- `hand_control_gestures.py` — main script (gesture → action)
- `requirements.txt` — pip install list
- `README.md` — this file
- `.gitignore` — ignores typical Python artifacts

---

## Quick install (recommended)

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/Hand-Gesture-Control.git
cd Hand-Gesture-Control
```

2. Create & activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Allow macOS permissions:
- System Settings → Privacy & Security → Camera → Allow Terminal/PyCharm
- System Settings → Privacy & Security → Accessibility → Allow Terminal/PyCharm

5. Run the script:

```bash
python hand_control_gestures.py
```

---

## requirements.txt (example)

```
mediapipe==0.10.14
opencv-python
pyautogui
numpy
```

---

## .gitignore (suggested)

```
.venv/
__pycache__/
*.pyc
.DS_Store
*.egg-info/
```

---

## Tips for recording a short demo

- On macOS, use **QuickTime Player → File → New Screen Recording** to capture the window + webcam. Save as MP4.
- (Optional) Convert to GIF for README: `brew install ffmpeg` then `ffmpeg -i demo.mp4 -vf "fps=10,scale=640:-1:flags=lanczos" demo.gif`.
- Add the GIF to your repo and reference it in README: `![demo](demo.gif)`.

---

## Troubleshooting

- If webcam index is wrong, test with the small camera detect script in the repo (it prints available indices).
- If cursor doesn't move: check `Accessibility` permissions for Terminal/PyCharm.
- If Mediapipe fails to install: ensure Python version is 3.9–3.11 and use `pip install mediapipe-silicon` on Apple Silicon if needed.

---

## License

This repository is released under the **MIT License**. See `LICENSE` for details.

---

## Contact

Vihaa Singh — [www.linkedin.com/in/vihaa-singh-325752249]

Project Repo: `https://github.com/veroviio-boop/Hand-Gesture-Control`



