# Voice LLMs Assistant

A voice-based AI assistant that creates a natural conversation flow by combining three powerful AI models:

🎤 Groq Whisper - Converts your speech to text
🧠 Groq LLaMA - Processes and understands your message
🔊 OpenAI TTS - Converts the AI response back to speech

## Project Structure
```
voice-llms/
├── voice_llms.py        # Main functionality
├── requirements.txt     # Project dependencies
├── .env                # Environment variables (create this)
└── LICENSE             # MIT License
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

3. **Set up environment variables**

Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

4. **Run the assistant**
```python
from voice_llms import record_and_process

# Start recording and processing
result = record_and_process(duration=3)  # Records for 3 seconds
```

## Usage Examples

### Basic Usage
```python
# Import the main function
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
- python-dotenv: Environment management

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

The script includes error handling for:
- Audio recording issues
- API connection problems
- File handling errors

Errors are caught and printed with descriptive messages:
```python
try:
    result = record_and_process()
except Exception as e:
    print(f"An error occurred: {str(e)}")
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Groq](https://groq.com/) for Whisper and LLaMA models
- [OpenAI](https://openai.com/) for TTS service
- All open-source package contributors

## Common Issues & Solutions

1. **Audio device not found**
   - Ensure your microphone is connected and properly set up
   - Check system audio settings

2. **API Key errors**
   - Verify your API keys in the `.env` file
   - Check for proper environment variable loading

3. **Audio playback issues**
   - Ensure speakers/headphones are connected
   - Check pygame initialization

## Support

For support, please:
1. Check existing [issues](your-repo-issues-url)
2. Create a new issue with detailed description
3. Include error messages and environment details