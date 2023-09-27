import pytest
import requests

# Define the base URL for your API
BASE_URL = "http://localhost:6543"

# Example test data
test_data_1 = [
    ("track", "genreid", "1"),
    ("employee", "city", "Calgary"),
]
test_data_2 = [
    ("track", "gentreid", "1"),
    ("employete", "city", "Calgary"),
]
@pytest.mark.parametrize("table, column, value", test_data_1)
def test_endpoint(table, column, value):
    # Construct the URL for the endpoint
    url = f"{BASE_URL}/{table}/{column}/{value}"

    # Send a GET request to the endpoint
    response = requests.get(url)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200


@pytest.mark.parametrize("table, column, value", test_data_2)
def test_endpoint_with_corrupted_table_name(table, column, value):
    # Construct the URL for the endpoint
    url = f"{BASE_URL}/{table}/{column}/{value}"

    # Send a GET request to the endpoint
    response = requests.get(url)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 500


if __name__ == "__main__":
    pytest.main()
