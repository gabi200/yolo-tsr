import os
import sys

import torch
from ultralytics import YOLO

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "..", "app"))

from logger import get_logger

log = get_logger(__name__)

log.info("Started training module")


def main():
    # 1. Setup Device (GPU is highly recommended)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    log.info(f"Using device: {device}")
    print("Loading YOLOv9c model...")
    log.info("Loading YOLOv9c model...")
    model = YOLO("../models/yolov9m.pt")

    print("Starting training...")
    log.info("Starting training...")
    results = model.train(
        data="dataset_config.yaml",
        epochs=100,
        imgsz=640,
        device=device,
        batch=16,  # Adjust based on your GPU VRAM
        name="yolov9_traffic_signs",  # Name of the run folder
        patience=20,  # Early stopping patience
        plots=True,  # Save plots of training metrics
    )

    print("Validating model...")
    log.info("Validating model...")
    metrics = model.val()
    print(f"mAP50: {metrics.box.map50}")
    print(f"mAP50-95: {metrics.box.map}")
    log.info(f"mAP50: {metrics.box.map50}")
    log.info(f"mAP50-95: {metrics.box.map}")

    print("Running evaluation on Test set...")
    log.info("Running evaluation on Test set...")
    try:
        test_metrics = model.val(split="test")
        print(f"Test Set mAP50: {test_metrics.box.map50}")
        print(f"Test Set mAP50-95: {test_metrics.box.map}")
        log.info(f"Test Set mAP50: {test_metrics.box.map50}")
        log.info(f"Test Set mAP50-95: {test_metrics.box.map}")
    except Exception as e:
        print(
            f"Could not run test set evaluation (check if 'test' path exists in yaml). Error: {e}"
        )
        log.error(
            f"Could not run test set evaluation (check if 'test' path exists in yaml). Error: {e}"
        )

    # Export the model (optional)
    # model.export(format='onnx')


if __name__ == "__main__":
    # Required for Windows multiprocessing safety
    main()
