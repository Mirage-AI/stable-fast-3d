from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

setup(
    name='sf3d',
    version='0.1.0',
    description='Stable Fast 3D',
    url='https://github.com/Mirage-AI/stable-fast-3d',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt') + [
        'git+https://github.com/vork/PyNanoInstantMeshes.git'
    ],
    python_requires='>=3.6',
)