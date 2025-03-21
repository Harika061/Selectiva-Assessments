import os
import pytest
import requests

# The function that downloads the file
def download_gh():
    url = "https://data.gharchive.org/2023-03-01-10.json.gz"
    local_filename = '/Users/harikaboyina/Downloads/2023-03-01-10.json.gz'

    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        with open(local_filename, 'wb') as f:
            f.write(response.content)
        return local_filename
    else:
        raise Exception(f"Failed to download the file. Status code: {response.status_code}")

# Unit test function using pytest
def test_download_gh():
    # Call the download function
    file_path = download_gh()

    # Assert that the file path is not None
    assert file_path is not None, "File path should not be None."

    # Assert that the file exists
    assert os.path.exists(file_path), "Downloaded file should exist."

    # Assert that the file is not empty
    assert os.path.getsize(file_path) > 0, "Downloaded file should not be empty."

    # Clean up by removing the downloaded file after the test
    if os.path.exists(file_path):
        os.remove(file_path)
