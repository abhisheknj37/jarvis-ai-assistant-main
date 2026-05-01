# Jarvis AI Assistant

## Description
Jarvis AI Assistant is a comprehensive Python-based virtual assistant inspired by Iron Man's JARVIS. It leverages AI, automation, and multimedia capabilities to perform a wide range of tasks, from system control and web automation to intelligent conversations and multimedia interactions. Built with modularity in mind, it integrates various libraries for speech recognition, text-to-speech, image generation, and more, making it a versatile tool for productivity and entertainment.

The project aims to provide an open-source, customizable AI assistant that can run on Windows systems, with features that can be extended or modified as needed.

## Features

### Core Features
- **AI-Powered Conversations**: Uses webscout for intelligent, context-aware responses to user queries.
- **Speech Recognition and Synthesis**: Supports voice input via Selenium-based web interface and text-to-speech output using Fast DF TTS.
- **Automation Suite**: Comprehensive system automation including app launching, web browsing, music playback, and hardware controls.

### Detailed Feature Breakdown
- **Automation**:
  - Battery monitoring and alerts (low battery, full charge).
  - App opening and management.
  - Music playback on YouTube and Spotify.
  - Web browsing and tab management.
  - System scrolling and media controls.
  - Plug detection for charging status.

- **AI Brain**:
  - Integrated chat functionality with persistent conversation history.
  - Supports complex queries and provides detailed responses.

- **Speech and Text**:
  - Voice commands via microphone input.
  - Text-to-speech for responses.
  - Animated text output for better user experience.

- **System Features**:
  - Brightness control (get/set screen brightness).
  - Volume adjustment (get/set system volume).
  - Microphone and speaker health diagnostics.
  - Clap detection for hands-free activation.
  - Running application monitoring.

- **Communication**:
  - WhatsApp message automation.
  - Email and other integrations (expandable).

- **Utilities**:
  - Weather checking.
  - Image generation using AI models.
  - Time-based operations: alarms, schedules, and alerts.
  - IP address retrieval.
  - Joke and advice fetching.

- **Vision and Real-Time**:
  - Computer vision tasks (face detection, object recognition).
  - Real-time Google search integration.

## Project Structure
The project is organized into modular directories for easy maintenance and extension:

- **Automation/**: Core automation scripts for system controls, music, web, and battery.
  - `Automation_Brain.py`: Main automation logic.
  - `Battery.py`: Battery monitoring and alerts.
  - `open_App.py`: Application launching.
  - `Play_Music_YT.py`: YouTube music playback.
  - `playmusic_Sfy.py`: Spotify music playback.
  - `Web_Open.py`: Web browser automation.
  - `tab_automation.py`: Browser tab management.
  - `scrool_system.py`: Scrolling controls.
  - `Youtube_play_back.py`: YouTube video controls.

- **Brain/**: AI conversation engine.
  - `brain.py`: AI chat integration.

- **Data/**: Data handling and configurations.
  - `DLG_Data.py`: Dialog data for responses.

- **Features/**: Additional system features.
  - `br_persentage.py`: Brightness control.
  - `check_running_app.py`: App monitoring.
  - `clap_d.py`: Clap detection.
  - `create_file.py`: File creation utilities.
  - `find_my_ip.py`: IP address finder.
  - `get_advice.py`: Advice fetching.
  - `get_jokes.py`: Joke generator.
  - `mike_health.py`: Microphone diagnostics.
  - `set_br.py`: Brightness setter.
  - `set_get_volume.py`: Volume controls.
  - `speaker_health.py`: Speaker diagnostics.

- **NetHyTechSTT/**: Speech-to-text using Selenium.
  - `listen.py`: Voice input handler.

- **New/**: Miscellaneous new features.
  - `datafeatch.py`: Data fetching utilities.

- **Real_Time/**: Real-time integrations.
  - `google_big.py`: Google search integration.
  - `google_small.py`: Lightweight Google queries.

- **TextToImage/**: AI image generation.
  - `gen_image.py`: Image generator.

- **TextToSpeech/**: Text-to-speech engine.
  - `Fast_DF_TTS.py`: TTS implementation.

- **Time_Operations/**: Time-based features.
  - `brain.py`: Time logic.
  - `throw_alert.py`: Alert system.

- **Vision/**: Computer vision modules.
  - `MVbrain.py`: Multi-vision tasks.
  - `Vbrain.py`: Vision processing.

- **Weather_Check/**: Weather information.
  - `check_weather.py`: Weather API integration.

- **Whatsapp_automation/**: WhatsApp messaging.
  - `wa.py`: WhatsApp automation.

- **Root Files**:
  - `jarvis.py`: Main entry point.
  - `co_brain.py`: Core brain logic.
  - `demo.py`: Demonstration script.
  - `ui.py`: User interface (if applicable).
  - `requirements.txt`: Python dependencies.
  - `setup.py`: Setup script.
  - `README.md`: This file.
  - `LICENSE`: License information.

## Installation
1. **Prerequisites**:
   - Python 3.7 or higher.
   - Windows OS (primary support; may work on others with modifications).
   - Internet connection for AI and web features.

2. **Clone the Repository**:
   ```
   git clone https://github.com/abhisheknj37/jarvis-ai-assistant.git
   cd jarvis-ai-assistant
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```
   Note: Some features require optional packages. If a feature is disabled, install the missing library (e.g., `pip install pyautogui` for automation).

4. **Run the Assistant**:
   ```
   python jarvis.py
   ```

## Usage
After starting, Jarvis will greet you and wait for commands. Interact via text input or voice (if Selenium is configured).

### Example Commands
- **Voice Activation**: Clap twice or say "Jarvis" (requires microphone setup).
- **App Opening**: "open notepad" or "open chrome".
- **Music**: "play music on youtube [song name]" or "play music on spotify [song name]".
- **System Info**: "check battery percentage" or "get volume".
- **AI Chat**: "what is the weather today?" or complex queries.
- **Automation**: "search in google [query]" or "scroll down".
- **Utilities**: "tell me a joke" or "generate image [prompt]".

### Configuration
- Edit `input.txt` for text input.
- Modify paths in scripts (e.g., icon paths in `Alert.py`).
- For voice input, ensure Chrome and Selenium are set up.

### Troubleshooting
- **Import Errors**: Install missing packages with `pip install [package]`.
- **Voice Not Working**: Check microphone permissions and Selenium setup.
- **AI Not Responding**: Verify internet and webscout API.
- **Performance Issues**: Run on a system with sufficient RAM (4GB+ recommended).

## Requirements
- **Core**: Python 3.x, requests, threading.
- **Automation**: pyautogui, psutil, pycaw, wmi, comtypes.
- **AI**: webscout.
- **Speech**: playsound, pyaudio, scipy.
- **Web**: selenium, webdriver_manager.
- **Vision**: opencv-python.
- **Others**: See `requirements.txt` for full list.

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-feature`).
3. Commit changes (`git commit -m "Add new feature"`).
4. Push to branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

### Guidelines
- Follow PEP 8 for Python code.
- Add tests for new features.
- Update documentation (this README) for changes.
- Report bugs via Issues.

## Author
- **Abhishek N J**
- LinkedIn: [https://www.linkedin.com/in/abhishek-n-j-4918b7273/](https://www.linkedin.com/in/abhishek-n-j-4918b7273/)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Inspired by Iron Man's JARVIS.
- Thanks to open-source libraries and communities for enabling this project.
- Special thanks to contributors and testers.# jarvis-ai-assistant-main
