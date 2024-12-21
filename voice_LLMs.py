import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from pydub import AudioSegment
from IPython.display import display, Markdown
import pygame
from pathlib import Path
from groq import Groq
from openai import OpenAI
import os

groq_api_key=os.getenv('GROQ_API_KEY')
openai_api_key=os.getenv('OPENAI_API_KEY')
def record_and_process(duration=3, freq=44100, filename="recording.wav"):
    """
    Records audio, transcribes it using Groq, and processes the response with TTS.
    """
    print(f"Recording for {duration} seconds...")
    
    # Start recording
    recording = sd.rec(int(duration * freq),
                      samplerate=freq,
                      channels=1)
    sd.wait()
    
    # Save the recording as a WAV file
    write(filename, freq, recording)
    print(f"Recording saved as {filename}")
    
    print("Transcribing audio...")
    
    # Initialize Groq client
    groq_client = Groq(api_key=groq_api_key)
    
    # Open and transcribe the audio file
    with open(filename, "rb") as file:
        translation = groq_client.audio.translations.create(
            file=(filename, file.read()),
            model="whisper-large-v3",
            response_format="json",
            temperature=0.0
        )
    
    transcription = translation.text
    print("\nTranscribed text:", transcription)
    
    # Process transcription through Groq
    chat_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Keep answers concise in just one line."
            },
            {
                "role": "user",
                "content": transcription
            }
        ],
        model="llama3-8b-8192",
        temperature=0.5,
        max_tokens=2048,
        top_p=1,
        stream=False
    )
    
    ai_response = chat_completion.choices[0].message.content
    print("\nAI Response:", ai_response)
    
    # Initialize OpenAI client for TTS
    openai_client = OpenAI(api_key=openai_api_key)
    
    
    # Generate and play TTS response
    print("\nGenerating speech response...")
    tts_response = openai_client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=ai_response
    )
    
    # Save to file and play
    speech_file_path = "response_speech.mp3"
    tts_response.stream_to_file(speech_file_path)
    
    # Play the response using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(speech_file_path)
    pygame.mixer.music.play()
    
    # Wait for audio to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    return {
        "transcription": transcription,
        "ai_response": ai_response
    }

if __name__ == "__main__":
    try:
        result = record_and_process()
        print("\nProcess completed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")