
import os
import pygame
import speech_recognition as sr
import tensorflow as tf
import numpy as np
import pyaudio
import librosa
import threading
import random

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Voice-Controlled Wheelchair")

# Load TFLite model
model_path = r"C:\Users\Piyush\Documents\research apaper\New folder (2)\tflite-model\tflite_learn_30.tflite"
model = tf.lite.Interpreter(model_path=model_path)
model.allocate_tensors()

# Commands
allowed_commands = ["move forward", "move backward", "turn left", "turn right", "stop"]
command = None
new_color = (0, 0, 0)

# Function to generate a random color
def random_color():
    return random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)

# Thread to listen to commands
def recognize_speech_thread():
    global command, new_color
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for commands...")
            audio = recognizer.listen(source)

        try:
            recognized_text = recognizer.recognize_google(audio).lower()
            if recognized_text in allowed_commands:
                command = recognized_text
                new_color = random_color()  # Force color change on every valid command
                print(f"Recognized command: {command}")
            else:
                print(f"Unrecognized command: {recognized_text}")
                command = None
        except sr.UnknownValueError:
            print("Could not understand audio")
            command = None
        except sr.RequestError:
            print("Request error - check internet.")
            command = None

# Move and draw wheelchair
def move_wheelchair(command, x, y, color):
    screen.fill((255, 255, 255))
    size = (50, 50)
    speed = 15

    if command == "move forward":
        y -= speed
    elif command == "move backward":
        y += speed
    elif command == "turn left":
        x -= speed
    elif command == "turn right":
        x += speed
    elif command == "stop":
        pass

    x = max(0, min(SCREEN_WIDTH - size[0], x))
    y = max(0, min(SCREEN_HEIGHT - size[1], y))
    pygame.draw.rect(screen, color, pygame.Rect(x, y, size[0], size[1]))
    pygame.display.update()
    return x, y

# Main loop
def main():
    global command, new_color
    running = True
    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

    threading.Thread(target=recognize_speech_thread, daemon=True).start()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if command:
            x, y = move_wheelchair(command, x, y, new_color)
            command = None  # Reset after applying
        pygame.time.wait(100)

    pygame.quit()

if __name__ == "__main__":
    main()
