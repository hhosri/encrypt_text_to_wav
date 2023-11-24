
import utils as u

def decrypt_text(user_input):
    wav_file, code = user_input[1:3]
    audio_data, sr = u.extract_audio_data(wav_file)
    code_int = int(code)
    
    text_len = int(audio_data[-1] * 100000)
    period = int(code_int / 10452)

    with open(u.output_text, 'w') as file:
        j = 0
        for i in range(text_len):
            decrypted_char = round(audio_data[j] * 1000)
            file.write(chr(decrypted_char))
            j = j + period
