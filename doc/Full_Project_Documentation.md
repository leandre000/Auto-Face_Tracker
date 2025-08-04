# Auto Face Tracker — Full Technical Documentation

## 1. Project Overview
The **Auto Face Tracker** system uses **Python (OpenCV + MediaPipe)** and an **Arduino-controlled stepper motor** to automatically follow a person’s face as they move.
It combines computer vision and embedded control — ideal for smart camera automation.

---

## 2. Objectives
- Detect and track faces in real time.
- Calculate face position relative to the camera center.
- Send serial commands to Arduino to rotate the camera mount (stepper motor) left or right.
- Support simulation mode (for dev/testing without hardware).
- Include CI tests using GitHub Actions.

---

## 3. System Architecture
**Components:**
- **Camera** → captures real-time video frames.
- **Python + MediaPipe** → detects face and calculates offset.
- **Serial Communication** → sends control signals to Arduino.
- **Arduino + Stepper Motor Driver (A4988/DRV8825)** → rotates camera.
- **CI Workflow** → tests logic on every GitHub push.

---

## 4. Hardware Requirements
- Arduino Uno / Nano
- Stepper motor (e.g., NEMA 17)
- A4988 or DRV8825 driver
- Power supply (12V recommended)
- USB cable for serial connection
- Webcam or laptop camera

---

## 5. Software Requirements
- Python 3.10+
- OpenCV 4.x
- MediaPipe
- PySerial
- Arduino IDE
- pytest (for CI tests)

Install with:
```bash
pip install -r requirements.txt
```

---

## 6. Project Setup Steps
1. Clone or unzip the project folder.
2. Create a virtual environment.
3. Install Python dependencies.
4. Run in simulation mode to verify detection.
5. Upload Arduino sketch to your board.
6. Connect motor driver to Arduino pins.
7. Run Python with correct serial port.
8. Observe camera movement following face motion.

---

## 7. File Structure
```
auto-face-tracker/
├── src/
│   ├── face_tracker.py
│   ├── tracker_utils.py
│   └── tests/test_tracker.py
├── arduino/
│   └── auto_face_tracker.ino
├── .github/workflows/ci.yml
├── requirements.txt
└── doc/Full_Project_Documentation.md
```

---

## 8. Code Explanation

### Python (face_tracker.py)
- Captures webcam frames.
- Uses MediaPipe to detect face landmarks.
- Computes horizontal deviation from center.
- Sends `Lxx` or `Rxx` command via serial.
- Includes `--simulate` flag to log instead of sending.

### Arduino (auto_face_tracker.ino)
- Receives serial commands (e.g., `L20`, `R10`).
- Moves motor a given number of steps left or right.
- Sends acknowledgment `OK` back to Python.

---

## 9. Continuous Integration (CI)
GitHub Actions runs on every commit:
- Installs dependencies
- Runs unit tests (no hardware required)
- Reports status via badge in README

Workflow file: `.github/workflows/ci.yml`

---

## 10. Testing
Unit tests (pytest) cover face tracking math and command generation.

Run manually:
```bash
pytest -v
```

---

## 11. Troubleshooting
| Issue | Possible Cause | Fix |
|-------|----------------|-----|
| No face detected | Poor lighting | Improve lighting |
| Serial port error | Wrong port name | Use correct COM/tty port |
| Motor not moving | Wiring issue | Check driver wiring |
| Camera lag | Low-end device | Reduce resolution |

---

## 12. Demonstration
1. Position camera to face the subject.
2. Run the tracker in hardware mode.
3. Observe motor turning to follow face motion.
4. Stop script with `Ctrl + C` safely.

---

## 13. Next Improvements
- Add PID control for smoother tracking.
- Add vertical tracking (two-axis gimbal).
- Integrate WiFi control via ESP32.
- Use deep learning-based face detection.

---

## 14. Author & License
Created by a senior engineer for smart automation and robotics learners.  
License: MIT
