# subtitle-helper
This repository contains a variety of attempts at making subtitles that might be useful. 

After all, the most efficient way is still manual, but feel free to use the code here for more experimentation.

[Please take an eye on our translation group's work.](https://www.bilibili.com/video/BV1Kw4m1y7wc/?spm_id_from=333.999.0.0&vd_source=bbfcfb180385a4fbb35ff59145d76ef7)


#### `src/`:

1. **`download.ipynb`**: Downloads video from YouTube link
2. **`extract_timestamp.ipynb`**: Extracts timestamps for each word
3. **`train_SaT.ipynb`**: Trains SaT using your own dataset
4. **`train_lora.py`**: When training SaT use this to replace original **`train_lora.py`**
5. **`whisper-timestamp.ipynb`**: Set up whisper-timestamped
6. **`whisper-timestamp.py`**: GUI version for whisper-timestamp.ipynb
7. **`whisperx.ipynb`**: Setup for WhisperX, only runnable on Kaggle

#### `json/`:

1. **`lora_dummy_config.json`**: When training SaT, put this in target file
2. **`output.json`**: Example output of `extract_timestamp`
3. **`whisper-timestamp.json`**: Example output of `whisper-timestamp`
4. **`whisperx.json`**: Example output of `whisperX`

#### `srt/`:

- Contains all `.srt` subtitle examples for a specific video



### Reference:

- [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped)
- [whisperX](https://github.com/m-bain/whisperX)
- [SaT](https://github.com/segment-any-text/wtpsplit)
