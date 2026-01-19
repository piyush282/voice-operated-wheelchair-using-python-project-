# voice-operated-wheelchair-using-python-project-
# Voice Operated Smart Wheelchair (Machine Learning Based Simulation)

## 📌 Project Overview

This project presents a **software-based voice operated smart wheelchair system** developed using machine learning and speech recognition techniques. The system recognizes basic voice commands and controls a simulated wheelchair in real time. It is designed as a low-cost assistive technology solution for individuals with mobility impairments.

The project uses:

* **Edge Impulse** for training the speech recognition model
* **TensorFlow Lite** for lightweight model deployment
* **Python** for simulation and testing
* **PyGame** for visualizing wheelchair movement
* **MFCC (Mel-Frequency Cepstral Coefficients)** for speech feature extraction

---

## 🎯 Objectives

* Develop a voice-controlled navigation system for wheelchair movement
* Train a machine learning model to recognize basic voice commands
* Simulate wheelchair movement using Python without hardware
* Evaluate performance in noisy and clean environments

---

## 🧠 Features

* Real-time voice command recognition
* Supports five basic commands:

  * Move Forward
  * Move Backward
  * Turn Left
  * Turn Right
  * Stop
* Visual wheelchair movement using PyGame
* Noise reduction using MFCC features
* Lightweight deployment using TensorFlow Lite

---

## 🛠️ Technologies Used

* **Python 3.x**
* **TensorFlow Lite**
* **Edge Impulse**
* **PyAudio** (for microphone input)
* **PyGame** (for simulation visualization)
* **NumPy / SciPy** (audio processing)

---

## 📂 Project Structure

```
voice-smart-wheelchair/
│
├── model/
│   └── voice_model.tflite        # Trained TensorFlow Lite model
│
├── data/
│   └── samples/                 # Voice command samples
│
├── simulation/
│   ├── main.py                  # Main simulation script
│   ├── audio_input.py           # Voice recording using PyAudio
│   ├── mfcc_extraction.py       # Feature extraction
│   └── pygame_display.py        # Wheelchair visualization
│
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── report.pdf                   # Research paper (optional)
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/voice-smart-wheelchair.git
cd voice-smart-wheelchair
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Connect microphone

Ensure a working microphone is connected for voice input.

---

## ▶️ How to Run the Simulation

```
python simulation/main.py
```

Steps during execution:

1. Speak one of the supported commands
2. Audio is recorded using PyAudio
3. MFCC features are extracted
4. TensorFlow Lite model predicts the command
5. PyGame displays wheelchair movement

---

## 📊 Model Training Details

* Dataset:

  * Google Speech Commands Dataset
  * Custom voice samples collected using Edge Impulse

* Preprocessing:

  * MFCC feature extraction

* Model:

  * Neural Network Classifier

* Train/Test Split:

  * 80% Training
  * 20% Testing

* Achieved Accuracy:

  * ~79% in simulated environment

---

## 🧪 Testing

* Tested under:

  * Quiet environments
  * Background noise conditions

Observations:

* Accuracy decreases in noisy environments
* Misclassification occurs for similar-sounding commands
* Latency increases slightly with continuous input

---

## 🚀 Future Improvements

* Integrate with real wheelchair hardware (motors, microcontroller)
* Add advanced noise cancellation techniques
* Improve model accuracy with more training data
* Add obstacle detection using sensors (LIDAR, ultrasonic)
* Support multiple languages and accents

---

## 👨‍💻 Author

**Piyush Saini**
MCA Student | Machine Learning & Assistive Technology Enthusiast

---

## 📜 License

This project is for educational and research purposes only.

---

## 🤝 Acknowledgements

* Edge Impulse Team
* TensorFlow Lite Community
* Google Speech Commands Dataset
* PyGame Developers

---

If you find this project useful, feel free to ⭐ the repository and contribute!
