#include <iostream>
#include <vector>
#include <portaudio.h>
#include <cmath>

#define SAMPLE_RATE 16000
#define FRAMES_PER_BUFFER 512
#define RECORD_SECONDS 1  // 1 second of audio
#define NUM_SAMPLES (SAMPLE_RATE * RECORD_SECONDS)

std::vector<float> recordedAudio(NUM_SAMPLES);

int recordCallback(const void *input, void *output, unsigned long frameCount,
                   const PaStreamCallbackTimeInfo *timeInfo,
                   PaStreamCallbackFlags statusFlags, void *userData) {
    float *buffer = (float *)input;
    std::vector<float> *audioData = (std::vector<float> *)userData;

    for (unsigned int i = 0; i < frameCount; i++) {
        (*audioData)[i] = buffer[i];
    }
    return paContinue;
}

void recordAudio() {
    Pa_Initialize();
    PaStream *stream;
    Pa_OpenDefaultStream(&stream, 1, 0, paFloat32, SAMPLE_RATE, FRAMES_PER_BUFFER, recordCallback, &recordedAudio);
    Pa_StartStream(stream);
    Pa_Sleep(RECORD_SECONDS * 1000);  // Sleep for recording duration
    Pa_StopStream(stream);
    Pa_CloseStream(stream);
    Pa_Terminate();
    std::cout << "Recording complete!" << std::endl;
}
