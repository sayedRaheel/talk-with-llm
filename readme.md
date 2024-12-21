# Voice LLMs Assistant

A voice-based AI assistant that creates a natural conversation flow by combining three powerful AI models:

🎤 Groq Whisper - Converts your speech to text
🧠 Groq LLaMA - Processes and understands your message
🔊 OpenAI TTS - Converts the AI response back to speech

## Audio Recording Details

The voice assistant uses `sounddevice` to handle real-time audio recording. Here's how it works:

### Recording Process
```python
import sounddevice as sd
from scipy.io.wavfile import write

def record_and_process(duration=3, freq=44100, filename="recording.wav"):
    # Start recording
    recording = sd.rec(int(duration * freq),
                      samplerate=freq,
                      channels=1)
    
    # Wait for the recording to complete
    sd.wait()
    
    # Save as WAV file
    write(filename, freq, recording)
```

### Recording Parameters
- **Duration**: Default 3 seconds (adjustable)
- **Frequency**: 44.1kHz (CD quality)
- **Channels**: Mono (1 channel)
- **Format**: WAV file
- **Bit Depth**: 16-bit

### Audio Processing Pipeline
1. **Recording**: Captures audio through your microphone
2. **Saving**: Stores as temporary WAV file
3. **Processing**: Sends to Groq's Whisper for transcription
4. **Cleanup**: Temporary files are managed automatically

### Customizing Recording

Change recording duration:
```python
# Record for 5 seconds
result = record_and_process(duration=5)
```

Use different audio quality:
```python
# Use higher sampling rate
result = record_and_process(freq=48000)
```

Custom output file:
```python
# Save to specific file
result = record_and_process(filename="my_speech.wav")
```


## Project Structure
```
voice-llms/
├── voice_llms.py        # Main functionality
└── requirements.txt     # Project dependencies
```

## Features

- 🎤 Real-time voice recording
- 🗣️ Speech-to-Text using Groq's Whisper Large v3
- 🤖 LLM processing using Groq's LLaMA 3-8b model
- 🔊 Text-to-Speech using OpenAI's TTS
- ▶️ Immediate audio playback of responses

## Quick Start

1. **Clone the repository**
```bash
git clone [your-repository-url]
cd voice-llms
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up API Keys**

You have two options to set up your API keys:

Option 1: Direct in code (Quick testing)
```python
# In voice_llms.py
groq_client = Groq(api_key="your_groq_api_key")
openai_client = OpenAI(api_key="your_openai_api_key")
```

Option 2: Environment variables (Recommended for development)
```bash
# Export in terminal
export GROQ_API_KEY="your_groq_api_key"
export OPENAI_API_KEY="your_openai_api_key"

# Or create .env file
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

4. **Run the assistant**

Simple run:
```bash
python voice_llms.py
```

Or import in your code:
```python
from voice_llms import record_and_process

# Start recording and processing
result = record_and_process(duration=3)  # Records for 3 seconds
```

## Usage Examples

### Basic Usage
```python
# Direct run
python voice_llms.py

# Or import and use
from voice_llms import record_and_process

# Record and process speech
result = record_and_process()

# Access results
print(f"You said: {result['transcription']}")
print(f"AI responded: {result['ai_response']}")
```

### Custom Duration Recording
```python
# Record for 5 seconds
result = record_and_process(duration=5)
```

### Custom Frequency
```python
# Record with different sampling frequency
result = record_and_process(freq=48000)
```

### Custom Output Filename
```python
# Specify custom output filename
result = record_and_process(filename="my_recording.wav")
```

## Dependencies

- sounddevice: Audio recording
- scipy: Audio processing
- wavio: WAV file handling
- pydub: Audio manipulation
- pygame: Audio playback
- groq: Whisper STT and LLaMA
- openai: TTS service
- python-dotenv: Environment management (optional)

## Configuration

### LLM Parameters
The LLaMA model can be configured by modifying parameters in `voice_llms.py`:
```python
chat_completion = groq_client.chat.completions.create(
    model="llama3-8b-8192",
    temperature=0.5,
    max_tokens=2048,
    top_p=1
)
```

### TTS Voice Options
Change the OpenAI TTS voice in `voice_llms.py`:
```python
tts_response = openai_client.audio.speech.create(
    model="tts-1",
    voice="nova",  # Options: alloy, echo, fable, onyx, nova, shimmer
    input=ai_response
)
```

## Error Handling

Common errors and solutions:

1. **Audio device not found**
   - Ensure microphone is connected
   - Check system audio settings

2. **API Key errors**
   - Verify API keys are correct
   - If using environment variables, ensure they're properly set
   - If using direct keys, check for typos

3. **Audio playback issues**
   - Ensure speakers/headphones are connected
   - Check pygame initialization

## License

MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Groq](https://groq.com/) for Whisper and LLaMA models
- [OpenAI](https://openai.com/) for TTS service
- All open-source package contributors