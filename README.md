🩺 Decoding Acne – Automated Facial Acne Detection

A Deep Learning–based web application that detects and classifies different types of facial acne using a trained YOLO model.

🚀 Live Demo:
https://huggingface.co/spaces/Nikhita070707/acne

📌 Project Overview

Decoding Acne is an AI-powered skin analysis system that:

Detects acne regions in facial images

Classifies acne types

Counts occurrences of each type

Displays bounding boxes visually

Provides acne type summaries

This project combines Computer Vision, Deep Learning, and Web Deployment using Docker on Hugging Face Spaces.

📸 Application Preview
Upload Interface

(Add this image inside an assets folder and rename it as upload.png)

![Upload Screen](assets/upload.png)
Detection Output

(Add detection result screenshot as result.png)

![Detection Result](assets/result.png)
🧠 Model Details

Model: YOLO (Ultralytics)

Framework: PyTorch

Custom trained acne detection dataset

Model file: backend/model/best.pt

Detection Classes

Blackheads

Whiteheads

Papules

Pustules

Nodules

Dark Spots

🏗 Project Structure
.
├── backend/
│   ├── model/
│   │   └── best.pt
│   ├── uploads/
│   │   └── .gitkeep
│   └── app.py
│
├── frontend/
│   └── index.html
│
├── Dockerfile
├── requirements.txt
└── README.md
⚙ How It Works

User uploads facial image.

Image is sent to /predict API.

Backend:

Saves image temporarily

Runs YOLO inference

Extracts bounding boxes

Counts acne types

Frontend:

Displays bounding boxes

Shows acne summary cards

🐳 Deployment – Hugging Face Spaces (Docker)
Create Space

Choose Docker SDK

Ensure port is 7860

Important Configuration

In app.py:

app.run(host="0.0.0.0", port=7860)

In Dockerfile:

EXPOSE 7860
🖥 Run Locally

Install dependencies:

pip install -r requirements.txt

Run application:

python backend/app.py

Open in browser:

http://localhost:7860
🔮 Future Improvements

Acne severity grading

Personalized skincare suggestions

Mobile optimization

Faster inference optimization

Dermatology dataset expansion

⚠ Disclaimer

This application is developed for educational and research purposes only.
It does not replace professional dermatological advice.
