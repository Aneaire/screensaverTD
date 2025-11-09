#!/usr/bin/env python3
"""
Simple Anti-Idle Script
Prevents system from going idle using basic system commands.
Works without GUI libraries.
"""

import time
import subprocess
import random
import argparse
import sys

def simulate_activity():
    """Simulate user activity using system commands"""
    try:
        # Try different methods to simulate activity
        methods = [
            # Method 1: Simulate key press (requires xdotool)
            lambda: subprocess.run(['xdotool', 'key', 'Shift_L'], 
                                  capture_output=True, timeout=5),
            # Method 2: Move mouse slightly (requires xdotool)
            lambda: subprocess.run(['xdotool', 'mousemove', 
                                   '--', '100', '100'], 
                                  capture_output=True, timeout=5),
            # Method 3: Touch a temporary file to simulate activity
            lambda: open('/tmp/anti_idle_activity', 'w').close(),
        ]
        
        # Try each method until one works
        for method in methods:
            try:
                method()
                return True
            except (subprocess.TimeoutExpired, FileNotFoundError, PermissionError):
                continue
        
        # If all GUI methods fail, at least update the timestamp
        open('/tmp/anti_idle_activity', 'w').close()
        return True
        
    except Exception as e:
        print(f"Warning: Could not simulate activity: {e}")
        return False

def check_dependencies():
    """Check if required tools are available"""
    try:
        subprocess.run(['which', 'xdotool'], 
                       capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    parser = argparse.ArgumentParser(description='Prevent system idle using basic commands')
    parser.add_argument('-i', '--interval', type=int, default=30, 
                       help='Interval between movements in seconds (default: 30)')
    parser.add_argument('-d', '--duration', type=int, default=0,
                       help='Total duration to run in minutes (0 = run forever, default: 0)')
    
    args = parser.parse_args()
    
    print("Simple Anti-Idle Script Started")
    print(f"Interval: {args.interval} seconds")
    
    # Check if xdotool is available
    has_xdotool = check_dependencies()
    if has_xdotool:
        print("✓ xdotool found - will use keyboard/mouse simulation")
    else:
        print("⚠ xdotool not found - will use basic file activity")
        print("  Install with: sudo pacman -S xdotool")
    
    if args.duration > 0:
        print(f"Duration: {args.duration} minutes")
    else:
        print("Duration: Forever (press Ctrl+C to stop)")
    print("-" * 40)
    
    start_time = time.time()
    end_time = start_time + (args.duration * 60) if args.duration > 0 else float('inf')
    
    try:
        while time.time() < end_time:
            if simulate_activity():
                elapsed = int(time.time() - start_time)
                remaining = int(end_time - time.time()) if args.duration > 0 else 0
                
                if args.duration > 0:
                    print(f"Activity simulated. Elapsed: {elapsed//60}:{elapsed%60:02d}, Remaining: {remaining//60}:{remaining%60:02d}")
                else:
                    print(f"Activity simulated. Elapsed: {elapsed//60}:{elapsed%60:02d}")
            else:
                print("Failed to simulate activity")
            
            time.sleep(args.interval)
            
    except KeyboardInterrupt:
        print("\nScript stopped by user.")
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)
    
    print("Anti-Idle Script Ended")

if __name__ == "__main__":
    main()