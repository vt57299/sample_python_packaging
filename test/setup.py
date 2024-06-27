from setuptools import setup, find_packages


with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="multi_ai_agents",
    version="0.0.5",
    author="Vivek",
    author_email="vt57299@gmail.com",
    description="A multi agent app that provides training content.",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "crewai",
        "crewai_tools",
        "load_dotenv",
        "langchain",
        "pyttsx3",
        "fpdf",
        "openai",
        # Add other dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    extras_require={
        "dev": ["pytest>=7.0","twine>=4.0.2"]
    },
    python_requires=">=3.10",
)

