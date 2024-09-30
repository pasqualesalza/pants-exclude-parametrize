import requests
import requests_mock

# Create a mock adapter
with requests_mock.Mocker() as mock:
    # Mock a GET request to 'http://example.com'
    mock.get('http://example.com', text='Hello, World!')

    # Make a request to the mocked URL
    response = requests.get('http://example.com')

    # Print the response text
    print(response.text)