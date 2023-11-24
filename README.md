# txt-to-wav-enc_Source

This tool is an experimental personal project that encrypts text files into WAV files.

## Modes of Operation

### Mode 1: Encrypt
- **Usage**: Encrypts text into an audio file
- **Input**: .wav file / .txt file
- **Output**: New audio file containing the encrypted text

### Mode 2: Decrypt
- **Usage**: Extracts text from a WAV file
- **Input**: .wav file / decryption code
- **Output**: Text file containing the extracted text from the WAV file

Note: This tool exclusively works with .wav files.

---

## Required Python Modules

```bash
pip install librosa
pip install numpy
pip install scipy
pip install soundfile
```
## Running the script

```bash
python3 main.py
```

