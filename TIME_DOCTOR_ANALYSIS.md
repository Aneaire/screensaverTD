# Time Doctor Detection Methods Analysis

## 🔍 Investigation Summary

Based on analysis of Time Doctor 3.16.69 running on Linux, here are the key detection methods:

## 📊 Primary Detection Methods

### 1. **X11 Input Event Monitoring**
- **Library**: `libxcb-xinput.so` (X11 XInput extension)
- **What it monitors**: Raw keyboard and mouse events at the X11 level
- **Detection capability**: Can distinguish between real user input and simulated input

### 2. **Qt Input System**
- **Plugins**: 
  - `libqevdevkeyboardplugin.so` (Linux keyboard events)
  - `libqevdevmouseplugin.so` (Linux mouse events)
- **Level**: Low-level device event monitoring
- **Capability**: Monitors actual hardware input vs software-generated input

### 3. **Process Monitoring**
- **File**: `processmonitor.log`
- **Method**: Monitors running processes for known automation tools
- **Detection**: Identifies common mouse jiggler software by process name

### 4. **Input Pattern Analysis**
- **File**: `inputmonitor.log`
- **Method**: Analyzes timing and patterns of input events
- **Detection**: Identifies robotic, repetitive input patterns

## 🚨 How Mouse Jigglers Are Detected

### **Pattern-Based Detection**
1. **Regular Intervals**: Real human input is irregular; jigglers are perfectly timed
2. **Same Movement**: Jigglers often move the same distance/direction
3. **Lack of Context**: No accompanying keyboard activity or window focus changes

### **Technical Detection**
1. **Event Source**: Distinguishes between hardware events and software-generated events
2. **Process Names**: Detects common jigglers (MouseJiggler, AutoMouseMover, etc.)
3. **System Calls**: Monitors for automation libraries (xdotool, pyautogui patterns)

### **Behavioral Analysis**
1. **No Application Activity**: Mouse moves but no active window changes
2. **Constant Activity**: 24/7 activity without breaks looks suspicious
3. **Missing Keyboard**: Mouse-only activity without keyboard input

## 🛡️ Evasion Strategies (Theoretical)

### **Human-Like Patterns**
```python
# Instead of regular intervals:
random_interval = random.randint(15, 45)  # 15-45 seconds
random_movement = random.randint(1, 8)     # Variable movement
```

### **Mixed Input Simulation**
```python
# Simulate both mouse and keyboard
if random.choice([True, False]):
    simulate_mouse_movement()
else:
    simulate_keyboard_typing()
```

### **Application Context**
```python
# Switch between applications occasionally
if random.random() < 0.1:  # 10% chance
    switch_to_random_window()
```

### **Process Name Obfuscation**
```python
# Use generic process names
# Instead of "mouse_jiggler.py" → "system_helper.py"
```

## ⚠️ Current Script Vulnerabilities

Our `screensaver.py` script has several detectable characteristics:

1. **Perfect Timing**: Fixed intervals (every 30 seconds)
2. **Same Movement**: Identical mouse movements each time
3. **Single Input Type**: Only mouse, no keyboard simulation
4. **Process Name**: Contains "screensaver" which could be flagged
5. **No Context**: Mouse moves without window activity

## 🔧 Improved Anti-Detection Script

To create a more sophisticated script that's harder to detect:

```python
import random
import time
import subprocess

def human_like_activity():
    # Random intervals (20-60 seconds)
    interval = random.randint(20, 60)
    
    # Mix of activities
    activity_type = random.choice(['mouse', 'keyboard', 'both'])
    
    if activity_type == 'mouse':
        # Random mouse movement
        move_mouse_randomly()
    elif activity_type == 'keyboard':
        # Random key press
        press_random_key()
    else:
        # Both activities
        move_mouse_randomly()
        time.sleep(random.uniform(0.1, 0.5))
        press_random_key()
    
    # Occasionally switch windows
    if random.random() < 0.05:  # 5% chance
        switch_window()
    
    return interval
```

## 📈 Detection Risk Levels

| Method | Risk Level | Detectability |
|--------|------------|---------------|
| Basic Mouse Jiggler | 🔴 High | Easily detected |
| Our Current Script | 🟡 Medium | Pattern-based detection |
| Human-Like Script | 🟢 Low | Harder to detect |
| Manual Activity | ✅ None | Undetectable |

## 🎯 Recommendations

1. **Use Sparingly**: Only during legitimate breaks
2. **Add Variety**: Mix intervals and movement patterns
3. **Include Keyboard**: Simulate occasional keyboard activity
4. **Context Matters**: Switch between applications
5. **Monitor Logs**: Check Time Doctor logs for detection alerts

## ⚖️ Legal & Ethical Considerations

This analysis is for educational purposes only. Using such tools may violate:
- Company policies
- Employment agreements
- Local labor laws
- Time Doctor's terms of service

**Always use time tracking software ethically and as intended by your employer.**

---

*Analysis conducted on Time Doctor 3.16.69 Linux version. Detection methods may vary by version and platform.*