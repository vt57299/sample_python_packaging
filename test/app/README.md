# Training Content Provider

This project involves creating multiple AI agents that collaborate to generate training content based on a user-provided topic. The system performs tasks ranging from information gathering and script writing to image generation and text-to-speech conversion.

## Project Structure

The project consists of the following main components:

1. **Agents**: Defined in the `agents` file.
2. **Tasks**: Defined in the `tasks` file.
3. **Tools**: Defined in the `tools` file.
4. **Text-to-Speech (TTS)**: Defined in the `tts` file.
5. **Main Execution**: Defined in the `main` file.

## Agents

The project includes several agents, each with a specific role and goal:

- **Senior Information Analyst**: Gathers comprehensive and accurate information on a given topic and explains it in a clear and concise manner suitable for a 10-minute presentation.
- **Senior Script Writer**: Transforms researched information into a compelling and educational script.
- **YouTube Blogger**: Creates engaging and professional training video scripts.
- **Content Extractor**: Extracts spoken content from a script for educational training.
- **Image Prompt Generator**: Creates image prompts based on training video content.
- **Image Creator**: Generates high-quality images based on given prompts.

## Tasks

Each agent is assigned specific tasks:

1. **Research and Explain**: Conducts thorough research on the topic and provides detailed educational content.
2. **Write Training Script**: Converts researched information into an engaging training script.
3. **Create Training Video**: Generates a YouTube-style video script.
4. **Extract Spoken Content**: Extracts spoken content from the script, ensuring proper formatting.
5. **Generate Image Prompt**: Creates image prompts from the training video content.
6. **Image Generation Task**: Generates images from the provided descriptions using DALL-E.

## Tools

The project utilizes various tools:

- **SerperDevTool**: Custom tool for data retrieval.
- **TXTSearchTool**: Custom tool for text search within a file.
- **DalleImageGenerator**: Uses OpenAI's DALL-E to generate images from prompts.

## Text-to-Speech (TTS)

The `tts` file includes a function to convert text files into audio files using the `pyttsx3` library. It ensures the output is well-formatted.

## Main Execution

The `main` file orchestrates the overall process by:

1. Initializing a `Crew` with the defined agents and tasks.
2. Kicking off the process based on the user-provided topic.
3. Generating audio from the extracted spoken content.

## Getting Started

### Prerequisites

- Python 3.7+
- Required Python libraries: `crewai`, `dotenv`, `pyttsx3`, `re`, `os`, `openai`, `langchain`

### Installation

1. Clone the repository.
2. Install the required libraries using pip:
   ```bash
   pip install crewai python-dotenv pyttsx3 openai langchain
   ```
3. Set up environment variables for OpenAI API and Serper API keys in a `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

### Running the Project

1. Navigate to the project directory.
2. Run the `main` file:
   ```bash
   python main.py
   ```
3. Enter a topic when prompted to generate the training content and convert it to speech.

### Output

The project generates various output files:
- `training_video_script.txt`: YouTube video script.
- `spoken_content.txt`: Extracted spoken content.
- `image_prompts.txt`: Generated image prompts.
- `generated_images.txt`: URLs of generated images.
- `audio_files`: Directory containing generated audio files.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

