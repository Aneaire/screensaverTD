# Screensaver Script

A simple Python script to prevent your system from going idle by simulating user activity. Perfect for when you're on break but need to appear active.

## Files Created

- `screensaver.py` - Basic screensaver script
- `ai-screensaver.py` - 🤖 AI-powered intelligent screensaver (recommended)
- `screensaver-advanced.py` - Advanced version with pyautogui (requires GUI environment)
- `screensaver-launcher.sh` - Basic interactive launcher
- `ai-launcher.sh` - 🤖 AI-powered launcher with topic selection
- `README.md` - This documentation
- `TIME_DOCTOR_ANALYSIS.md` - Time Doctor detection analysis
- `AI_COMPARISON.md` - AI vs Basic screensaver comparison

## Quick Start

### Option 1: 🤖 AI-Powered Launcher (Recommended)
```bash
./ai-launcher.sh
```

### Option 2: Basic Interactive Launcher
```bash
./screensaver-launcher.sh
```

### Option 3: Run AI Screensaver Directly
```bash
# 🤖 AI Screensaver (Recommended - Harder to detect)
./ai-screensaver.py -t "software development" -d 30

# Basic Screensaver
./screensaver.py -d 30

# Run forever (press Ctrl+C to stop)
./ai-screensaver.py -t "general"

# Custom interval (every 60 seconds)
./screensaver.py -i 60
```

## Usage Options

```bash
./screensaver.py [OPTIONS]

Options:
  -h, --help            Show help message
  -i, --interval SECONDS
                        Interval between activity simulations (default: 30)
  -d, --duration MINUTES
                        Total duration to run (0 = forever, default: 0)
```

## Examples

```bash
# Run for 15 minutes with 30-second intervals
./screensaver.py -d 15 -i 30

# Run for 2 hours with 1-minute intervals
./screensaver.py -d 120 -i 60

# Run forever with 45-second intervals
./screensaver.py -i 45
```

## How It Works

The script uses multiple methods to simulate activity:

1. **Primary**: Uses `xdotool` to simulate keyboard/mouse input
2. **Fallback**: Creates/modifies a temporary file to show system activity

## Requirements

- `xdotool` (automatically installed)
- Python 3 (comes with Arch Linux)

## Safety Features

- Non-intrusive mouse movements (small offsets)
- Keyboard simulation uses Shift key (minimal impact)
- Easy to stop with Ctrl+C
- No system modifications

## Troubleshooting

If the script shows "xdotool not found":
```bash
sudo pacman -S xdotool
```

## Notes

- The script is designed to be subtle and won't interfere with your work
- Activity is simulated every 30 seconds by default
- Perfect for short breaks when you've finished work
- Use responsibly and only when appropriate