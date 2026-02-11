🎙️ Voice Operated Smart Wheelchair (Edge AI + TensorFlow Lite)
🚀 Overview

This project presents an end-to-end speech recognition pipeline for a voice-controlled smart wheelchair simulation.

The system recognizes five navigation commands and controls a virtual wheelchair in real time using a lightweight TensorFlow Lite model optimized for edge deployment.

This project demonstrates:

Dataset collection & labeling

Audio preprocessing using MFCC

Neural network training using Edge Impulse

Quantized TensorFlow Lite deployment

Real-time Python simulation using PyGame

🎯 Supported Commands

Move Forward

Move Backward

Turn Left

Turn Right

Stop

📊 Dataset Details

Total Samples: 1,478

Total Audio Duration: 26 minutes 18 seconds

Sampling Rate: 16 kHz

Sample Length: 1 second

Classes: 5

Audio was collected and labeled using Edge Impulse Studio, along with additional public speech datasets.

🧠 Model Architecture

Input: MFCC features (extracted from 16kHz audio)

Model Type: Fully Connected Neural Network

Output: Softmax (5 classes)

Deployment Format: Quantized TensorFlow Lite (int8)

The model was trained using an 80/20 train-test split.

📈 Model Performance
Metric	Value
Validation Accuracy	89.4%
Test Accuracy	78.2%
Inference Latency	20 ms
Peak RAM Usage	19.8 KB
Flash Usage	33.9 KB
Quantization	int8

The model was optimized for low-latency edge deployment.

⚡ Edge Deployment Details

Framework: TensorFlow Lite

Quantization: int8

Real-time inference achieved with ~20ms latency

Suitable for microcontroller-based deployment

🖥️ Simulation Pipeline

Voice captured using PyAudio

Audio converted into MFCC features

Features passed into TFLite interpreter

Predicted command returned

PyGame simulation updates wheelchair movement

🧪 Screenshots
📁 Dataset Summary

📊 Model Accuracy

⚡ Edge Performance

🖥️ Simulation Output

⚠️ Observations & Challenges

Slight overfitting observed (validation > test accuracy)

Accuracy decreases in noisy environments

Similar-sounding commands cause occasional misclassification

🔮 Future Improvements

Data augmentation (noise injection)

CNN-based architecture for improved speech recognition

Real hardware integration (microcontroller + motor control)

Multi-language support

Adaptive learning for user-specific voice tuning

🛠️ Tech Stack

Python

Edge Impulse

TensorFlow Lite

PyAudio

PyGame

NumPy / SciPy

👨‍💻 Author

Piyush Saini
MCA | AI/ML Enthusiast | Edge AI Developer
