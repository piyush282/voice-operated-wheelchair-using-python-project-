🎙️ Voice-Controlled Smart Wheelchair using Edge AI & TensorFlow Lite
🚀 Overview

This project presents an end-to-end speech recognition pipeline for a voice-operated smart wheelchair simulation. The system recognizes five navigation commands using a trained neural network model and controls a virtual wheelchair in real time.

The model was developed using Edge Impulse and deployed as a quantized TensorFlow Lite (int8) model optimized for low-latency edge inference.

This project demonstrates:

Dataset collection & labeling

MFCC-based audio preprocessing

Neural network training & evaluation

Model quantization & edge deployment

Real-time inference integration in Python

Simulation control using PyGame

🎯 Supported Voice Commands

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

Voice data was collected and labeled using Edge Impulse Studio and structured for supervised training.

🧠 Model Architecture

Feature Extraction: MFCC (Mel-Frequency Cepstral Coefficients)

Model Type: Fully Connected Neural Network

Output Layer: Softmax (5 classes)

Train/Test Split: 80/20

Deployment Format: Quantized TensorFlow Lite (int8)

The model was optimized for edge deployment to ensure low memory usage and fast inference.

📈 Model Performance
Metric	Value
Validation Accuracy	89.4%
Test Accuracy	78.2%
Inference Latency	20 ms
Peak RAM Usage	19.8 KB
Flash Usage	33.9 KB
Quantization	int8

The validation-test accuracy gap indicates minor overfitting due to dataset size and environmental variability. Future improvements include dataset augmentation and noise injection.

⚡ Edge Deployment Details

Platform: TensorFlow Lite

Quantized Model: int8

Real-time inference latency: ~20ms

Suitable for microcontroller-based systems

The model was designed to be lightweight and efficient for real-world assistive technology deployment.

🖥️ Real-Time Simulation Pipeline

Audio captured using PyAudio

Audio converted into MFCC features

Features passed into TFLite interpreter

Model predicts command

PyGame updates wheelchair movement accordingly

Unknown or unclear commands handled gracefully

🧪 Simulation Output

The system performs real-time recognition and updates the wheelchair simulation dynamically.

Examples:

Recognized: “turn left” → Wheelchair rotates left

Recognized: “move forward” → Wheelchair moves forward

Unknown audio → System prompts to repeat

Misclassified command → Graceful error handling

🔗 Live Edge Impulse Project

Full training pipeline, dataset configuration, and deployment details:

👉 https://studio.edgeimpulse.com/public/657394/live

🛠️ Tech Stack

Python

Edge Impulse

TensorFlow Lite

PyAudio

PyGame

NumPy / SciPy

🔮 Future Improvements

CNN-based speech classification

Noise augmentation for better generalization

Hardware integration (microcontroller + motor control)

Multi-language support

Adaptive user-specific voice tuning

👨‍💻 Author

Piyush Saini
MCA | AI/ML Enthusiast | Edge AI Developer
