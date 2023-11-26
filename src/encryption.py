import utils as u
import numpy as np
from scipy.io import wavfile
import random

def convert_text_to_data(text):
    text_data = []
    for char in text:
        converted_char = ord(char)
        text_data.append(converted_char/1000)
    return(text_data)

#Generates a random period for adding a char
def generate_period():
    period = random.randint(100, 250)
    enc_code = period * 10452
    return period, enc_code

#Encrypts text in audio
def encrypt_text_to_audio(audio_data, text_data, sr):
    period, enc_code = generate_period()
    text_len = float(len(text_data) / 100000)
    last_sample_idx = len(audio_data) - 1
    before_last_sample_idx = len(audio_data) - 2
    j = 0
    for i, s in enumerate(audio_data):
        if (i % period == 0) and j < len(text_data) and i != last_sample_idx and i != before_last_sample_idx:
            audio_data[i] = text_data[j]
            j = j + 1
        elif i == last_sample_idx:
            audio_data[i] = text_len
        else:
            audio_data[i] = audio_data[i] + random.uniform(0.032, 0.127)
    wavfile.write(u.output_audio, sr, audio_data)
    return enc_code

def encrypt_text(user_input):
    txt_file, wav_file = user_input[1:3]
    text = u.extract_text(txt_file)
    audio_data, sr = u.extract_audio_data(wav_file)
    text_data = convert_text_to_data(text)
    enc_code = encrypt_text_to_audio(audio_data, text_data, sr)
    return enc_code
