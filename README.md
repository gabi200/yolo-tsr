
# Recunoastere semne de circulatie

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Georgescu Gabriel
**Data:** 21.11.2025

---

## Introducere

Acest proiect implementeaza un sistem de recunoastere a semnelor de circulatie implementat in Python, folosind in principal bibliotecile YOLO si OpenCV.

---

##  1. Structura Repository-ului Github 

```
project-name/
├── README.md
├── docs/
│   └── datasets/          # descriere seturi de date, surse, diagrame
├── data/
│   ├── raw/               # date brute
│   ├── processed/         # date curățate și transformate
│   ├── train/             # set de instruire
│   ├── validation/        # set de validare
│   └── test/              # set de testare
├── src/
│   ├── preprocessing/     # funcții pentru preprocesare
│   ├── data_acquisition/  # generare / achiziție date (dacă există)
│   └── neural_network/    # implementarea RN (în etapa următoare)
├── config/                # fișiere de configurare
└── requirements.txt       # dependențe Python (dacă aplicabil)
```

---

##  2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** Imagini de pe Google Maps, YouTube, alte surse publice
* **Modul de achiziție:** dataset public
* **Perioada / condițiile colectării:** Generat pe 19.02.2024

### 2.2 Caracteristicile dataset-ului

* **Număr total de observații:** 3253
* **Număr de caracteristici (features):** 2
* **Tipuri de date:** Imagini, Categoriale
* **Format fișiere:** PNG

### 2.3 Descrierea fiecărei caracteristici

| **Caracteristică** | **Tip** | **Unitate** | **Descriere** | **Domeniu valori** |
|-------------------|---------|-------------|---------------|--------------------|
| trafficsign_name | string | – | Numele semnului de circulatie | ex.: forb_left |
| category | categorial | – | Categoria semnului de circulatie: forb (interzicere), info (informare), mand (obligare), warn (avertizare)| {"forb", "info", "mand", "warn"} |

---

##  3. Analiza Exploratorie a Datelor (EDA)

### 3.1 Statistici descriptive aplicate

* **Distribuții pe caracteristici** (histograme)

### 3.2 Probleme identificate
- TODO
---

##  4. Preprocesarea Datelor

###  4.1 Transformarea caracteristicilor

* **Augumentarea datelor:** generare de caracteristici random (linii, patrate) pe imagini pentru a diversifica setul de date si a simula conditii reale. Dupa augumentare, s-a dublat setul de date, jumatate din total fiind generat.


### 4.2 Structurarea seturilor de date

**Împărțirea datelor:**
* 80% – train
* 10% – validation
* 10% – test

**Principii respectate:**
* Stratificare pentru clasificare
* Fără scurgere de informație (data leakage)
* Statistici calculate DOAR pe train și aplicate pe celelalte seturi

### 4.3 Salvarea rezultatelor preprocesării

* Datele preprocesate sunt salvate direct în folderul train
* Seturi train/val/test în foldere dedicate
