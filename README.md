
# Coffee Drinking Detection with OpenCV, dlib, and Pygame

This project is a Python-based application that uses a webcam to detect when you are drinking coffee. It uses OpenCV for video capture, dlib for facial landmark detection, and Pygame to play a sound alert.

## Features

- Real-time face detection and mouth aspect ratio (MAR) calculation.
- Alerts the user with a sound when drinking coffee is detected.
- Pause and resume the detection using keyboard input.
- Displays the number of times drinking coffee was detected when paused.

## Project Structure

project_directory/
│
├── main.py
├── detector.py
├── utils.py
├── config.py
└── shape_predictor_68_face_landmarks.dat


- **main.py**: The main script that handles video capture, detection logic, and user interaction.
- **detector.py**: Contains functions for face and landmark detection using dlib.
- **utils.py**: Contains utility functions, including the calculation of the Mouth Aspect Ratio (MAR).
- **config.py**: Configuration file containing threshold values and the path to the sound file.

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
   cd your-repository-name


2. **Install the required libraries**

pip install -r requirements.txt


3. **Download the shape_predictor_68_face_landmarks.dat file**

Download the file from dlib's model zoo and extract it into the project directory.


4. **Run the Application**

python main.py


**Usage**
The application will start capturing video from the webcam and will detect when you are drinking coffee based on the Mouth Aspect Ratio (MAR).
Press p to pause/resume the detection and to see the number of times drinking coffee was detected.
Press q to quit the application.

**Configuration**
The config.py file contains the configuration parameters:

MAR_THRESHOLD: The threshold value for the Mouth Aspect Ratio to detect drinking.
DURATION_THRESHOLD: The number of seconds the MAR must be above the threshold to trigger the alert.
SOUND_FILE: The path to the sound file that will be played when drinking is detected.


**Contributing**
Contributions are welcome! Please feel free to submit a Pull Request.

**License**
This project is licensed under the MIT License. See the LICENSE file for more details.








