from crewai_tools import SerperDevTool, TXTSearchTool, WebsiteSearchTool
from langchain.tools import tool
import os
import openai


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

serper_tool=SerperDevTool()
web_search = WebsiteSearchTool()
text_search = TXTSearchTool(txt = "C:\\Users\\VIVEK\\OneDrive\\Desktop\\multi ai agent\\training_video_script.txt")


# ---------------------------------------------------------Custom_Tools--------------------------------------------------------- #

# -------------1. Image_Generating_tool--------------Using Dall-E3
class DalleImageGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    @tool("dalle_image_generator")
    def generate_image(self, prompt: str, size: str = "1024x1024", n: int = 1) -> str:
        """
        Generate images using DALL-E.

        Args:
            prompt (str): The prompt for image generation.
            size (str): The size of the generated image. Default is 1024x1024.
            n (int): The number of images to generate. Default is 1.

        Returns:
            str: The URL(s) of the generated image(s).
        """
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=n,
                size=size
            )
            image_urls = [img['url'] for img in response['data']]
            return '\n'.join(image_urls)
        except Exception as e:
            return str(e)








# -------------1. PDF_Generating_tool--------------Using fpdf library
from fpdf import FPDF

@tool
def generate_pdf(content: str, output_file: str = 'output.pdf') -> str:
    """
    Generate a PDF from the given content.

    Args:
        content (str): The content to include in the PDF.
        output_file (str): The name of the output PDF file.

    Returns:
        str: The path to the generated PDF file.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    pdf.output(output_file)
    return output_file

# Usage Example
if __name__ == "__main__":
    with open("spoken_content.txt", "r") as file:
        content = file.read()
        pdf_path = generate_pdf(content)
        print(f"PDF generated at: {pdf_path}")
