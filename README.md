# 🩺 Decoding Acne-Automated Facial Acne Detection

A Deep Learning–based web application that detects and classifies different types of facial acne using a trained YOLO model.

🚀 **Live Demo:**  
👉 https://huggingface.co/spaces/Nikhita070707/testing_acne_detector
<img width="866" height="857" alt="image" src="https://github.com/user-attachments/assets/2a4b0b7b-38af-4dea-9baf-9215fc8bb505" />

---

## 📌 Project Overview

**Decoding Acne** is a skin analysis system that:

- Detects acne regions in facial images  
- Classifies acne types  
- Counts occurrences of each type  
- Displays bounding boxes visually  
- Provides acne type summaries
- Displays overall acne severity analysis: No, Low, Moderate, High, based on number of acne.

This project combines **Computer Vision, Deep Learning, and Web Deployment** using Docker on Hugging Face Spaces.

---

## 🧠 Model Details

- **Model:** YOLO (Ultralytics)  
- **Framework:** PyTorch  
- **Custom trained acne detection dataset**  
- **Model file:** `backend/model/best.pt`

### 🔍 Detection Classes

- Blackheads  
- Whiteheads  
- Papules  
- Pustules  
- Nodules  
- Dark Spots  

---

## How to Use

1. Click **Choose File** to upload your facial image.
2. Click **Analyze Skin**.
3. Wait for the AI to detect acne (loading indicator will show).
4. Review the results on the canvas and summary section below.

---

## 🏗 Project Structure
├── backend/  
│ ├── model/  
│ │ └── best.pt  
│ ├── uploads/  
│ │ └── .gitkeep  
│ └── app.py  
│  
├── frontend/  
│ └── index.html  
│  
├── Dockerfile  
├── requirements.txt  
└── README.md

---

## ⚙️ How It Works

1. User uploads a facial image.
2. Image is sent to the `/predict` API endpoint.
3. Backend:
   - Saves image temporarily  
   - Runs YOLO inference  
   - Extracts bounding boxes  
   - Counts acne types  
4. Frontend:
   - Displays bounding boxes  
   - Shows acne summary cards
   - Shows acne severity analysis: No, Low, Moderate or High

---

## 🐳 Deploy on Hugging Face Spaces (Docker)

### Step 1: Create Space

1. Go to **Hugging Face**
2. Click **Create New Space**
3. Choose:
   - **SDK:** Docker  
   - **Visibility:** Public or Private  

---

### Step 2: Upload Files

Upload the following files and folders:

- `backend/`
- `frontend/`
- `Dockerfile`
- `requirements.txt`
- `README.md`

---

### Step 3: Required Configuration

In `Dockerfile`, make sure you expose port 7860:

```dockerfile
EXPOSE 7860
```

## 🧪 Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/nikhita5733/Decoding_Acne.git
cd Decoding_Acne
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```
▶ Activate Virtual Environment

### For Windows (Command Prompt):
```bash
venv\Scripts\activate
```
### For Git Bash:
```bash
source venv/Scripts/activate
```
### For Mac/Linux:
```bash
source venv/bin/activate
```
You should see (venv) appear in your terminal.

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Backend Server
```bash
python backend/app.py
```
### 5️⃣ Open in Browser
```bash
http://localhost:7860
```
---

## ⚠ Notes

- The `uploads/` folder stores temporary images.
- Hugging Face file system is temporary (ephemeral).
- Uploaded images are not permanently stored.

---

## 🔮 Future Improvements

- Acne severity grading system  
- Treatment recommendations module  
- Model optimization for faster inference  
- UI enhancement  
- Mobile-friendly version  

---

## ⚠ Disclaimer

This tool is intended for **educational and research purposes only**.  
It does not provide medical diagnosis or treatment advice.  
Consult a certified dermatologist for professional medical guidance.
