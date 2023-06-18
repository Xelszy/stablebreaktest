from setuptools import setup, find_packages

setup(
    name='stablebreaktest',
    version='0.1.0-beta.1',
    author='Vans',
    author_email='xelszyfx@gmail.com',
    description='utility colab',
    url='https://github.com/Xelszy/stablebreaktest',
    packages=find_packages(),
    install_requires=[
        'safetensors==0.2.6',
        'requests==2.27.1',
        'tqdm==4.65.0',
        'PyYAML==6.0',
        'gdown==4.7.1',
        'toml==0.10.2',
        'rarfile==4.0',
        'xmltodict==0.13.0',
        'pydantic==1.10.8',
        'gradio==3.33.1',
    ],
)
