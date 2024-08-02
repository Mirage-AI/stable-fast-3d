from setuptools import setup, find_packages

# Function to read the requirements.txt file
def parse_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

setup(
    name='sf3d',
    version='0.1.0',
    description='Stable Fast 3D',
    url='https://github.com/Mirage-AI/stable-fast-3d',  # Update with your project's URL
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    python_requires='>=3.6',
)