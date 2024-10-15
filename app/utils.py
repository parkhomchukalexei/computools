from datetime import datetime

from app.logging_config import logger


def calculate_average(data):
    try:
        if not data:
            logger.error("No data available")
            return {"error": "No data available"}

        metrics = [
            "token_count",
            "total_generation_time",
            "time_to_first_token",
            "time_per_output_token",
        ]

        averages = {
            metric: sum(d[metric] for d in data) / len(data) for metric in metrics
        }

        return {
            "average_token_count": averages["token_count"],
            "average_generation_time": averages["total_generation_time"],
            "average_time_to_first_token": averages["time_to_first_token"],
            "average_time_per_output_token": averages["time_per_output_token"],
        }

    except TypeError as e:
        logger.error(f"TypeError: {str(e)} - Invalid data format")
        return {"error": "Invalid data format"}
    except KeyError as e:
        logger.error(f"KeyError: {str(e)} - Missing key in data")
        return {"error": f"Missing key: {str(e)}"}
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {"error": f"An unexpected error occurred: {str(e)}"}


def parse_datetime(param):
    if isinstance(param, str):
        return datetime.fromisoformat(param)
    elif isinstance(param, datetime):
        return param
    else:
        raise ValueError("Invalid datetime format. Must be str or datetime.")


def is_within_time_range(d, start_time, end_time):
    timestamp = parse_datetime(d["timestamp"])
    return start_time <= timestamp <= end_time
