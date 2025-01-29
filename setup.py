from setuptools import setup, find_packages

def read_requirements(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

setup(
    name='facexformer',
    version='0.1.0',   # Initial version
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=read_requirements('requirements.txt'),  # List of dependencies
    description=' Official implementation of FaceXFormer: A Unified Transformer for Facial Analysis ',
    long_description=open('README.md').read(),  # Optional: long description from README
    long_description_content_type='text/markdown',
    url='https://github.com/colossyan/facexformer',  # Replace with your repo URL
    author='adamantal',
    author_email='adam@colossyan.com',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.10',  # Specify Python version requirements
)
