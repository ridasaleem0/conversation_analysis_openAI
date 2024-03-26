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
    cd conversation_analysis_openAIconversation_analysis_openAI
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables in a `.env` file. Include any necessary API keys or configuration settings.

### Configuration

Make sure to configure the following environment variables in your `.env` file. For this assignment, we have provided both keys for testing the flask app. 

- `OPENAI_API_KEY`: Your OpenAI API key for performing speaker analysis using the GPT model.
- `DEEPGRAM_API_KEY` = Your DeepGram API key to transcribe the audio files to text.


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

### Troubleshooting

If you encounter any issues while running the application, try the following troubleshooting steps:

Check Dependencies: Make sure all dependencies are installed correctly by running pip install -r requirements.txt again.
Environment Variables: Double-check the .env file to ensure that all required environment variables are correctly configured.
API Keys: Verify that any API keys (such as OpenAI API key) are valid and have the necessary permissions.
File Permissions: Ensure that the Flask application has permission to read and write files in the specified directories, especially for uploaded files.
Logging: Check the application logs for any error messages or exceptions that might provide clues about the issue.
Network Connectivity: If the application relies on external services (such as Deepgram for audio transcription), ensure that your network connection is stable and not blocked by firewalls.
If the issue persists, feel free to open an issue in the GitHub repository for further assistance.

## Files

- `app.py`: Main Flask application file containing routes and logic for handling uploads and analysis.
- `speaker_analysis_gpt.py`: Python module for performing speaker analysis and psychological insights using OpenAI's GPT model.
- `transcribe_audio_deepgram.py`: Python module for extracting text from audio files using Deepgram's transcription service.

