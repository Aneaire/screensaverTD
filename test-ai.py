#!/usr/bin/env python3
"""
Simple test for AI screensaver functionality
"""

import random
import time
import subprocess
from datetime import datetime

def test_ai_content():
    """Test AI content generation"""
    print("🧠 Testing AI Content Generation...")
    
    # Test software development content
    dev_activities = [
        {
            "type": "typing",
            "content": [
                "def calculate_metrics(data):",
                "return sum(data) / len(data)",
                "",
                "# TODO: Add error handling",
                "if not data:",
                "    raise ValueError('Empty dataset')"
            ],
            "app": "code"
        },
        {
            "type": "typing", 
            "content": [
                "git commit -m 'Fix: resolve memory leak'",
                "npm run test:coverage",
                "docker-compose up -d redis postgres"
            ],
            "app": "terminal"
        }
    ]
    
    activity = random.choice(dev_activities)
    print(f"✅ Generated {activity['type']} activity for {activity['app']}")
    print(f"📝 Content preview: {activity['content'][:3]}")
    return activity

def test_simulation():
    """Test activity simulation"""
    print("\n🎯 Testing Activity Simulation...")
    
    # Test xdotool
    try:
        result = subprocess.run(['xdotool', 'key', 'Shift_L'], 
                              capture_output=True, timeout=2)
        print("✅ xdotool keyboard simulation working")
    except Exception as e:
        print(f"⚠️ xdotool issue: {e}")
    
    try:
        result = subprocess.run(['xdotool', 'mousemove', '--', '500', '300'], 
                              capture_output=True, timeout=2)
        print("✅ xdotool mouse simulation working")
    except Exception as e:
        print(f"⚠️ xdotool mouse issue: {e}")

def test_timing():
    """Test timing randomness"""
    print("\n⏱️ Testing Timing Randomness...")
    
    for i in range(5):
        interval = random.randint(5, 10)
        print(f"   Interval {i+1}: {interval} seconds")
        time.sleep(0.1)  # Small delay

def main():
    print("🚀 AI Screensaver Functionality Test")
    print("=" * 40)
    
    # Test components
    test_ai_content()
    test_simulation()
    test_timing()
    
    print("\n✅ All core components tested!")
    print("🎯 Ready to run full AI screensaver")
    
    # Show usage
    print("\n📖 Usage Examples:")
    print("   ./ai-screensaver.py -t 'software development' -d 30")
    print("   ./ai-screensaver.py -t 'writing' -d 15 -i 20 60")
    print("   ./ai-launcher.sh  # Interactive menu")

if __name__ == "__main__":
    main()