# Realtime_Face-Hand_detection

This project implements real-time face and hand detection using **MediaPipe** and **OpenCV**, integrated with a **Flask** web application for online streaming. The application detects faces and hands from webcam input and streams the output through a web browser interface.

## Features

- Real-time face and hand detection using MediaPipe.
- Web-based streaming of the webcam feed via Flask.
- Visual markers for detected faces and hands.

## Technologies Used

- **Python**
- **Flask**: For web application and online streaming.
- **OpenCV**: For video capture and processing.
- **MediaPipe**: For face and hand detection.

## Installation

### Prerequisites

- Python 3.7 or higher

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/face-hand-detection-flask.git
   cd face-hand-detection-flask

2. Create and activate a virtual environment:
   ```
   pip install flask opencv-python mediapipe
   
**Usage**

1. Run the Flask application:
   ```
   python app.py
2. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   
Future Enhancements

Support for additional MediaPipe models (e.g., full-body detection).
Enhanced UI for the web interface.


Contributing

Feel free to open issues or submit pull requests if you have suggestions for improving this project!

License
This project is licensed under the MIT License.
   
