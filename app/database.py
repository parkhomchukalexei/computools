import json

from app.logging_config import logger


def get_test_data():
    """
    Load benchmarking results from the 'test_database.json' file.

    This function attempts to open and read the 'test_database.json'
    file, parse its content as JSON, and return the value associated
    with the 'benchmarking_results' key. If the file is not found,
    cannot be decoded as JSON, or the key is missing, an appropriate
    error message is logged and returned.

    Returns:
        dict: If successful, returns the dictionary associated with
              the 'benchmarking_results' key from the JSON file.
              If an error occurs, returns a dictionary with an
              'error' key describing the issue.

    Exceptions Handled:
        - FileNotFoundError: If the file 'test_database.json' does
          not exist.
        - JSONDecodeError: If the file cannot be parsed as valid JSON.
        - KeyError: If the 'benchmarking_results' key is not present
          in the JSON.
        - Exception: Catches any other unexpected errors.
    """

    try:
        with open("test_database.json", "r") as f:
            data = json.load(f)
        return data["benchmarking_results"]
    except FileNotFoundError as e:
        logger.error(f"FileNotFoundError: {str(e)}")
        return {"error": "File 'test_database.json' not found"}
    except json.JSONDecodeError as e:
        logger.error(f"JSONDecodeError: {str(e)}")
        return {"error": "Error decoding JSON from 'test_database.json'"}
    except KeyError as e:
        logger.error(f"KeyError: {str(e)}")
        return {"error": "'benchmarking_results' key not found in the JSON file"}
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {"error": f"An unexpected error occurred: {str(e)}"}
