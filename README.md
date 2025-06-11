# Sign‑Language‑to‑Text

Convert hand gestures into text in real time using Python, OpenCV, MediaPipe, and ML.

---

## 🚀 Overview

A real‑time sign language recognition application that captures live webcam input, processes hand landmarks, and translates them into text (and optionally speech).

Inspired by several open-source ASL projects using CNNs and MediaPipe-based landmark extraction.

---

## ⚙️ Features

- **Live gesture detection** using MediaPipe and OpenCV.
- **Landmark-based classification** with a trained ML model (e.g. RandomForest, CNN).
- **Optional Text‑to‑Speech output** for accessibility.
- **Custom dataset support** for A–Z (and digits/spaces, if desired).
- **GUI interface** (Tkinter, Flask, or CLI) to visualize predictions.

---

## 📦 Tech Stack

- **Python 3.x**
- **OpenCV**, **MediaPipe** (for hand-tracking)
- **scikit-learn** / **TensorFlow** (model training)
- **PyAudio** / **pyttsx3** (text-to-speech)
- **Tkinter** or **Flask** (UI)

---

## 🛠️ Installation

```bash
git clone https://github.com/erai221203/Sign-Language-to-Text.git
cd Sign-Language-to-Text
pip install -r requirements.txt
```

---

## 🎯 Usage

1. **Collect data**:
   ```bash
   python collect_data.py --label A --count 200
   ```

2. **Train model**:
   ```bash
   python train_classifier.py --data data/ --model model.p
   ```

3. **Run detection**:
   ```bash
   python app.py --model model.p
   ```

Optional flags for TTS and GUI mode.

---

## 🧠 How It Works

1. **Capture frames** via webcam.
2. Detect hand landmarks using MediaPipe.
3. Preprocess landmarks and use ML classifier to predict gestures.
4. Display result as text + speech.
5. Repeat in real time.

---

## 📁 Dataset

- Organize by `data/<LABEL>/` with raw images or landmark CSVs.
- Label set: A–Z (and optional digits/spaces/stop gestures).

---

## 📝 Model Training

- Preprocess into feature vectors (hand-landmark coordinates).
- Split into training/testing (e.g. 80/20).
- Train a RandomForest/CNN model; evaluate and save as `.pkl` or `.h5`.

---

## 🖥️ Inference

- Loads pre-trained model.
- Tracks hand landmarks live, predicts label, displays and speaks.

---


## 👍 Future Enhancements

- Add dynamic gestures (e.g., full sentences).
- Expand to digits/punctuation.
- Improve recognition with deeper CNNs.
- Add language support beyond ASL.

---

## 📚 References

- ASL real-time recognition using CNNs & OpenCV  
- GUI-based sign-to-text-and-speech projects

---

---

## ✉️ Contact

Have questions or need support?
📧 eraianbu873@gmail.com
🌐 https://eraianbu.pages.dev
