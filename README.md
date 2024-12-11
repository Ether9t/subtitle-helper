# subtitle-helper

src/ └── download.ipynb # Download video from Youtube link
     └── extract_timestamp.ipynb # Extract each word's timestamp
     └── train_SaT.ipynb # Using you own datasets to train SaT
     └── train_lora.py # .py that need to be replaced when training SaT
     └── whisper-timestamp.ipynb # Setup for whisper-timestamped
     └── whisper-timestamp.py # a GUI version
     └── whisperx.ipynb # Setup for whisperX, only can run on Kaggle
     
json/ └── lora_dummy_config.json # Using when training SaT
      └── output.json # Example for output of extract_timestamp
      └── whisper-timestamp.json # Example for output of whisper-timestamp
      └── whisperx.json # Example for output of whisperX

srt/ Contains all .srt examples for one specific video
