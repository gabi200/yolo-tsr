# Traffic Sign Recognition – Real-Time CNN for ADAS 

High-performance traffic sign recognition system built for real-time automotive and ADAS applications.

Developed using **YOLO (PyTorch)** and deployed through a **Flask Web UI**, the system balances accuracy, robustness, and low inference latency.

---

##  Overview

Multi-class traffic sign detection system with:

- Real-time webcam detection  
- Image upload inference  
- Vehicle behavior simulation  
- Logging + FPS monitoring  
- Serial communication support  

**Classes:** 55  
**Total samples:** 7,634 (42.6% synthetic)  

---

##  Key Results

| Metric | Result |
|--------|--------|
| **Accuracy** | 95.7% |
| **F1-Score (Macro)** | 0.91 |
| **Precision** | 1.00 |
| **Recall** | 0.98 |
| **Latency** | 17.6 ms |

Real-time performance (<20 ms) with strong multi-class classification accuracy.

---

##  Model

- Architecture: **YOLOv9c**
- Trained from scratch (no pretrained weights)
- Optimizer: Adam  
- Learning Rate: 0.001  
- Batch Size: 8  
- Epochs: 8  
- Label Smoothing: 0.1  

Five structured optimization experiments performed.

---

## 🏗 System Structure

```
src/
├── data_acquisition/
├── preprocessing/
├── neural_network/
└── app/
```

Includes:

- Synthetic data generation (OpenCV-based augmentation)
- Training + optimization pipeline
- Flask-based real-time web interface
- ONNX export for deployment

---

## Run Application

```bash
python src/app/main.py
```

Train model:

```bash
python src/neural_network/train.py
```

GPU recommended.

---

##  Deployment

Exported model:

```
models/final_model.onnx
```

Suitable for edge / embedded automotive systems.

---

##  Limitations

- Some class imbalance  
- Confusion between similar speed limit signs  
- Limited extreme weather coverage  
- Model may require optimization for low-end hardware  

---

##  Future Work

- Data balancing improvements  
- Edge optimization (quantization / pruning)  
- Higher resolution training  
- Embedded hardware deployment  

---

**Author:** Gabriel Georgescu  
**Focus:** Automotive / ADAS  
