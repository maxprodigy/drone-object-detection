# Drone Object Detection - COCO Dataset 

[Link To Dataset](https://www.kaggle.com/datasets/dasmehdixtr/drone-dataset-uav/data) 

## 📌 Project Overview
This project focuses on **annotating drones** using the **COCO dataset format** to train machine learning models for **drone detection**. The dataset consists of images with bounding box annotations, which can be used for **object detection models** like **YOLOv8, Faster R-CNN, or SSD**.

## 📂 Dataset Structure
The dataset is structured as follows:

```
📂 drone-object-detection
 ├── 📂 images/
 │   ├── 🖼️    
 ├── 📂 annotations/
 │   ├── result.json  # COCO annotations
 ├── 📜 README.md        # Project documentation
```

## 🖼️ Sample Annotations
The dataset contains labeled drone images with bounding boxes:

[Sample Annotation](https://github.com/maxprodigy/drone-object-detection/blob/main/images/sample.png) 

## 🚀 Features
✅ **COCO-format annotations** for easy integration with deep learning models  
✅ **Automated dataset splitting (train/test)**  
✅ **Bounding box visualization script included**  
✅ **Ready for training with YOLOv8, Faster R-CNN, or SSD**  

## 🔧 Setup & Usage
### Clone Repository
```
git clone https://github.com/yourusername/drone-object-detection.git
cd drone-object-detection
```

### Install Dependencies
```
pip install opencv-python matplotlib json
```

### Visualize Annotations
To see how the bounding boxes look on the images:
```
python visualize_annotations.py
```

### 4️⃣ Split Dataset into Train/Test
Run the script to automatically divide the dataset:
```
python dataset_split.py
```
 

## 👨‍💻 Author
📌 **[Peter Johnson]**  
📺 **LinkedIn:** [https://www.linkedin.com/in/peter-johnson-3a4074224/]  

