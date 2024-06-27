from crewai import Crew, Process
from .tts import generate_audio_from_text
from .agents import information_analyst, script_writer, youtube_blogger,spoken_content_extraction_agent,image_prompt_agent,image_generation_agent
from .tasks import research_and_explain,write_training_script, create_training_video,extract_spoken_content,generate_image_prompt,image_generation_task

def run():
    # setting up crew
    crew = Crew(
        agents = [information_analyst, script_writer, youtube_blogger, spoken_content_extraction_agent, image_prompt_agent],
        tasks = [research_and_explain, write_training_script, create_training_video, extract_spoken_content, generate_image_prompt],
        process = Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        share_crew=True,
        verbose=2,
    )

    # kicking off crew
    topic = input("Enter a topic: ")
    result = crew.kickoff(inputs = {'topic':topic})
    # print(result)

    # ------------------Converting Text to Speech------------------------------------------------
    # file_path = "C:\\Users\\VIVEK\\OneDrive\\Desktop\\multi ai agent\\spoken_content.txt"
    # output_directory = 'audio_files'

    # generate_audio_from_text(file_path, output_directory)
    return result