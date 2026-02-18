# 🏎️ F1 AI Race Director - Day 1 Production Release

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF.svg)](https://github.com/ultralytics/ultralytics)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B.svg)](https://streamlit.io)

## 🎯 What is This?

An **AI-powered Formula 1 penalty prediction system** that:
- 🔍 Detects F1 violations in real-time using YOLOv8
- 🏎️ Identifies which **specific car** committed the violation (multi-car support!)
- 📹 Analyzes race videos frame-by-frame
- ⚖️ Makes FIA-inspired penalty decisions
- 🎨 Beautiful interactive Streamlit dashboard

**Built for Nvidia-Dell Hackathon 2024**

---

## 🚀 Quick Start (60 Seconds!)

### 1. Clone & Setup
```bash
git clone https://github.com/Yashjadhav04/F1-DELIVERABLES.git
cd F1-DELIVERABLES

# Create virtual environment
python -m venv f1_env
source f1_env/bin/activate  # Windows: f1_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Dashboard
```bash
streamlit run code/ultimate_dashboard.py
```

### 3. Open Browser
Go to: `http://localhost:8501`

**That's it! 🎉**

---

## ✨ Key Features

### ✅ Multi-Car Penalty Detection
The system correctly identifies **which specific car** violated the rules in multi-car scenarios:

```
Input: 2 cars + 1 track limits violation

Output:
✅ Car #1: No penalty (racing cleanly)
🚨 Car #2: PENALTY - Track Limits (85% confidence)

Reasoning: "Car #2: Track Limits detected with 85.0% confidence.
            Penalty: Time Penalty. (2 cars in frame, only car #2 violated rules)"
```

### 🎬 Video Analysis
- Upload race videos
- Frame-by-frame penalty detection
- Temporal consistency tracking
- Incident timeline visualization

### 📊 Dashboard Tabs
1. **Overview** - Model performance & metrics
2. **Live Predictor** - Upload images for instant analysis
3. **Video Analysis** - Process race footage
4. **Training** - View model training progress
5. **Predictions** - Browse detection gallery

---

## 📁 Project Structure

```
F1_DAY_1/
├── code/
│   ├── ultimate_dashboard.py    # 🎨 Main Streamlit dashboard
│   ├── train_yolov8.py         # 🧠 Model training
│   ├── inference.py            # 🔍 Image inference
│   └── video_inference.py      # 📹 Video processing
├── model/
│   ├── best.pt                 # 🤖 Trained YOLOv8 model
│   └── yolov8n.pt             # 📦 Base model
├── data/
│   ├── Formula 1.v1i.yolov8/  # 📊 Dataset
│   └── sample_images/          # 🖼️ Test images
├── results/
│   ├── training/               # 📈 Training metrics
│   ├── predictions/            # 🎯 Prediction outputs
│   └── visualizations/         # 📊 Charts & graphs
├── docs/
│   ├── MULTI_CAR_FIX_COMPLETE.md
│   ├── FIX_VERIFIED.md
│   └── QUICK_TEST_GUIDE.md
├── requirements.txt            # 📦 Dependencies
└── README.md                   # 📖 This file
```

---

## 🎯 Detection Classes

- 🏎️ **Car** - F1 vehicles
- 🚧 **Track Limits** - Exceeding track boundaries  
- 💥 **Collision** - Car-to-car contact
- ⚠️ **Unsafe Release** - Pit lane violations
- 🏁 **Flag Violation** - Racing under flags
- ⏱️ **Pit Lane Speeding** - Speed limit violations

---

## 🔬 Model Performance

| Metric | Value |
|--------|-------|
| **mAP@0.5** | 92.3% |
| **Precision** | 88.7% |
| **Recall** | 85.4% |
| **Speed** | 45 FPS (GPU) / 5 FPS (CPU) |
| **Multi-Car Accuracy** | 100% ✅ |

---

## 💡 How It Works

### 1️⃣ Detection (YOLOv8)
```python
model = YOLO('model/best.pt')
results = model('race_incident.jpg')
```

### 2️⃣ Spatial Analysis (Per-Car)
```python
# For each car detected:
# - Calculate overlap with violations
# - Determine proximity
# - Associate violations with specific cars
```

### 3️⃣ Penalty Decision (FIA Rules)
```python
if violation_confidence >= threshold:
    if car_is_responsible:
        issue_penalty(car_number, violation_type)
```

### 4️⃣ Multi-Car Handling
- ✅ Each car analyzed independently
- ✅ Only penalize the violating car(s)
- ✅ Clear car numbering (Car #1, #2, #3...)

---

## 🧪 Testing

### Test Multi-Car Logic
```bash
python docs/test_multi_car_fix.py
```

**Expected Output:**
```
🎉 TEST PASSED! Multi-car logic working correctly!
✨ Your model is working perfectly!
   Only the violating car (Car #2) was penalized.
   Car #1 is correctly identified as racing cleanly.
```

### Test Dashboard Locally
```bash
streamlit run code/ultimate_dashboard.py
```

---

## 🌐 Deploy to Streamlit Cloud

### Option 1: Streamlit Cloud (Recommended)
1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub account
4. Select this repository
5. Set main file: `code/ultimate_dashboard.py`
6. Click **Deploy**!

### Option 2: Local Network Sharing
```bash
streamlit run code/ultimate_dashboard.py --server.address 0.0.0.0
# Access from other devices: http://YOUR_IP:8501
```

### Option 3: ngrok (Temporary Public URL)
```bash
# Terminal 1: Run dashboard
streamlit run code/ultimate_dashboard.py

# Terminal 2: Create public URL
ngrok http 8501
# Share the ngrok URL!
```

---

## 🎓 Training Your Own Model

```bash
python code/train_yolov8.py
```

Customize in `train_yolov8.py`:
- Epochs (default: 50)
- Batch size (default: 16)
- Image size (default: 640)
- Augmentation parameters

---

## 📚 Documentation

- **[Multi-Car Fix Guide](docs/MULTI_CAR_FIX_COMPLETE.md)** - How we fixed multi-car detection
- **[Fix Verification](docs/FIX_VERIFIED.md)** - Test results & validation
- **[Quick Test Guide](docs/QUICK_TEST_GUIDE.md)** - Testing checklist
- **[Dashboard Guide](docs/ULTIMATE_DASHBOARD_GUIDE.md)** - Full dashboard documentation

---

## 🐛 Troubleshooting

### Model Not Found?
```bash
# Download from releases or train your own
python code/train_yolov8.py
```

### Streamlit Import Error?
```bash
pip install --upgrade streamlit
```

### CUDA Not Available?
The system works on CPU too! Just slower (~5 FPS vs 45 FPS on GPU)

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 👥 Team

**Nvidia-Dell Hackathon 2024**

- **Developer**: Yash Jadhav
- **GitHub**: [@Yashjadhav04](https://github.com/Yashjadhav04)
- **Project**: F1 AI Race Director

---

## 🙏 Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) - Object detection
- [Streamlit](https://streamlit.io) - Dashboard framework
- [Roboflow](https://roboflow.com) - Dataset tools
- FIA - F1 penalty regulations

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file

---

## 📧 Support

- **Issues**: [GitHub Issues](https://github.com/Yashjadhav04/F1-DELIVERABLES/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Yashjadhav04/F1-DELIVERABLES/discussions)

---

## ⭐ Star This Repo!

If you find this project useful, please give it a star! ⭐

---

**Made with ❤️ for F1 and AI enthusiasts**

🏎️💨 *"Box box, box box... for an AI penalty prediction!"*
