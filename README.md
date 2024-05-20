# ⚽ Football Match Analyzer

## 🎯 Project Overview

Welcome to the "Football Match Analysis" project! 🌟 This endeavor aims to delve into the intricacies of football matches using state-of-the-art computer vision methodologies. ⚽ Leveraging advanced techniques, we'll detect and track players, referees, and the football itself in video footage. 🎥 Utilizing the renowned YOLO (You Only Look Once) object detection model, known for its unparalleled accuracy and efficiency, we'll revolutionize match analysis. To ensure optimal performance, custom training tailored to our specific dataset will be conducted, guaranteeing precise and insightful results. 🎯

### 🌟 Key Features and Highlights

#### 1. Team Identification:

- Utilizing K-means clustering for pixel segmentation, we will distinguish and assign players to their respective teams based on the colors of their uniforms. This enables accurate analysis of team-specific metrics. 🎨

#### 2. Ball Control Measurement:

- By tracking the football and players' interactions with it, we will calculate the ball possession percentages for each team, providing insights into game dynamics and team performance. ⚽

#### 3. Player Movement Analysis:

- Implementing optical flow techniques, we will measure camera movement between frames. This allows us to accurately track player movements and adjust for camera panning and zooming. 🎥
- Through perspective transformation, we will convert pixel-based measurements to real-world distances in meters. This transformation accounts for the depth and perspective of the scene, offering a more realistic representation of player movements on the field. 🌐

#### 4. Speed and Distance Calculation:

- We will calculate the speed of players and the total distance they cover during the match. This data is crucial for assessing player performance, stamina, and overall contribution to the game. 🏃‍♂️

#### 5. Real-World Applications:

- The project addresses real-world challenges in sports analytics, making it relevant for both academic research and practical applications in sports management and coaching. 📈

## 🖼️ Demo

![Football Analysis System](https://drive.google.com/uc?id=1it9GltCm2mIwEQ27z3K9VPF_bGIa2E6y)

## Modules Used

The following modules are used in this project:

### 1. YOLO (You Only Look Once):

- An AI object detection model utilized for detecting and tracking players, referees, and football in the video. 👁️

### 2. K-means:

- A clustering algorithm used for pixel segmentation to detect the color of t-shirts, enabling the identification and assignment of players to their respective teams. 🎨

### 3. Optical Flow:

- A technique to measure camera movement between frames, ensuring accurate tracking of player movements by accounting for changes in the camera's position and orientation. 🎥

### 4. Perspective Transformation:

- A method to represent the scene's depth and perspective, converting pixel measurements into real-world distances (meters) for a more accurate analysis of player movements. 🌐

### 5. Speed and Distance Calculation:

- Algorithms to compute each player's speed and the total distance covered during the match, providing essential metrics for performance analysis. 🏃‍♂️

## 🚀 Installation

### 📋 Step-by-Step Instructions

To set up the "Football Analysis System" project locally, follow these step-by-step instructions:

1. 🍴 Clone the project repository from GitHub:

   ```
   git clone https://github.com/AkshaySatasiya/Football-Analysis-System.git
   ```

2. 📂 Navigate to the project directory:

   ```
   cd Football-Analysis-System
   ```

3. 🐍 Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   ```

4. 🔄 Activate the virtual environment:

5. 📦 Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

6. 🎬 Run the project:

   ```
   python main.py
   ```

   The project should now be up and running, ready to analyze football matches! 🎾✨

## 📋 Dependencies and Requirements

The "Football Match Analyzer" project has the following dependencies and requirements:

- 🐍 Python 3.10.0 or above
- 🔍 Ultralytics
- 🧠 TensorFlow
- 🔍 OpenCV
- 🧠 Keras
- 📊 NumPy
- 🌐 Roboflow
- 🛠 Supervision
- 📈 Matplotlib
- 🧪 Scikit-learn

These dependencies are listed in the `requirements.txt` file, which is used to install them automatically during the installation process. 📦

## 📜 License

Football Match Analyzer is released under the [MIT License](LICENSE), allowing you to freely use, modify, and distribute the project.

## 🙌 Acknowledgements

We would like to express our gratitude to the open-source community for their invaluable contributions and the amazing libraries that made this project possible.

---

Get ready to experience football like never before with Football Match Analyzer✨

If you have any questions or need further assistance, feel free to reach out. Happy analyzing! 😊
