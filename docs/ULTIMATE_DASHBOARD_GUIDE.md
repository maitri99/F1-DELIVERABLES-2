# 🏎️ F1 Steward AI - Ultimate Dashboard Guide

## Overview
The Ultimate Dashboard is a comprehensive web-based interface for visualizing, analyzing, and validating F1 incident detection results. It combines training metrics, detection results, ground truth comparisons, penalty analysis, and live inference capabilities.

## Features

### 1. **Overview Dashboard** 📊
- **Key Metrics Cards**: Total incidents, correct predictions, accuracy, average confidence
- **Class Distribution**: Bar chart showing detection counts per class
- **Penalty Distribution**: Pie chart of penalty types
- **Incident Timeline**: Interactive scatter plot of incidents by lap and confidence
- **Quick Stats**: Real-time accuracy and F1-score metrics

### 2. **Training Metrics** 📈
- **Loss Curves**: Train and validation loss over epochs
- **mAP Metrics**: mAP@50 and mAP@50-95 progression
- **Precision & Recall**: Performance tracking over training
- **Model Convergence**: F1-score progression with area fill
- **Training Statistics**: Final metrics display

### 3. **Detection Results** 🎯
- **Radar Chart**: Multi-dimensional performance view per class
- **Performance Table**: Precision, recall, F1-score, mAP for each class
- **Color-coded Performance**: Gradient visualization of metrics
- **Class Comparison**: Side-by-side class performance

### 4. **Penalty Analysis** ⚖️
- **Penalty Distribution**: Visual breakdown of penalty types
- **Confusion Matrix**: Predicted vs actual penalty heatmap
- **Penalty Breakdown Cards**: Detailed count and percentage per type
- **Decision Analysis**: Comparison of model predictions with FIA decisions

### 5. **Ground Truth Comparison** ✅
- **Incident Timeline**: Visual representation of prediction accuracy
- **Detailed Cards**: Full incident information including:
  - Race, lap, corner, drivers
  - Predicted vs ground truth penalties
  - FIA decision and violation type
  - Timestamp and confidence
- **Match Indicators**: Color-coded cards showing correct/incorrect predictions

### 6. **Performance Analytics** 📊
- **Inference Statistics**: Total frames, detections, FPS, confidence
- **Performance Comparison**: Grouped bar chart of metrics by class
- **Real-time Metrics**: Current processing statistics
- **Efficiency Analysis**: Frame processing and detection rates

### 7. **Live Inference** 🎥
- **Real-time Simulation**: Live detection metrics
- **Recent Detections Table**: Latest frames with classes and confidences
- **Live Confidence Chart**: Streaming visualization of detection confidence
- **FPS Monitoring**: Current processing speed

## Quick Start

### Option 1: Launch Script (Recommended)
```bash
cd ~/HACKATHON/F1_DELIVERABLES
chmod +x launch_ultimate_dashboard.sh
./launch_ultimate_dashboard.sh
```

### Option 2: Direct Streamlit
```bash
cd ~/HACKATHON/F1_DELIVERABLES
streamlit run code/ultimate_dashboard.py --server.port=8501
```

### Option 3: Custom Port
```bash
./launch_ultimate_dashboard.sh 8080  # Use port 8080
```

## Accessing the Dashboard

### Local Access
```
http://localhost:8501
```

### Network Access (from other devices)
```
http://<your-ip-address>:8501
```

To find your IP:
```bash
hostname -I | awk '{print $1}'
```

## Navigation

### Sidebar Controls
- **View Selector**: Radio buttons to switch between different views
- **Model Info**: Quick reference for model specifications
- **Quick Stats**: At-a-glance accuracy and F1-score metrics

### Main Content Area
- **Dynamic Views**: Content changes based on selected view
- **Interactive Charts**: Hover, zoom, pan on all visualizations
- **Responsive Layout**: Adapts to different screen sizes

## Visualizations Explained

### Training Curves
- **Purpose**: Monitor model learning progress
- **Metrics**: Loss, mAP, precision, recall, F1-score
- **Interpretation**: 
  - Decreasing loss = learning progress
  - Increasing mAP = better detection
  - Converging precision/recall = balanced model

### Class Distribution
- **Purpose**: Understand dataset composition
- **Display**: Bar chart with counts per class
- **Use Case**: Identify class imbalance, training focus areas

### Penalty Distribution
- **Purpose**: Visualize penalty decision patterns
- **Display**: Donut chart with percentages
- **Insights**: Common vs rare penalty types

### Incident Timeline
- **Purpose**: Track model performance across race events
- **Display**: Scatter plot with confidence bubbles
- **Color Coding**: 
  - Green = Correct prediction
  - Red = Incorrect prediction

### Confusion Matrix
- **Purpose**: Detailed accuracy analysis
- **Display**: Heatmap of predicted vs actual
- **Interpretation**: Diagonal = correct, off-diagonal = errors

### Radar Chart
- **Purpose**: Multi-metric class comparison
- **Display**: Polygon overlay per class
- **Use Case**: Identify strong/weak classes across metrics

## Data Sources

### Ground Truth Data
Location: `F1_DELIVERABLES/validation/ground_truth.json`
```json
{
  "incidents": [
    {
      "incident_id": "INC_001",
      "race": "Bahrain GP 2024",
      "lap": 23,
      "predicted_penalty": "Time Penalty",
      "ground_truth": "Time Penalty",
      "fia_decision": "5s Time Penalty"
    }
  ]
}
```

