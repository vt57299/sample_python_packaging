from crewai import Task
from .agents import information_analyst, script_writer, youtube_blogger, spoken_content_extraction_agent,image_prompt_agent, image_generation_agent
from .tools import serper_tool, DalleImageGenerator, text_search,web_search
import os


# Initialize the custom tool
dalle_tool = DalleImageGenerator(api_key=os.getenv("OPENAI_API_KEY"))


research_and_explain = Task(
    description="Conduct thorough research to gather comprehensive information on the topic '{topic}'. The goal is to provide a detailed and accurate content suitable for a 10-minute training video.",
    expected_output=''' A comprehensive 5-paragraphs long educational content on topic of {topic}''',
    agent=information_analyst,
    tools=[serper_tool, web_search],
    output_file='training content.txt'
)

# Task for writing a training script
write_training_script = Task(
    description="Transform the researched information into a compelling and educational training script on '{topic}'. The script should be structured and engaging, suitable for a 10-minute training video.",
    expected_output='''A well-written training script that makes the information engaging and easy to follow.
                       The script should include an introduction, main content, and conclusion, should contain atleast 1000 words.

                       Example Output:

                       ## Training Script for {topic}

                       1. **Introduction** (1 minute)
                          - "Welcome! Today we'll be discussing {topic}..."
                          - Briefly introduce the topic and its importance.

                       2. **Main Content** (8 minutes)
                          - Explain key concepts.
                          - Use engaging language to maintain interest.
                          - Include examples and applications.
                          - Dive deeper into the topic, explaining how it works or how it is used.
                          - Highlight important data, statistics, or case studies.

                       3. **Conclusion** (1 minute)
                          - "To sum up, {topic} is important because..."
                          - Summarize the key points covered in the video.
                          - Provide a call to action or suggest further reading/resources.

                       Ensure the script is clear, engaging, and suitable for the intended audience also should contain atleast 1000 words. It should be of 10 minutes.
                    ''',
    agent=script_writer,
)

# Task for the YouTube Blogger agent
create_training_video = Task(
    description="Create a 10-minute educational training video script based on the provided script. The goal is to engage students and teach them about '{topic}' in a professional manner, suitable for a YouTube video.",
    expected_output='''A script that outlines the structure and content for a 10-minute training video on '{topic}'.
                       The script should be engaging, easy to follow, educational and should contain minimum of 1000 words.

                       Example Output:

                       ## Script for {topic} Training Video

                       1. **Introduction** (1 minute)
                          - Greet the audience.
                          - Briefly introduce the topic.
                          - Explain why the topic is important.

                       2. **Main Content** (8 minutes)
                          - Break down the main concepts into simple, digestible parts.
                          - Use examples, analogies, and visuals to explain complex ideas.
                          - Provide detailed information, processes, or methods.
                          - Highlight important data, statistics, or case studies.

                       3. **Conclusion** (1 minute)
                          - Summarize the key points covered in the video.
                          - Provide a call to action (e.g., like, subscribe, comment).
                          - Thank the audience for watching.

                       Ensure the script is clear, concise, and engaging, contains atleast 1000 words with a natural flow that keeps the audience interested for 10 minutes.
                    ''',
    agent=youtube_blogger,
    output_file='training_video_script.txt'
)

extract_spoken_content = Task(
    description="Extract only spoken content from the provided script file and ensure the output is properly formatted with line breaks.\n"
                "The agent should read the script, identify and extract only the lines, and output the content.",
    expected_output="The agent should read the script, identify and extract only the content that needs to be spoken for our training video, and output the content maintaining the structure and flow."
                    "For example, the output should not be in one continuous line but should respect the script's natural pauses and sections."
                    "Make sure the output does not contain any special characters except . and , .",
    agent=spoken_content_extraction_agent,
   #  tools = [text_search],
    output_file = 'spoken_content.txt'
)



# Task definition for generating image prompts
generate_image_prompt = Task(
    description="Generate image prompts based on the provided training video content.\n"
                "The images should visually represent key concepts or scenes described in the script.",
    expected_output="Image prompts that visually convey the training video content."
                     "Each prompts stored in different lines."
                     "The output should conatain nothing more then just generated prompts",
    agent=image_prompt_agent,
    output_file = 'image_prompts.txt'
)


# Task definition for generating images from prompt 
image_generation_task = Task(
    description="Generate an image based on the provided description.\n"
                "The agent should read the description and use a pre-trained model to generate a relevant image.",
    expected_output="URL links to the generated images in a .txt file.",
    agent=image_generation_agent,
    tools=[dalle_tool],
    output_file = 'generated_images.txt'
)


