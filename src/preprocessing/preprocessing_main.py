import os
import shutil
from random import shuffle

from generate_bad_images import *

original_img_path = "../../data/raw"
target_img_path = "../../data/train"

# copy labels and original images
print("Copying labels...")
shutil.copytree(
    original_img_path + "/labels", target_img_path + "/labels", dirs_exist_ok=True
)

print("Copying original images...")
shutil.copytree(
    original_img_path + "/images", target_img_path + "/images", dirs_exist_ok=True
)

# generate labels for new images
for name in os.listdir(original_img_path + "/labels"):
    shutil.copyfile(
        original_img_path + "/labels/" + name,
        target_img_path + "/labels/" + "proc-" + name,
    )

# process images
print("Augmenting dataset...")
for name in os.listdir(original_img_path + "/images"):
    generate_bad_image(
        original_img_path + "/images/" + name,
        target_img_path + "/images/" + "proc-" + name,
    )

print("Done.")
