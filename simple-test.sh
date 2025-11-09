#!/bin/bash
# Simple test to verify screensaver activity

echo "Screensaver Activity Test"
echo "========================"
echo "1. Start screensaver: ./screensaver.py -d 2 -i 5"
echo "2. Watch for activity messages"
echo "3. Check /tmp/anti_idle_activity file updates"
echo ""

# Monitor the activity file
echo "Monitoring activity file (Ctrl+C to stop):"
while true; do
    if [ -f "/tmp/anti_idle_activity" ]; then
        echo "$(date): Activity file updated - Screensaver is working!"
        stat -c "Last modified: %y" /tmp/anti_idle_activity
    else
        echo "$(date): Waiting for activity file..."
    fi
    sleep 3
done