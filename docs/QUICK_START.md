# 🚀 QUICK START - F1 Steward AI Dashboard

## Instant Setup (30 seconds)

```bash
# 1. Activate environment
source /home/dell/f1_steward_env/bin/activate

# 2. Go to project
cd /home/dell/HACKATHON/F1_DELIVERABLES

# 3. Launch dashboard
streamlit run code/ultimate_dashboard.py
```

**Dashboard opens at:** http://localhost:8501

---

## 📸 Image Analysis (Single Frame)

1. **Click:** 🚨 Live Penalty Predictor (sidebar)
2. **Upload:** Image (JPG/PNG) of F1 incident
3. **Click:** "ANALYZE FOR PENALTY" button
4. **Get:** Instant decision with reasoning

**Example Decision:**
```
🚨 PENALTY ISSUED
Decision: Time Penalty
Reasoning: Track Limits detected near car with 87.3% confidence
Cars: 3 in frame, 1 violation associated with Car #1
```

---

## 🎬 Video Analysis (Frame-by-Frame)

1. **Click:** 🎬 Video Analysis (sidebar)
2. **Upload:** Video (MP4/AVI/MOV) of incident
3. **Set:** Max frames slider (300 = ~10 seconds)
4. **Click:** "START VIDEO ANALYSIS" button
5. **Wait:** ~2-5 seconds per second of video
6. **Get:** Clear verdict

**Example Verdict:**
```
🚨 FINAL VERDICT: PENALTY ISSUED

Incident #1
⏱️ Timestamp: 4.83 seconds
🎬 Frame: 145
⚖️ Decision: Time Penalty
🏎️ Cars: 3 in frame

Violation: Track Limits (87.3%)
Car #1: RESPONSIBLE (violation overlap 67%)
Car #2: Clean
Car #3: Clean

[Annotated frame showing violation]
```

---

## 🏎️ Multi-Car Analysis

The system automatically:
- ✅ Detects ALL cars in frame
- ✅ Identifies violations (Track Limits, Collision, etc.)
- ✅ Associates violations with specific cars using:
  - Distance between centers (< 100 pixels)
  - Bounding box overlap (IoU > 10%)
- ✅ Shows which car is responsible

**No confusion with multiple cars!**

---

## 📊 What You'll See

### For Images:
```
Decision Card (color-coded):
├─ 🚨 PENALTY (red) or ✅ NO PENALTY (blue)
├─ Severity level
├─ Detection summary (cars, violations)
├─ Primary violation details
├─ Reasoning
└─ Annotated image with bounding boxes
```

### For Videos:
```
Final Verdict:
├─ 🚨 PENALTY or ✅ NO PENALTY
├─ For each incident:
│   ├─ Frame number
│   ├─ Timestamp
│   ├─ Decision type
│   ├─ Cars involved
│   ├─ Which car responsible
│   └─ Why
├─ Visual evidence (annotated frames)
└─ Download decision (JSON)
```

---

## 💡 Tips for Best Results

### Image Upload:
- ✅ Clear view of incident
- ✅ Multiple cars visible OK (system handles it!)
- ✅ Good lighting
- ✅ PNG/JPG format (transparency auto-converted)

### Video Upload:
- ✅ MP4 recommended (also AVI, MOV)
- ✅ Short clips (5-20 seconds) for fast results
- ✅ Adjust max_frames slider:
  - 150 frames = 5 seconds
  - 300 frames = 10 seconds (default)
  - 600 frames = 20 seconds
- ✅ Clear incident footage

---

## 🔍 Understanding Decisions

### Penalty Thresholds:
| Violation | Confidence Needed | Decision |
|-----------|------------------|----------|
| Track Limits | 75% | Time Penalty |
| Collision | 70% | Time/Grid Penalty |
| Unsafe Release | 65% | Fine/Time Penalty |
| Flag Violation | 80% | Grid Penalty |
| Pit Lane Speed | 75% | Time Penalty |

### Spatial Association:
- **"Center"** = Violation overlaps car (IoU > 50%)
- **"Near"** = Violation close to car (distance < 100px or IoU 10-50%)

---

## 📥 Export Options

### Image Analysis:
- View annotated image in dashboard
- No export needed (instant decision)

### Video Analysis:
- Click "Download Decision" button
- Gets JSON with:
  - Verdict (PENALTY / NO PENALTY)
  - All incidents (frame, timestamp, car, violation)
  - Summary statistics

---

## ⚡ Performance

### Speed:
- **Image:** < 1 second per image
- **Video:** ~2-5 seconds per second of footage
- **GPU:** Faster if NVIDIA GPU available (auto-detected)

### Limits:
- **Max video frames:** 600 (configurable)
- **Max video length:** ~20 seconds recommended
- **Longer videos:** Increase max_frames slider

---

## 🐛 Troubleshooting

### Model not loading:
```bash
# Check model exists
ls -lh model/best.pt

# Should see: model/best.pt (85MB+)
```

### Video processing slow:
- Reduce max_frames slider
- Use shorter video clips
- Check GPU availability

### Wrong car blamed:
- System uses bounding box overlap
- Check if violation is clearly within/near car
- Multi-car incidents may show multiple cars involved

---

## 🎯 Example Workflows

### Workflow 1: Quick Image Check
```
1. Screenshot from race broadcast
2. Upload to Live Penalty Predictor
3. Get instant verdict (< 1 second)
4. Show reasoning and confidence
```

### Workflow 2: Video Incident Review
```
1. Extract 10-second clip of incident
2. Upload to Video Analysis
3. Wait ~20-30 seconds for processing
4. Get frame-by-frame verdict
5. See which car at which timestamp
6. Download decision for record
```

### Workflow 3: Multi-Car Collision
```
1. Upload video of 3-car collision
2. System analyzes all cars
3. Shows:
   - Car #1: 2 violations (PRIMARY)
   - Car #2: 1 violation (also involved)
   - Car #3: 0 violations (innocent)
4. Clear decision with evidence
```

---

## 📱 Dashboard Navigation

**Sidebar Menu:**
- 📊 Overview - Model performance and stats
- 🎯 Training Analysis - Training curves and metrics
- 🔍 Predictions - Prediction gallery
- ✅ Ground Truth - Validation data
- 📈 Visualizations - Performance charts
- 🚨 Live Penalty Predictor - **IMAGE ANALYSIS**
- 🎬 Video Analysis - **VIDEO ANALYSIS**

---

## ✅ System Status Check

```bash
# Run verification test
python3 test_dashboard.py

# Should show:
# ✅ PASS: Imports
# ✅ PASS: Model Loading
# ✅ PASS: Function Definitions
# ✅ PASS: File Structure
```

---

## 🎉 Ready to Use!

The dashboard is **production-ready** with:
- ✅ Clear penalty decisions (not complex reports)
- ✅ Multi-car spatial analysis
- ✅ Frame and timestamp identification
- ✅ Visual evidence with annotations
- ✅ Simple export format

**Perfect for demo day and real steward decisions!**

---

## 📞 Quick Reference

**Start Dashboard:**
```bash
streamlit run code/ultimate_dashboard.py
```

**URL:** http://localhost:8501

**For Help:** Check sidebar documentation or hover over ℹ️ icons

**For Issues:** See FINAL_IMPLEMENTATION_SUMMARY.md

---

**🏎️ Happy Stewarding! 🏁**
