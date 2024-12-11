# subtitle-helper


---

### File Descriptions:

#### `src/` Directory:

1. **`download.ipynb`**: Downloads a video from a YouTube link.
2. **`extract_timestamp.ipynb`**: Extracts timestamps for each word in the video.
3. **`train_SaT.ipynb`**: Trains SaT using your own dataset.
4. **`train_lora.py`**: Python script that should be replaced when training SaT.
5. **`whisper-timestamp.ipynb`**: Jupyter notebook for setting up whisper-timestamped data.
6. **`whisper-timestamp.py`**: A GUI version for whisper-timestamp.
7. **`whisperx.ipynb`**: Setup for WhisperX, only runnable on Kaggle.

#### `json/` Directory:

1. **`lora_dummy_config.json`**: Configuration file used when training SaT.
2. **`output.json`**: Example output from `extract_timestamp`.
3. **`whisper-timestamp.json`**: Example output from `whisper-timestamp`.
4. **`whisperx.json`**: Example output from `whisperX`.

#### `srt/` Directory:

- Contains all `.srt` subtitle examples for a specific video.

---

### Explanation:

- The **`src/`** directory contains scripts related to video processing, model training, and setup for different tools like Whisper.
- The **`json/`** directory holds configuration files and output results for different processes.
- The **`srt/`** directory contains subtitle files for a specific video, typically in `.srt` format.
