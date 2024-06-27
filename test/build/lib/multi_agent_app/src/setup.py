from setuptools import setup, find_packages

setup(
    name='MY_PROJECT',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'crewai',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'my_crewai_project= my_crewai_project.main:main',
        ],
    },
)
