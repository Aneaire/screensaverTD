#!/usr/bin/env python3
"""
Real AI-Powered Screensaver using OpenAI API
Generates truly unique, contextual work content.
Requires: pip install openai
"""

import time
import random
import subprocess
import argparse
import sys
from datetime import datetime

try:
    import openai
except ImportError:
    print("❌ OpenAI library not installed. Install with: pip install openai")
    sys.exit(1)

class RealAIScreensaver:
    def __init__(self, topic="software development", api_key=None, interval_range=(30, 90)):
        self.topic = topic
        self.interval_range = interval_range
        self.activity_log = []
        
        if api_key:
            openai.api_key = api_key
        elif not openai.api_key:
            print("❌ OpenAI API key not found. Set OPENAI_API_KEY environment variable or use --api-key")
            sys.exit(1)
    
    def generate_ai_content(self, activity_type):
        """Generate content using real AI"""
        prompts = {
            "coding": f"Generate 3-5 lines of realistic {self.topic} code that a developer would actually write. Only return the code, no explanations.",
            "writing": f"Write 2-3 sentences of professional {self.topic} content that someone would type in an email or document. Make it realistic and specific.",
            "commands": f"Generate 2-3 realistic command-line commands related to {self.topic}. Only return the commands.",
            "documentation": f"Write 2-3 lines of technical documentation for {self.topic}. Make it professional and specific."
        }
        
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant generating realistic work content. Be concise and authentic."},
                    {"role": "user", "content": prompts.get(activity_type, prompts["coding"])}
                ],
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"⚠️ AI generation failed: {e}")
            return self.get_fallback_content(activity_type)
    
    def get_fallback_content(self, activity_type):
        """Fallback content if AI fails"""
        fallbacks = {
            "coding": ["def process_data(data):", "return data.strip()", "# TODO: Add validation"],
            "writing": ["Please review the attached document and provide feedback.", "Thank you for your consideration."],
            "commands": ["git status", "npm run build", "docker ps"],
            "documentation": ["## Overview", "This module handles data processing.", "### Usage"]
        }
        return random.choice(fallbacks.get(activity_type, fallbacks["coding"]))
    
    def simulate_typing(self, text, wpm=60):
        """Simulate realistic typing"""
        lines = text.split('\n')
        for line in lines:
            for char in line:
                delay = random.uniform(60/wpm/60, 80/wpm/60)
                time.sleep(delay)
                # Occasional typos
                if random.random() < 0.03:
                    time.sleep(random.uniform(0.2, 0.5))
            time.sleep(random.uniform(0.5, 2.0))
    
    def perform_ai_activity(self):
        """Perform AI-generated activity"""
        activity_types = ["coding", "writing", "commands", "documentation"]
        activity_type = random.choice(activity_types)
        
        # Generate AI content
        content = self.generate_ai_content(activity_type)
        
        # Log activity
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.activity_log.append({
            "timestamp": timestamp,
            "type": activity_type,
            "ai_generated": True
        })
        
        print(f"[{timestamp}] 🤖 AI-generated {activity_type} activity")
        
        # Simulate typing
        self.simulate_typing(content)
        
        # Occasional mouse movement
        if random.random() < 0.3:
            self.simulate_mouse_movement()
    
    def simulate_mouse_movement(self):
        """Simulate mouse movement"""
        try:
            subprocess.run(['xdotool', 'mousemove', 
                           '--', str(random.randint(100, 1200)), 
                           str(random.randint(100, 800))], 
                          capture_output=True, timeout=2)
        except:
            pass
    
    def run(self, duration_minutes=0):
        """Main execution loop"""
        print(f"🤖 Real AI Screensaver Started")
        print(f"🧠 Using OpenAI GPT-3.5 Turbo")
        print(f"📝 Topic: {self.topic}")
        print(f"⏱️  Interval range: {self.interval_range[0]}-{self.interval_range[1]} seconds")
        
        if duration_minutes > 0:
            print(f"⏰ Duration: {duration_minutes} minutes")
        else:
            print("🔄 Duration: Forever (press Ctrl+C to stop)")
        print("-" * 50)
        
        start_time = time.time()
        end_time = start_time + (duration_minutes * 60) if duration_minutes > 0 else float('inf')
        
        try:
            while time.time() < end_time:
                self.perform_ai_activity()
                
                next_interval = random.randint(*self.interval_range)
                elapsed = int(time.time() - start_time)
                
                if duration_minutes > 0:
                    remaining = int(end_time - time.time())
                    print(f"✅ AI activity complete. Next in {next_interval}s | Elapsed: {elapsed//60}:{elapsed%60:02d} | Remaining: {remaining//60}:{remaining%60:02d}")
                else:
                    print(f"✅ AI activity complete. Next in {next_interval}s | Elapsed: {elapsed//60}:{elapsed%60:02d}")
                
                time.sleep(next_interval)
                
        except KeyboardInterrupt:
            print("\n🛑 Real AI Screensaver stopped by user.")
        except Exception as e:
            print(f"❌ Error occurred: {e}")
            sys.exit(1)
        
        print("🏁 Real AI Screensaver Ended")

def main():
    parser = argparse.ArgumentParser(description='Real AI-powered screensaver using OpenAI')
    parser.add_argument('-t', '--topic', type=str, default='software development',
                       help='Work topic for AI content generation')
    parser.add_argument('-k', '--api-key', type=str,
                       help='OpenAI API key (or set OPENAI_API_KEY env var)')
    parser.add_argument('-i', '--interval', type=int, nargs=2, default=[30, 90],
                       help='Interval range in seconds (min max, default: 30 90)')
    parser.add_argument('-d', '--duration', type=int, default=0,
                       help='Duration in minutes (0 = forever, default: 0)')
    
    args = parser.parse_args()
    
    ai_screensaver = RealAIScreensaver(
        topic=args.topic,
        api_key=args.api_key,
        interval_range=tuple(args.interval)
    )
    
    ai_screensaver.run(duration_minutes=args.duration)

if __name__ == "__main__":
    main()