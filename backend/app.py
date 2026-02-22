from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from ultralytics import YOLO
from collections import Counter
import os

# ------------------------
# Absolute paths (HF SAFE)
# ------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # /app/backend
FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "frontend"))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
MODEL_PATH = os.path.join(BASE_DIR, "model", "best.pt")

# ------------------------
# App setup
# ------------------------
app = Flask(__name__)
CORS(app)

# Load YOLO model
model = YOLO(MODEL_PATH)

LABEL_FIX = {
    "papuless": "papules",
    "whiteheadss": "whiteheads"
}

descriptions = {
    "blackheads": "Clogged pores with oil and dead skin.",
    "whiteheads": "Closed clogged pores.",
    "papules": "Small red bumps.",
    "pustules": "Pus-filled pimples.",
    "nodules": "Large painful lumps.",
    "dark spot": "Post acne pigmentation."
}

# ------------------------
# Frontend route (FIXED)
# ------------------------
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_frontend(path):
    return send_from_directory(FRONTEND_DIR, "index.html")

# ------------------------
# Prediction route
# ------------------------
@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    img_path = os.path.join(UPLOAD_DIR, "test.jpg")
    request.files["image"].save(img_path)

    results = model(
        img_path,
        conf=0.03,
        iou=0.1,
        imgsz=1024,
        max_det=300
    )

    boxes = results[0].boxes
    if boxes is None or len(boxes) == 0:
        return jsonify({"detections": [], "counts": {}})

    detections = []
    labels = []

    for box in boxes:
        cid = int(box.cls[0])
        raw_label = model.names[cid]
        label = LABEL_FIX.get(raw_label, raw_label)

        detections.append({
            "label": label,
            "confidence": float(box.conf[0]),
            "bbox": list(map(float, box.xyxy[0]))
        })
        labels.append(label)

    counts = Counter(labels)

    summary = {
        k: {
            "count": int(v),
            "description": descriptions.get(k, "Skin condition detected.")
        }
        for k, v in counts.items()
    }

    return jsonify({
        "detections": detections,
        "counts": summary
    })

# ------------------------
# Run server (HF REQUIRED)
# ------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
