# Face-Recognition

This is a face recognition attendance system built using OpenCV, face_recognition, and Streamlit. The system recognizes faces from a set of training images, captures faces using a webcam, and logs attendance in a CSV file.

## Installation

1. Clone the repository: `git clone https://github.com/vivekraiii/face-recognition.git`
2. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Place the training images in a directory.
2. Run the Streamlit app: `streamlit run Final_Project.py`
3. Enter the path of the directory containing the training images.
4. Click the "Start webcam" checkbox to start capturing faces.
5. The app displays the recognized face along with the name of the person and logs attendance in a CSV file.

## Credits

The face recognition model is powered by the [face_recognition](https://github.com/ageitgey/face_recognition) library developed by Adam Geitgey.
