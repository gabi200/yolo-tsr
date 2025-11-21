import os

from dotenv import load_dotenv
from roboflow import Roboflow

load_dotenv()

if os.getenv("ROBOFLOW_API_KEY") is None:
    raise ValueError("ROBOFLOW_API_KEY environment variable is not set")

rf = Roboflow(api_key=os.getenv("ROBOFLOW_API_KEY"))

# download dataset from Roboflow
project = rf.workspace("radu-oprea-r4xnm").project("traffic-signs-detection-europe")
version = project.version(14)
dataset = version.download("yolov9")
