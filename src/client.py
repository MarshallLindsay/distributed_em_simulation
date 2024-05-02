import requests
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import pickle

# get data from server - numpy array converted to binary
def get_data(url="localhost:10001"):

    # Send a GET request
    response = requests.get(f"http://{url}")

    # Check if the request was successful
    if response.status_code != 200:
        print("Error:", response.status_code)
        return

    # Load the response
    data = BytesIO(response.content)

    # Deserialize the data
    data = pickle.load(data)

    # Extract the image and metadata
    image = data['image']
    metadata = data['metadata']

    print(metadata)

    # Display the image
    plt.imshow(image, cmap='gray')
    plt.show()


if __name__ == "__main__":
    get_data() 

