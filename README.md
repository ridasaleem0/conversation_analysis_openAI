# conversation_analysis_openAI


# Flask Application for Sentimental Analysis and Speaker Insights

This repository contains a Flask application for analyzing conversations uploaded by users. The application extracts text from uploaded audio files, performs sentiment analysis, and provides insights about the speakers involved in the conversation.

## Usage

### Prerequisites

- Python 3.10 installed on your system
- Dependencies installed using `pip install -r requirements.txt`
- Environment variables configured in a `.env` file

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/ridasaleem0/conversation_analysis_openAI.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables in a `.env` file. Include any necessary API keys or configuration settings.

### Running the Application

Run the Flask application using the following command:

```bash
python app.py
```

The application will start, and you can access it in your web browser at `http://localhost:2005`.

### Uploading Conversations

Users can upload conversation files through the web interface. Supported file formats include text and audio.

### Viewing Analysis Results

After uploading a conversation, the application performs sentiment analysis and speaker insights. Users can view the analysis results on the web interface.

## Files

- `app.py`: Main Flask application file containing routes and logic for handling uploads and analysis.
- `speaker_analysis_gpt.py`: Python module for performing speaker analysis and psychological insights using OpenAI's GPT model.
- `transcribe_audio_deepgram.py`: Python module for extracting text from audio files using Deepgram's transcription service.

