# Test Computools

This project is a Python application that utilizes Docker for deployment. It includes tests written using `pytest`.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Building the Docker Image](#building-the-docker-image)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [GitHub Actions](#github-actions)
- [License](#license)

## Project Structure

The directory structure of the project is as follows:


- **app/**: The main folder containing the application code.
  - `database.py`: Module for database operations.
  - `logging_config.py`: Configuration for logging.
  - `main.py`: The main application module.
  - `models.py`: Model definitions.
  - `utils.py`: Utility functions.
- **test/**: Folder containing tests.
  - `test_main.py`: Tests for the `main.py` module.
- **.github/**: Contains GitHub Actions settings for CI/CD.
- **requirements.txt**: A list of Python dependencies.
- **Dockerfile**: File for building the Docker image.
- **README.md**: This file.


## Installation

To work with this project, you will need Docker and Docker Compose installed on your machine. Ensure that they are properly set up.

## Building the Docker Image

1. Clone the repository:

```git clone https://github.com/parkhomchukalexei/computools.git```
```cd computools```

2. Build the Docker image:

```docker build -t test_computools .```

3. Running the Application

After building the image, you can run the application:

```docker run -d --name test_computools_container test_computools```

4. Running Tests

To run the tests, you need to set the PYTHONPATH environment variable so that pytest can find your modules. Run the tests inside the container:

```docker run --rm -v $(pwd):/app -w /app test_computools pytest```
