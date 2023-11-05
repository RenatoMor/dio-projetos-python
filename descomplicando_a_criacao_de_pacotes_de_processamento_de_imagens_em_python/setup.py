from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing-RenatoMor",
    version="0.0.1",
    author="Renato Moreira",
    author_email="renato",
    description="Image processing. This project is part of DIO Python Developer Training Bootcamp project challenge. This package is the first upload project on the Test Pypi website. E-mail:renato.moreira@gmail.com.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RenatoMor/dio_formacao_python_developer_image-processing-package-renatom",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)