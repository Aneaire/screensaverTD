#!/bin/bash
# Test script to detect system idle time

echo "Testing idle detection..."
echo "Start screensaver in another terminal, then run this"
echo "=================================================="

# Method 1: Check X11 idle time
if command -v xprintidle &> /dev/null; then
    echo "X11 idle time: $(xprintidle) ms"
else
    echo "xprintidle not found. Install with: sudo pacman -S xprintidle"
fi

# Method 2: Check last user input
echo "Last input time: $(cat /proc/uptime | cut -d' ' -f1) seconds"

# Method 3: Monitor activity file
if [ -f "/tmp/anti_idle_activity" ]; then
    echo "Screensaver activity file last modified: $(stat -c %Y /tmp/anti_idle_activity)"
    echo "Current time: $(date +%s)"
    echo "Time since last activity: $(($(date +%s) - $(stat -c %Y /tmp/anti_idle_activity))) seconds"
fi

echo ""
echo "Run this every 30 seconds while screensaver is active to see if idle resets"