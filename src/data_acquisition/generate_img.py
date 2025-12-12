import os
import random
import sys

import cv2
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "..", "app"))

from logger import get_logger

log = get_logger(__name__)


def augument(image_path, output_path):
    log.info(f"Generating image from source img with path {image_path}...")
    img = cv2.imread(image_path)
    if img is None:
        return

    for _ in range(random.randint(4, 20)):
        pt1 = (random.randint(0, img.shape[1]), random.randint(0, img.shape[0]))
        pt2 = (random.randint(0, img.shape[1]), random.randint(0, img.shape[0]))
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        thickness = random.randint(3, 9)
        cv2.line(img, pt1, pt2, color, thickness)

    h, w, _ = img.shape
    top_left = (random.randint(0, w // 2), random.randint(0, h // 2))
    bottom_right = (
        top_left[0] + random.randint(15, 50),
        top_left[1] + random.randint(15, 50),
    )
    cv2.rectangle(img, top_left, bottom_right, (0, 0, 0), -1)

    cv2.imwrite(output_path, img)
    log.info(f"Written generated image to {output_path}...")
