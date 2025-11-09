#!/home/aneaire/Work/screensaver/venv/bin/python
"""
Anti-Idle Script
Prevents system from going idle by simulating mouse movement.
Useful when you're on break but need to appear active.
"""

import time
import random
import pyautogui
import argparse
import sys

def move_mouse_slightly():
    """Move mouse cursor slightly to simulate activity"""
    # Get current mouse position
    x, y = pyautogui.position()
    
    # Move mouse by a small random offset (1-5 pixels)
    offset_x = random.randint(-5, 5)
    offset_y = random.randint(-5, 5)
    
    # Ensure we don't move outside screen bounds
    screen_width, screen_height = pyautogui.size()
    new_x = max(0, min(screen_width - 1, x + offset_x))
    new_y = max(0, min(screen_height - 1, y + offset_y))
    
    # Move mouse smoothly
    pyautogui.moveTo(new_x, new_y, duration=0.5)
    
    # Move back to original position after a short delay
    time.sleep(random.uniform(0.1, 0.3))
    pyautogui.moveTo(x, y, duration=0.5)

def main():
    parser = argparse.ArgumentParser(description='Prevent system idle by simulating mouse movement')
    parser.add_argument('-i', '--interval', type=int, default=30, 
                       help='Interval between movements in seconds (default: 30)')
    parser.add_argument('-d', '--duration', type=int, default=0,
                       help='Total duration to run in minutes (0 = run forever, default: 0)')
    
    args = parser.parse_args()
    
    print(f"Anti-Idle Script Started")
    print(f"Interval: {args.interval} seconds")
    if args.duration > 0:
        print(f"Duration: {args.duration} minutes")
    else:
        print("Duration: Forever (press Ctrl+C to stop)")
    print("-" * 40)
    
    # Safety check: fail-safe to stop mouse movement
    pyautogui.FAILSAFE = True
    
    start_time = time.time()
    end_time = start_time + (args.duration * 60) if args.duration > 0 else float('inf')
    
    try:
        while time.time() < end_time:
            move_mouse_slightly()
            elapsed = int(time.time() - start_time)
            remaining = int(end_time - time.time()) if args.duration > 0 else 0
            
            if args.duration > 0:
                print(f"Mouse moved. Elapsed: {elapsed//60}:{elapsed%60:02d}, Remaining: {remaining//60}:{remaining%60:02d}")
            else:
                print(f"Mouse moved. Elapsed: {elapsed//60}:{elapsed%60:02d}")
            
            time.sleep(args.interval)
            
    except KeyboardInterrupt:
        print("\nScript stopped by user.")
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)
    
    print("Anti-Idle Script Ended")

if __name__ == "__main__":
    main()