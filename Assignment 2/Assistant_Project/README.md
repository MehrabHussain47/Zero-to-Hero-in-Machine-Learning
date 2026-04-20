# Nexus AI Assistant

Nexus is a voice-activated, modular AI assistant built using Python. It integrates speech recognition, text-to-speech, local automation skills, and the Google Gemini LLM for a smart, interactive user experience.

## 🚀 Features

- **Phase 1: Sensory System (I/O)**:
  - **listen()**: Captures voice input via microphone with robust error handling for `UnknownValueError` and `RequestError`.
  - **speak()**: High-quality text-to-speech with customizable rate, volume, and voice personality.

- **Phase 2: The Command Center (The Brain)**:
  - **Intent Router**: Distinguishes between local commands (like opening apps) and general questions.
  - **LLM Fallback**: Uses Google Gemini to generate "smart" conversational responses when no local skill is triggered.

- **Phase 3: Automation & Skills**:
  - **Launch Apps**: Open Notepad or Chrome via voice.
  - **Web Search**: Automatically search Google or YouTube.
  - **System Stats**: Get real-time CPU usage and battery levels using `psutil`.
  - **Weather**: Integrated function to fetch data from OpenWeatherMap API.

- **Phase 4: Data Persistence & Memory**:
  - **manage_memory()**: Stores user preferences and facts in a `memory.json` file.
  - **Agentic Memory**: Remembers specific details like "I like black coffee" to recall them later.

## 📁 Project Structure

The project follows a professional directory structure to keep the logic clean and modular:

```text
Assistant_Project/
├── main.py        # The Master Loop & Wake-Word detection
├── engine.py      # Listen and Speak functions
├── brain.py       # LLM integration and Intent Routing
├── skills.py      # System automation functions
└── memory.json    # Stored user data (JSON)
