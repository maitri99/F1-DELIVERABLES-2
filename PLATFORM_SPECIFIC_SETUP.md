# 💻 F1 AI Race Director - Platform-Specific Instructions

## 🖥️ Choose Your Operating System

- [Windows Instructions](#-windows-instructions)
- [macOS Instructions](#-macos-instructions)
- [Linux Instructions](#-linux-instructions)
- [Common Issues](#-common-issues-all-platforms)

---

## 🪟 Windows Instructions

### Prerequisites

1. **Install Python 3.8+**
   - Download from: https://www.python.org/downloads/
   - ✅ **IMPORTANT:** Check "Add Python to PATH" during installation!
   - Verify: Open Command Prompt and run `python --version`

2. **Install Git (Optional)**
   - Download from: https://git-scm.com/download/win
   - Or just download ZIP from GitHub

### Setup Steps

#### 1. Extract F1_DAY_1 folder
```cmd
# Extract to: C:\Users\YourName\F1_DAY_1
# Or any location you prefer
```

#### 2. Open Command Prompt
```cmd
# Press Windows Key + R
# Type: cmd
# Press Enter

# Navigate to folder:
cd C:\Users\YourName\F1_DAY_1
```

#### 3. Create Virtual Environment
```cmd
python -m venv f1_env
```

#### 4. Activate Virtual Environment
```cmd
f1_env\Scripts\activate
```
✅ You should see `(f1_env)` in your prompt

#### 5. Install Dependencies
```cmd
python -m pip install --upgrade pip
pip install -r requirements.txt
```
⏱️ Wait 3-5 minutes

#### 6. Run Dashboard
```cmd
streamlit run code\ultimate_dashboard.py
```

🎉 Browser opens at http://localhost:8501

### Windows-Specific Notes

**PowerShell Users:**
If using PowerShell instead of Command Prompt:
```powershell
# Activation command is different:
f1_env\Scripts\Activate.ps1

# If you get execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Then try activation again
```

**Path Separators:**
- Windows uses backslash `\`
- Commands: `code\ultimate_dashboard.py`

**Closing Dashboard:**
- Press `Ctrl+C` in Command Prompt
- Or close the Command Prompt window

---

## 🍎 macOS Instructions

### Prerequisites

1. **Python 3.8+ (Usually pre-installed)**
   ```bash
   python3 --version
   ```
   If not installed:
   - Download from: https://www.python.org/downloads/
   - Or use Homebrew: `brew install python3`

2. **Xcode Command Line Tools (Optional, for development)**
   ```bash
   xcode-select --install
   ```

### Setup Steps

#### 1. Extract F1_DAY_1 folder
```bash
# Extract to: ~/F1_DAY_1
# Or Downloads folder: ~/Downloads/F1_DAY_1
```

#### 2. Open Terminal
```bash
# Press Cmd+Space
# Type: Terminal
# Press Enter

# Navigate to folder:
cd ~/F1_DAY_1
# Or: cd ~/Downloads/F1_DAY_1
```

#### 3. Create Virtual Environment
```bash
python3 -m venv f1_env
```

#### 4. Activate Virtual Environment
```bash
source f1_env/bin/activate
```
✅ You should see `(f1_env)` in your prompt

#### 5. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
⏱️ Wait 3-5 minutes

#### 6. Run Dashboard
```bash
streamlit run code/ultimate_dashboard.py
```

🎉 Browser opens at http://localhost:8501

### macOS-Specific Notes

**M1/M2 Mac (Apple Silicon):**

If you have an M1/M2 Mac, PyTorch installation might need special steps:

```bash
# Option 1: Let it install automatically (works most of the time)
pip install -r requirements.txt

# Option 2: If above fails, install separately:
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
```

**GPU Acceleration on M1/M2:**
```python
# In code files, change device to:
device = 'mps'  # Instead of 'cuda' or 'cpu'
```

**Rosetta vs Native:**
- The project works on both Intel and Apple Silicon Macs
- Apple Silicon Macs are actually faster!

**Permission Issues:**
```bash
# If you get "Permission denied":
chmod +x code/*.py
```

---

## 🐧 Linux Instructions

### Prerequisites

1. **Python 3.8+**
   ```bash
   python3 --version
   ```
   
   If not installed:
   ```bash
   # Ubuntu/Debian:
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   
   # Fedora/RHEL:
   sudo dnf install python3 python3-pip
   
   # Arch:
   sudo pacman -S python python-pip
   ```

2. **Development Tools (Optional)**
   ```bash
   # Ubuntu/Debian:
   sudo apt install build-essential python3-dev
   
   # Fedora:
   sudo dnf groupinstall "Development Tools"
   ```

### Setup Steps

#### 1. Extract F1_DAY_1 folder
```bash
# Extract to: ~/F1_DAY_1
unzip F1_DAY_1.zip -d ~/
cd ~/F1_DAY_1
```

#### 2. Create Virtual Environment
```bash
python3 -m venv f1_env
```

#### 3. Activate Virtual Environment
```bash
source f1_env/bin/activate
```
✅ You should see `(f1_env)` in your prompt

#### 4. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
⏱️ Wait 3-5 minutes

#### 5. Run Dashboard
```bash
streamlit run code/ultimate_dashboard.py
```

🎉 Browser opens at http://localhost:8501

### Linux-Specific Notes

**CUDA/GPU Support:**

If you have NVIDIA GPU:
```bash
# Check CUDA availability:
nvidia-smi

# Install PyTorch with CUDA support:
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu118
# Then install rest:
pip install -r requirements.txt
```

**Headless Server (No GUI):**

Running on server without display:
```bash
# Run dashboard with network access:
streamlit run code/ultimate_dashboard.py --server.address 0.0.0.0

# Access from another computer:
http://SERVER_IP:8501
```

**Port Already in Use:**
```bash
# Check what's using port 8501:
sudo lsof -i :8501

# Kill it:
kill -9 PID

# Or use different port:
streamlit run code/ultimate_dashboard.py --server.port 8080
```

**System Python vs Virtual Environment:**
```bash
# Always activate virtual env first!
source f1_env/bin/activate

# Check you're using correct Python:
which python  # Should show: /path/to/F1_DAY_1/f1_env/bin/python
```

---

## 🔧 Common Issues (All Platforms)

### Issue 1: "python: command not found"

**Windows:**
```cmd
# Use 'python' instead of 'python3'
python --version
```

**Mac/Linux:**
```bash
# Use 'python3' instead of 'python'
python3 --version
```

### Issue 2: "pip: command not found"

**Windows:**
```cmd
python -m pip install --upgrade pip
```

**Mac/Linux:**
```bash
python3 -m pip install --upgrade pip
```

### Issue 3: Virtual Environment Won't Activate

**Windows (PowerShell):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
f1_env\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
# Make sure you're in F1_DAY_1 folder:
pwd
# Should show: /path/to/F1_DAY_1

# Try full path:
source ~/F1_DAY_1/f1_env/bin/activate
```

### Issue 4: Packages Won't Install

**All Platforms:**
```bash
# Clear pip cache
pip cache purge

# Try with no cache:
pip install -r requirements.txt --no-cache-dir

# Install one by one:
pip install ultralytics
pip install streamlit
pip install torch torchvision
pip install opencv-python pillow
pip install plotly pandas numpy
```

### Issue 5: "Port 8501 already in use"

**Windows:**
```cmd
# Find process using port:
netstat -ano | findstr :8501
# Kill it:
taskkill /PID <PID> /F

# Or use different port:
streamlit run code\ultimate_dashboard.py --server.port 8080
```

**Mac/Linux:**
```bash
# Find and kill process:
lsof -ti:8501 | xargs kill -9

# Or use different port:
streamlit run code/ultimate_dashboard.py --server.port 8080
```

### Issue 6: Browser Doesn't Open Automatically

**All Platforms:**

Manually open browser and go to:
```
http://localhost:8501
```

Or if you changed port:
```
http://localhost:8080
```

### Issue 7: "CUDA out of memory"

**All Platforms:**
```python
# Force CPU usage instead of GPU
# Edit code files and change:
device = 'cpu'  # Instead of 'cuda'
```

---

## 📊 System Requirements by Platform

### Windows
| Component | Minimum | Recommended |
|-----------|---------|-------------|
| OS | Windows 10 | Windows 10/11 |
| Python | 3.8+ | 3.10+ |
| RAM | 4GB | 8GB+ |
| Storage | 2GB | 5GB+ |
| GPU | Optional | NVIDIA GTX 1060+ |

### macOS
| Component | Minimum | Recommended |
|-----------|---------|-------------|
| OS | macOS 10.14+ | macOS 12+ |
| Chip | Intel/M1/M2 | M1/M2/M3 |
| Python | 3.8+ | 3.10+ |
| RAM | 4GB | 8GB+ |
| Storage | 2GB | 5GB+ |

### Linux
| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Distro | Ubuntu 20.04+ | Ubuntu 22.04+ |
| Python | 3.8+ | 3.10+ |
| RAM | 4GB | 8GB+ |
| Storage | 2GB | 5GB+ |
| GPU | Optional | NVIDIA GTX 1060+ |

---

## ✅ Platform-Specific Quick Commands

### Windows (Command Prompt)
```cmd
cd C:\Users\YourName\F1_DAY_1
python -m venv f1_env
f1_env\Scripts\activate
pip install -r requirements.txt
streamlit run code\ultimate_dashboard.py
```

### Windows (PowerShell)
```powershell
cd C:\Users\YourName\F1_DAY_1
python -m venv f1_env
f1_env\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run code\ultimate_dashboard.py
```

### macOS
```bash
cd ~/F1_DAY_1
python3 -m venv f1_env
source f1_env/bin/activate
pip install -r requirements.txt
streamlit run code/ultimate_dashboard.py
```

### Linux
```bash
cd ~/F1_DAY_1
python3 -m venv f1_env
source f1_env/bin/activate
pip install -r requirements.txt
streamlit run code/ultimate_dashboard.py
```

---

## 🎯 Next Steps

After successful setup on your platform:

1. ✅ Test with sample image
2. ✅ Upload your own F1 footage
3. ✅ Explore all dashboard features
4. ✅ Read advanced guides in `docs/`

**Happy F1 AI Racing! 🏁**

---

*Platform-specific help available in docs/ folder*
