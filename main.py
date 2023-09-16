import asyncio
from hume import HumeStreamClient
from hume.models.config import LanguageConfig
from music_generation import music_gen
from prompt_generation import get_music_prompt
from emotion_detection import get_emotions_text 
from audiocraft.utils.notebook import display_audio


samples = [
    """Today was a gloomy day, nothing changed in terms of observation. I missing my family a little more today. 
    It's been a month since I talked to them. I wish I could see the face of my son."""
]

print("JOURNAL ENTRY: ")
j_text = input()

async def main():
    client = HumeStreamClient("HUME_API_KEY")
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        result = await socket.send_text(j_text)
        emotions = result["language"]["predictions"][0]["emotions"]
        emotions = sorted(emotions, key=lambda x: x["score"], reverse=True)
        e_text  = get_emotions_text(emotions[:5])
        m_prompt = get_music_prompt(e_text)
        print("=====================")
        print("MUSIC GEN PROMPT: ")
        print(m_prompt)
        print("=====================")
        music_output = music_gen(m_prompt)
        display_audio(music_output, sample_rate=32000)

asyncio.run(main())


## SPEECH INPUT
# import openai
# from docx import Document

# def transcribe_audio(audio_file_path):
#     with open(audio_file_path, 'rb') as audio_file:
#         transcription = openai.Audio.transcribe("whisper-1", audio_file)
#     return transcription['text']