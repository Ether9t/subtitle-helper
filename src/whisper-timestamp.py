import sys
import os
import json
import whisper_timestamped
from moviepy.editor import VideoFileClip
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QVBoxLayout, QMessageBox, QInputDialog
from PyQt5.QtCore import Qt
import numpy as np
import yt_dlp

def download_audio_from_youtube(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(id)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            audio_file = f"{info_dict['id']}.wav"

            return audio_file
        
    except Exception as e:

        return str(e)

def extract_audio_from_video(video_file):
    try:
        audio_file = "extracted_audio.wav"
        video_clip = VideoFileClip(video_file)
        video_clip.audio.write_audiofile(audio_file, codec='pcm_s16le', ffmpeg_params=["-ac", "1", "-ar", "16000"])

        return audio_file
    
    except Exception as e:

        return str(e)

def process_audio(audio_file):
    try:
        print("Processing audio file:", os.path.abspath(audio_file))
        if not os.path.exists(audio_file):
            
            return "Audio file does not exist."

        with open(audio_file, 'rb') as f:
            print("Successfully opened audio file.")
        try:
            audio = whisper_timestamped.load_audio(audio_file)
        except Exception as e:
            print(f"An error occurred while loading audio: {e}")
        audio = audio / np.max(np.abs(audio))
        model = whisper_timestamped.load_model("base", device="cpu")
        result = whisper_timestamped.transcribe_timestamped(model, audio, language="en")

        writer = whisper_timestamped.utils.get_writer("srt", ".")
        writer(result, "output")
        print(f"SRT file saved: transcription.srt")

        json_output_file = "output.json"
        with open(json_output_file, 'w', encoding='utf-8') as json_file:
            json.dump(result, json_file, indent=2, ensure_ascii=False)
        print(f"JSON file saved: {json_output_file}")

        return "Transcription completed"
    
    except Exception as e:
        return str(e)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Video Transcriber')
        self.setGeometry(250, 250, 750, 500)

        layout = QVBoxLayout()

        self.label = QLabel('🌟 Video Transcriber 🌟', self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.upload_button = QPushButton('Upload Video', self)
        self.upload_button.clicked.connect(self.upload_video)
        layout.addWidget(self.upload_button)

        self.youtube_button = QPushButton('Download YouTube Video', self)
        self.youtube_button.clicked.connect(self.download_and_transcribe_youtube)
        layout.addWidget(self.youtube_button)

        self.setLayout(layout)

    def upload_video(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Video Files (*.mp4 *.avi);;All Files (*)", options=options)
        if file_name:
            audio_file = extract_audio_from_video(file_name)
            if audio_file:
                result = process_audio(audio_file)
                QMessageBox.information(self, "Transcription Result", result)
            else:
                QMessageBox.warning(self, "Error", "Audio extraction failed.")

    def download_and_transcribe_youtube(self):
        url, ok = QInputDialog.getText(self, 'YouTube URL', 'Enter YouTube video URL:')
        if ok and url:
            audio_file = download_audio_from_youtube(url)
            if audio_file:
                result = process_audio(audio_file)
                QMessageBox.information(self, "Transcription Result", result)
            else:
                QMessageBox.warning(self, "Error", "Audio extraction or download failed.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

# tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")
# model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B")