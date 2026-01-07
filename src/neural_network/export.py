import os
import sys

from ultralytics import YOLO

# --- Configuration ---
# Path to your BEST trained weights.
# Adjust this path to where your training script saved the result.
# Example: '../custom_models/yolov9_traffic_signs/weights/best.pt'
MODEL_PATH = "../../saved_models/weights/best.pt"


def main():
    if not os.path.exists(MODEL_PATH):
        print(f"❌ Error: Model weights not found at: {MODEL_PATH}")
        print("Please update MODEL_PATH in the script.")
        return

    print(f"Loading model from: {MODEL_PATH}...")
    try:
        model = YOLO(MODEL_PATH)
        print("✅ Model loaded successfully.")
    except Exception as e:
        print(f"❌ Error loading YOLO model: {e}")
        return

    print("\nStarting export to ONNX...")
    try:
        # Export the model
        # opset=12 is widely compatible. dynamic=True allows variable input sizes.
        path = model.export(format="onnx", opset=12, dynamic=True)

        print(f"\n Success! Model exported to: {path}")
        print(
            "You can now use this .onnx file for inference in other frameworks (OpenCV, C++, C#, etc.)"
        )

    except Exception as e:
        print(f"\n❌ Export failed: {e}")


if __name__ == "__main__":
    main()
