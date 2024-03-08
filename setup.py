from setuptools import find_packages, setup

setup(
    name="mcgenetrator",
    version="0.0.1",
    author="smide kuba",  # Added comma
    author_email="smide223@gmail.com",  # Added comma
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)
