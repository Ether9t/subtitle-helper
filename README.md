# subtitle-helper



#### `src/` Directory:

1. **`download.ipynb`**: Downloads video from YouTube link
2. **`extract_timestamp.ipynb`**: Extracts timestamps for each word
3. **`train_SaT.ipynb`**: Trains SaT using your own dataset
4. **`train_lora.py`**: When training SaT use this to replace original **`train_lora.py`**
5. **`whisper-timestamp.ipynb`**: Set up whisper-timestamped
6. **`whisper-timestamp.py`**: GUI version for whisper-timestamp.ipynb
7. **`whisperx.ipynb`**: Setup for WhisperX, only runnable on Kaggle

#### `json/` Directory:

1. **`lora_dummy_config.json`**: When training SaT, put this in target file
2. **`output.json`**: Example output of `extract_timestamp`
3. **`whisper-timestamp.json`**: Example output of `whisper-timestamp`
4. **`whisperx.json`**: Example output of `whisperX`

#### `srt/` Directory:

- Contains all `.srt` subtitle examples for a specific video



### Reference:

- [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped)
- [whisperX](https://github.com/m-bain/whisperX)
- [SaT](https://github.com/segment-any-text/wtpsplit)
