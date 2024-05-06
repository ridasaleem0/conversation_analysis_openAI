# Import required packages
import backoff  # for exponential backoff
import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


# Define your LLMWrapper class within this file, with the necessary methods.
class LLMWrapper:
    def __init__(self, api_key, config):
        # Store the API key and configuration.
        self.api_key = api_key
        self.model_name = config['model_name']
        self.max_tokens = config['max_tokens']

    # Function to handle OpenAI API calls with rate limit backoff
    @backoff.on_exception(backoff.expo, openai.RateLimitError)
    def prompt_completion(self, messages):
        """
        Prompt completion is a helper function that wraps the OpenAI API call to
        complete a prompt. It handles rate limiting and retries on errors.
        Args:
        prompt: The prompt to complete.
        Returns: The OpenAI API response.
        """

        try:
            # Logic to generate a response to a prompt by interacting with the OpenAI API.
            client = OpenAI(api_key=self.api_key)
            response = client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                max_tokens=self.max_tokens
            )

            # Return the generated response.
            full_text = response.choices[0].message.content

            # Split text on the basis of each speaker of the generated text
            sentences = full_text.split("r'speaker\d*")
            # print("sentences", sentences)

            # # Split the generated text into sentences
            # if len(sentences) > 1:
            #     first_sentence = sentences[0].strip()
            #     if not first_sentence[0].isupper() or not first_sentence[-1].isalnum():
            #         full_text = full_text[len(first_sentence):].strip()
            #
            #     last_sentence = sentences[-1].strip()
            #     if not last_sentence or not last_sentence[-1].isalnum():  # Add check for empty string
            #         full_text = full_text[:len(full_text) - len(last_sentence)].strip()

            # Additional cleanup
            # full_text = full_text.strip(".”")
            f = '\n'.join(sentences)
            return f

        except Exception as e:
            print(f"Exception in OpenAI completion task: {str(e)}")
            return None

    def extract_conversation_text(self, file_path):
        """
        Extracts the text from a conversation.
        Args:
        file: The path of the text file.
        Returns: Conversation text between speakers
        """

        # Logic to extract the text from an article.
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content

        except Exception as e:
            print(f"Forbidden URL Exception, Error downloading and parsing article from {file}: {str(e)}")
            return None, None


class SmartConversationAnalysis:
    def __init__(self, api_key, config):
        self.llm_wrapper = LLMWrapper(api_key, config)

    def deep_analytics(self, text_file, sentiment_logic):
        """
        Generates the speaker analysis given text/audio file using the given sentiment logic. It uses the
        load_text_content and LLMWrapper's methods to produce the psychological analysis of the chat.
        Args:
        text_file (str): path of the chat to be analyzed.
        sentiment_logic (str): Summarization logic to be used.
        Returns: formatted_output (str): Formatted output of each speaker analysis.
        """
        try:
            # Fetch and process the content from the URL.
            conversation_text = self.load_text_content(text_file)

            # Make separate API calls for each part of the article
            print("\nGenerating Summary...\n")
            summary = self.generate_speaker_insights(conversation_text, sentiment_logic)

            return summary

        except Exception as e:
            print(f"Exception in summarization process: {str(e)}")
            return None

    def load_text_content(self, file):
        """
        Loads the conversation from a file uploaded.
        Args:
        file: The file to load.
        Returns: string containing contents of the text file.
        """
        # Method to fetch and process content from the given text file.
        conversation_flow = self.llm_wrapper.extract_conversation_text(file)

        return conversation_flow

    def generate_speaker_insights(self, conversation_text, sentiment_logic):
        """
        Generate speaker analysis from the chat
        Args:
        conversation_text: A list of responses in the conversation.
        sentiment_logic: A dict indicating the reasoning and output format in the prompt.
        Returns: A string containing the speaker analysis of each speaker in the conversation.
        """
        try:
            # Logic to generate a psychological and sentiment insights of speakers from the conversation history.
            summaries = []

            # Generate system and user prompts
            # print(f"\nSystem: Give the sentimental insights of the following chat:\n{conversation_text}\n")
            system_prompt = f"""
                          You are an advanced AI language model designed to extract expert psychological
                          insights and sentiments of all the speakers in the given conversation flows.
                          Your goal is to distill complex information, identify key sentiment
                          insights about the each speaker according to the {sentiment_logic}, and 
                          generate concise and informative description about the insights gathered 
                          in the form of {sentiment_logic['output_format']}
                          """

            user_prompt = f"""
                        Write expert sentimental or psychological insights of each speaker involved 
                        in the following conversational flow: \n{conversation_text}\n
                        Consider relevant {sentiment_logic['reasoning']} and nuances in the content.
                        """
            # Single shot prompt
            assistant_prompt = f"""
                        [Speaker_2] likes a sport. It seems he cares about his health’.
                        [Speaker_1] pretends to be smart’.
                        """

            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
                {"role": "assistant", "content": assistant_prompt}
            ]

            # Call the LLM wrapper to generate a response to the prompt.
            summary = self.llm_wrapper.prompt_completion(messages)
            summaries.append(summary)

            # Combine the summaries of all chunks
            combined_summary = " ".join(summaries)

            return combined_summary

        # Handle exceptions if the LLM wrapper encounters an error.
        except Exception as e:
            print(f"Generating summary error occurred. {e}")
            return None


# Main function to demonstrate usage.
# Instantiate the SmartConversationAnalysis class.
def analyse_conversation(text_file):
    # The text file of the conversation for analysis.

    # Retrieving the OpenAI API key from environment variables.
    # openai_api_key = os.getenv("OPENAI_API_KEY")
    openai_api_key = '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'

    # Configuration for the LLMWrapper, such as the model name and token limits.
    openai_config = {"model_name": "gpt-3.5-turbo", "max_tokens": 2000}

    # Instantiate the chat analyser with the API key and configuration.
    analyser = SmartConversationAnalysis(openai_api_key, openai_config)

    # The logic for summarization may include parameters like reasoning or output format, or it could be blank.
    sentiment_logic = {
        "reasoning": "Extract key points relevant to sentiment analysis.",
        "output_format": "Speaker name followed by the results."
    }

    # Generate the summary.
    analytics = analyser.deep_analytics(text_file, sentiment_logic)

    # Print the summary.
    print("\nDeep analytics generated.\n")

    return analytics
