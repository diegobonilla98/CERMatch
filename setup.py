from setuptools import setup, find_packages

setup(
    name='CERMatch',
    version='0.1.69',
    packages=find_packages(),
    install_requires=[
        'fastwer==0.1.3',
        'unidecode==1.3.7',
    ],
    description='A Python package for calculating CER match score between texts. A novel OCR scoring metric.',
    author='Diego Bonilla',
    author_email='diegobonila@gmail.com',
    url='https://github.com/yourusername/CERMatch'
)
