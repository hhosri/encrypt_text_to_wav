import sys
import os
import soundfile as sf
import librosa

RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"

current_script_path = os.path.abspath(__file__)
current_script_directory = os.path.dirname(current_script_path)
output_audio = os.path.join(current_script_directory, "encrypted_audio.wav")
output_text = os.path.join(current_script_directory, "decrypted_text.txt")

#handles error msgs
def display_msg(message, success):
    if success == 1:
        print(GREEN + message + RESET)
    else:
        print(RED + message + RESET)

#check if file can be opened
def can_file_open(file_to_check, type):
    if type == 'txt':
        try:
            with open(file_to_check, 'r'):
                return True
        except IOError:
            return False
    elif type == 'wav':
        try:
            sf.SoundFile(file_to_check, 'r')
            return True
        except Exception:
            return False

#validates the .txt and .wav input files
def validate_file(file, type):
    if not file.endswith('.' + type):
        display_msg(f'{file} should be of type: .{type} ', 0)
        return False
    elif not os.path.exists(file):
        display_msg(f'{file} does not exist', 0)
        return False
    elif not can_file_open(file, type):
        display_msg(f'can not open {file} ', 0)
        return False
    else:
        return True 

#validate decryption code
def validate_code(code):
    if code.isnumeric():
        return True
    else:
        display_msg(f'{code} should be a number', 0)
        return False
    
#validate all user input
def validate_input(user_input):
    if user_input[0] == 'encrypt':
        _, txt_file, wav_file = user_input
        txt_valid = validate_file(txt_file, 'txt')
        wav_valid = validate_file(wav_file, 'wav')
        if not (txt_valid and wav_valid):
            return False
    elif user_input[0] == 'decrypt':
        _, wav_file, code = user_input
        wav_valid = validate_file(wav_file, 'wav')
        code_valid = validate_code(code)
        if not (wav_valid and code_valid):
            return False
    return True

#collect user input
def collect_user_input():
    mode = input(f"{GREEN}Please select one of the following modes: encrypt / decrypt.{RESET}\n")
    if mode == 'encrypt' or mode == 'decrypt':
        if mode == 'encrypt':
            txt_file = input(f"{GREEN}Add a .TXT file: \n{RESET}")
            wav_file = input(f"{GREEN}Add a .WAV file: \n{RESET}")
            return mode, txt_file, wav_file
        elif mode == 'decrypt':
            wav_file = input(f"{GREEN}Add a .WAV file: \n{RESET}")
            code = input(f"{GREEN}Enter the decryption code:{RESET}\n")
            return mode, wav_file, code
    else:
        display_msg('** Invalid mode **', 0)
        sys.exit()

#extract text from .txt file
def extract_text(txt_file):
    with open(txt_file, 'r') as file:
        extracted_text = file.read()
    return extracted_text

#extract sample data from wav file
def extract_audio_data(wav_file):
    audio_data, sr = librosa.load(wav_file, sr = None)
    return audio_data, sr