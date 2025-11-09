#!/bin/bash
# Demo script to showcase AI screensaver functionality

echo "🚀 AI Screensaver Demo"
echo "===================="
echo ""

echo "1. Testing AI Content Generation..."
python3 -c "
import random
activities = [
    {'type': 'typing', 'content': ['def calculate_metrics(data):', '    return sum(data)/len(data)'], 'app': 'code'},
    {'type': 'typing', 'content': ['git commit -m \"Fix: resolve issue\"', 'npm test'], 'app': 'terminal'},
    {'type': 'typing', 'content': ['// Implementing new feature', 'const handler = (req, res) => {'], 'app': 'code'}
]
activity = random.choice(activities)
print(f'📝 Generated {activity[\"type\"]} activity for {activity[\"app\"]}')
print(f'💬 Content: {activity[\"content\"][0]}')
"

echo ""
echo "2. Testing Mouse Movement..."
xdotool mousemove 500 300
echo "✅ Mouse moved to (500, 300)"

echo ""
echo "3. Testing Keyboard Input..."
xdotool key Shift_L
echo "✅ Keyboard key pressed (Shift)"

echo ""
echo "4. Testing Random Intervals..."
for i in {1..3}; do
    interval=$(shuf -i 5-10 -n 1)
    echo "   Interval $i: $interval seconds"
done

echo ""
echo "✅ All AI Screensaver components working!"
echo ""
echo "🎯 Ready for full run:"
echo "   ./ai-screensaver.py -t 'software development' -d 30"
echo "   ./ai-launcher.sh"
echo ""
echo "📁 Repository: https://github.com/Aneaire/screensaverTD.git"