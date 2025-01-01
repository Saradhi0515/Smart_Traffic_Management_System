# ANPR and ATCC for Smart Traffic Management

Welcome to the ANPR and ATCC for Smart Traffic Management repository! This project aims to revolutionize traffic management in smart city environments by utilizing advanced technologies like Automatic Number Plate Recognition (ANPR) and Automatic Traffic Classification and Control (ATCC).

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Output](#output)
- [License](#license)

---

## Introduction

This project leverages Deep Learning and Object Detection techniques to automate traffic monitoring and control. The system detects and recognizes vehicle license plates using ANPR and classifies different types of traffic with ATCC. By doing so, it aims to:

- Improve traffic flow
- Reduce congestion
- Enhance road safety

## Project Structure

Here is the structure of the repository:

```
ipynbPrograms/CV_Basics/                                # Contains basic learning of computer vision and OCR
Data/                                                   # Input data or videos
Output/Results/Interpolated_results/                    # Interpolated CSV files for visualization
ipynbPrograms/number_plate_detection_model_training/    # Files related to model training
object_tracker/tracker_3.py/                            # Main file for detection and tracking of vehicles in video
output_videos/                                          # Result videos after running visualize.py
Output/Results/                                         # CSV files for initial detection used for interpolation
.testing/                                               # Code for different testing scenarios
Internship_Artifacts/                                   # Agile documents, defect tracker, and unit test files
.env                                                    # Contains secret keys
.gitignore                                              # Ignored files and folders for Git
add_missing_data.py                                     # Performs data interpolation for accurate detection
main.py                                                 # Main file to generate initial detection CSV
requirements.txt                                        # Project dependencies
visualize.py                                            # Visualizes video using interpolated data
```

## Features

- Automatic Number Plate Recognition (ANPR)
- Traffic classification and control (ATCC)
- Data interpolation for accurate detection and visualization
- Video output with annotated traffic information

## Technologies Used

- **Programming Language**: Python
- **Libraries**: listed in `requirements.txt`
- **Deep Learning**: Object detection models (e.g., YOLO)

## Setup Instructions

### Prerequisites

Ensure the following are installed:

- Python 3.8+
- Necessary Python libraries (listed in `requirements.txt`)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Saradhi0515/ANPR_And_ATCC_For_Smart_Traffic_Management_System.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ANPR_And_ATCC_For_Smart_Traffic_Management_System
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the `.env` file with your secret keys.

## Usage

1. Run `main.py` to generate the initial detection CSV file:
   ```bash
   python main.py
   ```
   - The generated CSV file will be saved in the `results/` directory.

2. Interpolate the data using `add_missing_data.py`:
   ```bash
   python add_missing_data.py
   ```
   - The interpolated CSV file will be saved in the `Interpolated_results/` directory.

3. Visualize the results using `visualize.py`:
   ```bash
   python visualize.py
   ```
   - The resulting video will be saved in the `output_videos/` directory.

## Output

You can view examples of the output or results generated by this project:

- [Output Video 1](https://drive.google.com/file/d/18kXH2gPBrXbENc6GSOcBSypdQme7qgPY/view?usp=sharing)
- [Output Video 2](https://drive.google.com/file/d/1htVjJBrTU6we8hHl2GbJXRxWiY0Vv5LZ/view?usp=sharing)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For any issues or inquiries, feel free to reach out via the [Issues](https://github.com/Saradhi0515/ANPR_And_ATCC_For_Smart_Traffic_Management_System/issues) section.