### Training Metrics
Location: `F1_DELIVERABLES/reports/analysis_report.json`
- Epoch-wise metrics
- Class-wise performance
- Validation results

### Inference Results
Location: `F1_DELIVERABLES/visualizations/`
- Detection images
- Performance charts
- Class distribution

## Customization

### Modify Data Source
Edit `ultimate_dashboard.py`:
```python
# Line ~100
def __init__(self, base_path):
    self.base_path = Path(base_path)
    # Modify paths as needed
```

### Change Theme Colors
Edit launcher script or dashboard directly:
```python
--theme.primaryColor="#FF1801"  # F1 Red
--theme.backgroundColor="#0E1117"  # Dark background
```

### Add Custom Metrics
In `generate_sample_data()`:
```python
# Add your custom metrics
'custom_metric': [values]
```

Then create visualization function:
```python
def create_custom_chart(data):
    fig = go.Figure()
    # Your chart code
    return fig
```

## Troubleshooting

### Dashboard Won't Start
```bash
# Check Python environment
which python
python --version

# Verify Streamlit installation
pip show streamlit

# Reinstall if needed
pip install --upgrade streamlit plotly
```

### Port Already in Use
```bash
# Use different port
./launch_ultimate_dashboard.sh 8502

# Or kill existing process
lsof -ti:8501 | xargs kill -9
```

### Missing Visualizations
```bash
# Ensure data directories exist
cd F1_DELIVERABLES
mkdir -p visualizations validation reports

# Check file permissions
ls -la visualizations/
```

### Slow Performance
- Reduce data points in sample generation
- Use pagination for large tables
- Enable caching:
```python
@st.cache_data
def load_data():
    # Your data loading code
```

## Integration with Other Tools

### Export Data from Dashboard
```python
# Add download buttons in dashboard
csv = df.to_csv(index=False)
st.download_button(
    label="Download CSV",
    data=csv,
    file_name='results.csv',
    mime='text/csv'
)
```

### Connect to Live Model
```python
# In Live Inference view, replace simulation with:
from inference import run_inference
results = run_inference(video_path)
```

### FastF1 Integration
```python
import fastf1
from fastf1_validator import F1RegulatoryValidator

validator = F1RegulatoryValidator()
session = fastf1.get_session(2024, 'Bahrain', 'R')
validation_results = validator.validate_predictions(predictions, session)
```

## Best Practices

### For Presentation
1. **Pre-load Data**: Have all visualizations ready before demo
2. **Test Navigation**: Practice switching between views smoothly
3. **Prepare Talking Points**: Note key insights for each view
4. **Have Backup**: Screenshot key visualizations in case of issues

### For Development
1. **Use Session State**: Cache expensive computations
2. **Modular Functions**: Keep visualization functions separate
3. **Error Handling**: Add try-except blocks for data loading
4. **Logging**: Use Streamlit's logging for debugging

### For Production
1. **Authentication**: Add login if deploying publicly
2. **Rate Limiting**: Prevent abuse on public servers
3. **Data Validation**: Sanitize all user inputs
4. **Monitoring**: Track usage and performance metrics

## Advanced Features

### Real-time Updates
```python
import time

placeholder = st.empty()
while True:
    with placeholder.container():
        # Update metrics
        st.metric("Live FPS", current_fps)
    time.sleep(1)
```

### Multi-page App
```python
# config.toml
[pages]
"Overview" = "pages/overview.py"
"Training" = "pages/training.py"
```

### Database Integration
```python
import sqlite3

conn = sqlite3.connect('incidents.db')
df = pd.read_sql_query("SELECT * FROM incidents", conn)
```

## Performance Optimization

### Caching
```python
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_training_data():
    return pd.read_csv('training_metrics.csv')
```

### Lazy Loading
```python
# Only load data when view is selected
if view == 'Training Metrics':
    data = load_training_data()
```

### Pagination
```python
page = st.number_input('Page', min_value=1, max_value=total_pages)
start_idx = (page - 1) * items_per_page
end_idx = start_idx + items_per_page
st.dataframe(df[start_idx:end_idx])
```

## API Reference

### Key Functions

#### `create_training_curves(data)`
Creates multi-subplot training visualization
- **Input**: Training metrics dictionary
- **Output**: Plotly figure object

#### `create_incident_timeline(incidents)`
Generates interactive timeline of incidents
- **Input**: List of incident dictionaries
- **Output**: Plotly scatter figure

#### `create_confusion_matrix()`
Builds penalty prediction confusion matrix
- **Input**: None (uses sample data)
- **Output**: Plotly heatmap figure

## Deployment Options

### Local Network
```bash
streamlit run ultimate_dashboard.py --server.address=0.0.0.0
```

### Streamlit Cloud (Public)
1. Push to GitHub
2. Visit share.streamlit.io
3. Connect repository
4. Deploy

### Docker Container
```dockerfile
FROM python:3.12-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "code/ultimate_dashboard.py"]
```

## Support & Resources

### Documentation
- Streamlit: https://docs.streamlit.io
- Plotly: https://plotly.com/python/
- FastF1: https://docs.fastf1.dev/

### Example Usage
See `SCRIPTS_GUIDE.md` for integration examples

### Contact
For hackathon support, refer to project documentation in `F1_DELIVERABLES/`

---

**🏎️ Happy Racing! May your predictions be accurate and your FPS be high!**
