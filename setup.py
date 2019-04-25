import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="docker-compose-help",
    version="0.1.0",
    author="Ariel Lima",
    author_email="ariel.lima@gordon.edu",
    description="A Python wrapper for generating a compose file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArielLima/DC-wrapper",
    packages=setuptools.find_packages(),
    install_requires=[
          'pyyaml',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)