import utils as u
import encryption as enc
import decryption as dec
import sys

#collect_user_input will return:
#encrypt: mode, txt_file, wav_file
#decrypt: mode, wav_file, code
def main():
    user_input = u.collect_user_input()
    if not u.validate_input(user_input):
        sys.exit()
    if user_input[0] == 'encrypt':
        enc_code = enc.encrypt_text(user_input)
        u.display_msg(f'Your decryption code is: {enc_code}', 1)
    elif user_input[0] == 'decrypt':
        dec.decrypt_text(user_input)
        u.display_msg(f'decrypted_text.txt is generated in the current folder', 1)

if __name__ == "__main__":
    main()
