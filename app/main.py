import os
from datetime import datetime
from typing import List

from fastapi import FastAPI, HTTPException

from app.database import get_test_data
from app.models import TimeWindowParams
from app.utils import calculate_average, is_within_time_range, parse_datetime

app = FastAPI()

SUPERBENCHMARK_DEBUG = os.getenv("SUPERBENCHMARK_DEBUG", "False").lower() == "true"

if SUPERBENCHMARK_DEBUG:
    data = get_test_data()
else:
    raise HTTPException(status_code=501, detail="Feature not ready for live yet")


@app.get("/results/average")
def get_average_results():
    """
    Retrieve the average results from the dataset.

    This endpoint calculates and returns the average of the
    available data using the 'calculate_average' function.

    Returns:
        dict: A dictionary containing the calculated average
              results for the dataset.
    """
    return calculate_average(data)


@app.post("/results/average/")
def get_average_results_in_window(params: TimeWindowParams):
    """
    Retrieve the average results within a specified time window.

    This endpoint calculates the average results for data points that
    fall within the specified time window. The time window is defined
    by 'start_time' and 'end_time' parameters.

    Args:
        params (TimeWindowParams): A Pydantic model containing
                                   'start_time' and 'end_time'.

    Raises:
        HTTPException:
            - 400 Bad Request: If 'start_time' is greater than
              'end_time'.
            - 404 Not Found: If no data is found within the specified
              time window.

    Returns:
        dict: A dictionary containing the calculated average results
              for the data within the specified time window.
    """

    if params.start_time > params.end_time:
        raise HTTPException(
            status_code=400, detail="start_time cannot be greater than end_time"
        )

    start_time: datetime = parse_datetime(params.start_time)
    end_time: datetime = parse_datetime(params.end_time)

    filtered_data: List = [
        d for d in data if is_within_time_range(d, start_time, end_time)
    ]

    if not filtered_data:
        raise HTTPException(
            status_code=404, detail="No data found in the given time window"
        )

    return calculate_average(filtered_data)
