import http.server
import numpy as np
from io import BytesIO
import pickle

# Handler that returns a random image
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):

        image = np.random.rand(100, 100)

        metadata = {
            'description': 'Random image',
            'shape': image.shape,
            'dtype': str(image.dtype),
        }


        buffer = BytesIO()

        # Serialize the image and metadata
        pickle.dump({'metadata': metadata, 'image': image}, buffer)
        binary_data = buffer.getvalue()

        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'application/octet-stream')
        self.end_headers()

        self.wfile.write(binary_data)

if __name__ == '__main__':
    http.server.test(HandlerClass=MyHandler, port=10001) 
