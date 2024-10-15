import logging

from app.main import calculate_average

test_data = [
    {
        "token_count": 100,
        "total_generation_time": 50,
        "time_to_first_token": 5,
        "time_per_output_token": 0.5,
    },
    {
        "token_count": 200,
        "total_generation_time": 100,
        "time_to_first_token": 10,
        "time_per_output_token": 0.6,
    },
]


def test_calculate_average_with_valid_data():
    result = calculate_average(test_data)
    assert result["average_token_count"] == 150
    assert result["average_generation_time"] == 75
    assert result["average_time_to_first_token"] == 7.5
    assert result["average_time_per_output_token"] == 0.55


def test_calculate_average_with_missing_metric(caplog):
    invalid_data = test_data.copy()
    del invalid_data[0]["time_to_first_token"]

    with caplog.at_level(logging.ERROR):
        calculate_average(invalid_data)

    assert "KeyError: 'time_to_first_token' - Missing key in data" in caplog.text


def test_calculate_average_with_empty_data():
    result = calculate_average([])
    assert "error" in result
    assert result["error"] == "No data available"
