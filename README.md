<div align="center">
  <img src="https://media.tenor.com/E_2tP78jM6YAAAAj/website.gif" width="150px" alt="Navigation GIF">
  <h1>AI-Powered RFID Navigation Assistant for Visually Impaired</h1>
  <p>Empowering Independent Mobility Through Intelligent Location Sensing</p>
</div>

---

### 🌟 Project Overview

This project develops an **AI-powered navigation assistant** designed to enhance the independent mobility and safety of visually impaired individuals. By leveraging **RFID (Radio-Frequency Identification) technology** and intelligent processing, the system provides real-time, context-aware audio guidance, enabling users to navigate unfamiliar indoor and outdoor environments with confidence.

It's an end-to-end solution demonstrating the integration of hardware (RFID readers/tags), data processing, and AI to solve a critical accessibility challenge, built with considerations for real-world deployment and usability.

---

### ✨ Key Features & Functionality

* **Precise RFID-Based Localization:** Utilizes strategically placed RFID tags and a portable RFID reader to pinpoint the user's exact location within a mapped environment.
* **Intelligent Path Guidance:** An AI module processes location data and provides contextual, turn-by-turn audio instructions (e.g., "You are approaching a staircase, turn left for the elevator," or "Proceed straight for the exit").
* **Point-of-Interest (POI) Announcement:** Automatically announces nearby points of interest (e.g., "Restroom to your right," "Cafeteria ahead").
* **User-Friendly Interface:** Primarily audio-based for the visually impaired user, with a potential companion mobile app or dashboard for caretakers/administrators to manage maps and RFID tag locations.
* **AI-Powered Navigation:** The core intelligence processes RFID signals to determine precise location and provides real-time, dynamic navigation advice.

---

### 🚀 Architecture & Data Flow

The system is designed for robustness and responsiveness, integrating hardware with cloud-based intelligence.

**Key Components & Technologies:**

* **Hardware:** RFID Reader (e.g., **RC522 or similar UHF RFID reader**), RFID Tags, **Raspberry Pi** (Microcontroller/SBC), Audio Output Device.
* **Data Acquisition & Processing:**
    * **Python:** For scripting RFID reader interface and data processing on the edge device.
    * **Raspberry Pi OS:** For the edge compute platform.
    * **AWS IoT Core:** For streaming RFID data to the cloud for real-time ingestion.
* **Machine Learning / AI:**
    * **Python (Scikit-learn, TensorFlow/PyTorch if using Neural Networks):** For the navigation logic, potentially localization filtering or basic path prediction.
    * **Simple Machine Learning Models for pattern recognition / Rule-based AI for guidance:** For core AI decision-making.
    * **Google Text-to-Speech API:** For generating clear audio cues.
* **Cloud Backend:**
    * **AWS Lambda / API Gateway:** For serverless function execution of location processing and AI inference.
    * **AWS DynamoDB / RDS:** For storing map data, RFID tag locations, and user preferences.
    * **AWS S3:** For storing audio files or map assets.
* **Frontend (Optional for Admin/Caretaker):**
    * **[React / Next.js]:** For a web-based map management or monitoring dashboard.
* **MLOps & Deployment Considerations:**
    * **Docker:** For containerizing the AI inference module.
    * **AWS SageMaker / ECS:** For scalable deployment of the AI module.
    * **Git & GitHub:** For version control.

---

### ⚙️ Getting Started (Local Setup & Simulation)

To run a simulation or develop locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Navyansgr/AI-RFID-Navigation-Assistant.git](https://github.com/Navyansgr/AI-RFID-Navigation-Assistant.git)
    cd AI-RFID-Navigation-Assistant
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If `requirements.txt` doesn't exist, generate it after installing libs with `pip freeze > requirements.txt`)*
4.  **Hardware Setup (if applicable for physical testing):**
    * Connect your RFID reader (e.g., RC522) to your Raspberry Pi according to the circuit diagram in `docs/circuit_diagram.png`.
    * Ensure your Raspberry Pi is configured for network access.
5.  **Run the RFID Data Simulator (for local development/testing without hardware):**
    ```bash
    python src/hardware_simulator/rfid_stream_simulator.py
    ```
    *This will generate simulated RFID readings.*
6.  **Run the AI/Logic module locally:**
    ```bash
    python src/ai_navigation/main.py
    ```
    *This will process simulated/real RFID readings and output navigation commands/audio cues.*

---

### 📺 Demo

Check out a demo of the AI-Powered RFID Navigation Assistant in action:



---

### ⏭️ Future Enhancements

* **Advanced AI for Dynamic Environments:** Incorporate real-time obstacle avoidance using computer vision or ultrasonic sensors.
* **Personalized Routing:** Allow users to set preferences (e.g., avoid stairs, prefer specific routes).
* **Battery Optimization:** Develop power-saving modes for the portable reader and processing unit.
* **Crowdsourced Mapping:** Enable community contributions for mapping new environments.
* **Integration with Public Transit Data:** Provide guidance for bus stops, train stations etc.

---

### 👋 Connect With Me

* **GitHub Profile:** https://github.com/Navyansgr/
* **LinkedIn:**https://www.linkedin.com/in/navyashree-n-7bbab2280/

---

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=Navyansgr&style=flat-square&color=purple" alt="Project Views">
</div>
