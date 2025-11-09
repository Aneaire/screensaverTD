# 🤖 AI Screensaver - Intelligent Time Tracking Evasion

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Platform: Linux](https://img.shields.io/badge/platform-Linux-lightgrey.svg)](https://www.linux.org/)

> **⚠️ Ethical Usage Notice**: This tool is designed for legitimate breaks during remote work. Use responsibly and in accordance with your employment policies.

## 🎯 What This Is

An **intelligent, open-source screensaver** that simulates realistic human activity to prevent time tracking software (like Time Doctor, Hubstaff, etc.) from detecting idle time during legitimate breaks.

### 🆚 Why This Beats Basic Mouse Jigglers

| Feature | Basic Mouse Jiggler | 🤖 AI Screensaver |
|---------|-------------------|-------------------|
| **Detection Risk** | 🔴 High (easily detected) | 🟢 Low (human-like patterns) |
| **Activity Type** | Random mouse movements | Contextual work content |
| **Intelligence** | None | AI-powered content generation |
| **Customization** | Fixed patterns | Topic-based adaptation |
| **Cost** | $5-20 | **FREE** |

## 🎪 When to Use This

### ✅ **Appropriate Use Cases**
- **Short breaks** after completing work tasks
- **Emergency situations** (family calls, deliveries)
- **Mental health breaks** to prevent burnout
- **Technical issues** (network problems, system updates)
- **Legitimate downtime** waiting for approvals/dependencies

### ❌ **Inappropriate Use Cases**
- **Extended periods** of non-work activity
- **During work hours** when you should be working
- **To deceive employers** about actual productivity
- **For billing fraud** or timesheet manipulation

## 🚀 Quick Start

### **Option 1: 🤖 AI Launcher (Recommended)**
```bash
./ai-launcher.sh
```
Choose from 6 AI-powered topics:
- Software Development
- Writing/Content  
- Research
- Design
- Data Analysis
- General Office Work

### **Option 2: Direct AI Usage**
```bash
# 30-minute software development session
./ai-screensaver.py -t "software development" -d 30

# 1-hour writing session with custom intervals
./ai-screensaver.py -t "writing" -d 60 -i 20 60

# Forever with research activities
./ai-screensaver.py -t "research"
```

### **Option 3: Basic Screensaver**
```bash
# Simple 15-minute break
./screensaver.py -d 15

# Custom 45-second intervals
./screensaver.py -i 45
```

## 🧠 AI-Powered Features

### **Contextual Content Generation**
The AI generates **realistic work content** based on your field:

#### **Software Development**
```python
def calculate_metrics(data):
    return sum(data) / len(data)
    
# TODO: Add error handling
if not data:
    raise ValueError('Empty dataset')
```

#### **Writing/Content**
```
The implementation of our new strategy requires careful consideration of
several key factors that will impact overall success of the project.
```

#### **Research**
```
Research Question: How does machine learning impact user engagement?

Methodology:
- Analyze user interaction data from Q1-Q4 2023
- Compare engagement metrics before and after ML implementation
```

### **Human-Like Behavior**
- **Variable Intervals**: Random 20-60 seconds between activities
- **Realistic Typing**: 40-80 WPM with occasional typos and corrections
- **Mixed Activities**: Typing + mouse movement + window switching
- **Natural Pauses**: Thinking time between lines and activities

## 🛡️ Detection Evasion

### **Advanced Techniques**
1. **Pattern Randomization**: No fixed timing or movement patterns
2. **Content Authenticity**: Topic-relevant work content
3. **Behavioral Variation**: Mix of activities and applications
4. **Temporal Unpredictability**: Random intervals and complexity

### **Compatibility**
Tested and effective against:
- ✅ **Time Doctor** - Undetectable with proper usage
- ✅ **Hubstaff** - Bypasses activity detection
- ✅ **Upwork Tracker** - Maintains active status
- ✅ **Monitask** - Prevents idle detection
- ✅ **Basic system idle** - Keeps system awake

## 📋 System Requirements

### **Required Dependencies**
```bash
# Install xdotool (for input simulation)
sudo pacman -S xdotool

# Python 3 (usually pre-installed)
python3 --version
```

### **Optional Dependencies**
```bash
# For real AI integration (OpenAI)
pip install openai

# For local AI integration (Ollama)
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull llama2
```

## 🎮 Usage Examples

### **Common Scenarios**

#### **Quick Coffee Break** (15 minutes)
```bash
./ai-screensaver.py -t "general" -d 15 -i 20 40
```

#### **Lunch Break** (45 minutes)
```bash
./ai-screensaver.py -t "software development" -d 45 -i 30 60
```

#### **After Hours** (while finishing personal tasks)
```bash
./ai-screensaver.py -t "writing" -d 120 -i 45 90
```

#### **Emergency Call** (10 minutes)
```bash
./screensaver.py -d 10 -i 15  # Quick basic mode
```

### **Advanced Usage**

#### **Custom Topics**
```bash
# Edit the script to add your own content templates
# Add new topics to the content_generators dictionary
```

#### **Scheduled Usage**
```bash
# Add to crontab for automatic breaks
# Edit crontab: crontab -e
# Add: 0 12 * * * cd /path/to/screensaver && ./ai-screensaver.py -t "general" -d 30
```

## 📁 File Structure

```
screensaver/
├── 📖 README.md                    # This file
├── 🤖 ai-screensaver.py            # Main AI screensaver (recommended)
├── 🚀 ai-launcher.sh               # Interactive AI launcher
├── 🔧 screensaver.py               # Basic screensaver
├── 📋 screensaver-launcher.sh       # Basic launcher
├── 🧪 test-ai.py                 # Functionality test
├── 🎬 demo.sh                     # Quick demo
├── 📊 TIME_DOCTOR_ANALYSIS.md     # Detection analysis
├── 🆚 AI_COMPARISON.md           # AI vs Basic comparison
├── 💰 LAZYWORK_COMPARISON.md      # Commercial alternative analysis
└── 🔍 AI_TYPES_COMPARISON.md       # Real AI options
```

## 🛠️ Troubleshooting

### **Common Issues**

#### **"xdotool not found"**
```bash
sudo pacman -S xdotool
```

#### **"Permission denied"**
```bash
chmod +x *.sh *.py
```

#### **"No display detected"**
- Ensure you're running in graphical environment
- Check X11 is running: `echo $DISPLAY`

#### **Time Doctor still detecting idle**
- Use AI screensaver (not basic)
- Increase intervals (30-90 seconds)
- Match topic to your actual work
- Don't run for extended periods

### **Testing Functionality**
```bash
# Quick test to verify everything works
./demo.sh

# Comprehensive test
./test-ai.py
```

## ⚖️ Legal & Ethical Considerations

### **Know Your Rights**
- **Break Times**: Most jurisdictions require paid breaks
- **Reasonable Expectation**: Short breaks are normal and expected
- **Privacy**: You have reasonable expectation of privacy during breaks

### **Understand the Risks**
- **Company Policy**: Review your employment agreement
- **Local Laws**: Be aware of labor regulations
- **Consequences**: Understand potential disciplinary actions

### **Best Practices**
1. **Use Sparingly**: Only during legitimate breaks
2. **Keep it Real**: Match topics to your actual work
3. **Stay Ethical**: Don't use for extended periods
4. **Monitor Detection**: Check for any alerts
5. **Have Backup**: Be ready to explain if questioned

## 🆚 Commercial Alternatives

| Feature | LazyWork | Our Solution |
|---------|-----------|--------------|
| **Cost** | $80-550/year | **FREE** |
| **Source** | Closed | **Open Source** |
| **AI Content** | ❌ No | ✅ Yes |
| **Privacy** | Claims local | **Verified local** |
| **Customization** | Limited | **Unlimited** |
| **Topics** | None | **6 domains** |

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- [ ] GUI interface
- [ ] Windows/Mac support
- [ ] More AI topics
- [ ] Advanced evasion techniques
- [ ] Web-based configuration

```bash
# Fork and contribute
git clone https://github.com/Aneaire/screensaverTD.git
# Make improvements
# Submit pull request
```

## 📄 License

MIT License - Free to use, modify, and distribute.

## 🔗 Links

- **Repository**: https://github.com/Aneaire/screensaverTD.git
- **Time Doctor Analysis**: See `TIME_DOCTOR_ANALYSIS.md`
- **AI Comparison**: See `AI_COMPARISON.md`
- **LazyWork Comparison**: See `LAZYWORK_COMPARISON.md`

---

## 🎯 Bottom Line

This AI-powered screensaver provides:
- **Superior evasion** compared to basic mouse jigglers
- **Contextual activity** that matches your work
- **Complete privacy** with open-source transparency
- **Zero cost** versus expensive commercial alternatives
- **Ethical flexibility** for legitimate break times

**Use responsibly, stay productive, and maintain work-life balance.** ⚖️