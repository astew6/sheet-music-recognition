import json
import cv2
import os
from ultralytics import YOLO

# === Configurable ===
image_path = "C:\\Users\\alexa\\Downloads\\detector\\5.png"
models_folder = "C:\\Users\\alexa\\Downloads\\detector\\models"
output_json = "C:\\Users\\alexa\\Downloads\\detector\\detections_combined.json"
CONFIDENCE_THRESHOLD = 0.002  # Only include detections above this confidence

# === Load Image ===
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError(f"Image not found: {image_path}")
height, width, _ = image.shape

# === Prepare Output ===
output = {}
detection_id = 0

# === Iterate Through Models ===
for model_file in os.listdir(models_folder):
    if model_file.endswith(".pt"):
        label = os.path.splitext(model_file)[0]  # Get filename without extension
        model_path = os.path.join(models_folder, model_file)

        try:
            model = YOLO(model_path)
            results = model(image_path)[0]
        except Exception as e:
            print(f"Error loading or using model {model_file}: {e}")
            continue

        for box in results.boxes:
            conf = float(box.conf[0])
            if conf < CONFIDENCE_THRESHOLD:
                continue  # Skip low-confidence detections

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            output[str(detection_id)] = {
                "label": label,
                "x": x1,
                "y": y1,
                "width": x2 - x1,
                "height": y2 - y1,
                "confidence": round(conf, 4)
            }
            detection_id += 1

# === Save Output ===
with open(output_json, "w") as f:
    json.dump(output, f, indent=2)

print(f"Detection complete. Results saved to {output_json}")
5