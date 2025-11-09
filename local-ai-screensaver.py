#!/usr/bin/env python3
"""
Local AI-Powered Screensaver using Ollama
Runs completely offline with local LLM.
Requires: Ollama installed with a model (e.g., llama2, codellama)
"""

import time
import random
import subprocess
import argparse
import sys
import json
from datetime import datetime

class LocalAIScreensaver:
    def __init__(self, topic="software development", model="llama2", interval_range=(30, 90)):
        self.topic = topic
        self.model = model
        self.interval_range = interval_range
        self.activity_log = []
        
        # Check if Ollama is available
        try:
            subprocess.run(['ollama', '--version'], capture_output=True, check=True, timeout=5)
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            print("❌ Ollama not found. Install with: curl -fsSL https://ollama.ai/install.sh | sh")
            print("Then pull a model: ollama pull llama2")
            sys.exit(1)
    
    def generate_local_ai_content(self, activity_type):
        """Generate content using local Ollama AI"""
        prompts = {
            "coding": f"Generate 3-5 lines of realistic {self.topic} code. Only return the code, no explanations.",
            "writing": f"Write 2-3 sentences of professional {self.topic} content for an email. Be specific and realistic.",
            "commands": f"Generate 2-3 realistic command-line commands for {self.topic}. Only return the commands.",
            "documentation": f"Write 2-3 lines of technical documentation for {self.topic}. Be professional."
        }
        
        try:
            prompt = prompts.get(activity_type, prompts["coding"])
            result = subprocess.run([
                'ollama', 'run', self.model, prompt
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                raise Exception(f"Ollama error: {result.stderr}")
                
        except Exception as e:
            print(f"⚠️ Local AI generation failed: {e}")
            return self.get_fallback_content(activity_type)
    
    def get_fallback_content(self, activity_type):
        """Fallback content if AI fails"""
        fallbacks = {
            "coding": ["def analyze_data(data):", "results = process(data)", "return results"],
            "writing": ["The project timeline needs to be adjusted based on current progress.", "Please review the attached specifications."],
            "commands": ["git pull origin main", "npm test", "docker build -t app ."],
            "documentation": ["## Function Overview", "Processes input data and returns metrics.", "### Parameters"]
        }
        return random.choice(fallbacks.get(activity_type, fallbacks["coding"]))
    
    def simulate_typing(self, text, wpm=65):
        """Simulate realistic typing with variations"""
        lines = text.split('\n')
        for line in lines:
            if line.strip():
                for char in line:
                    # Variable typing speed
                    delay = random.uniform(55/wpm/60, 75/wpm/60)
                    time.sleep(delay)
                    
                    # Occasional typos and corrections
                    if random.random() < 0.04:
                        time.sleep(random.uniform(0.1, 0.3))  # Notice typo
                        time.sleep(random.uniform(0.2, 0.6))  # Correct
                
                # Pause between lines (thinking)
                time.sleep(random.uniform(0.8, 2.5))
            else:
                # Empty line pause
                time.sleep(random.uniform(0.3, 0.8))
    
    def simulate_mouse_movement(self, movements=3):
        """Simulate realistic mouse movements"""
        try:
            for _ in range(movements):
                subprocess.run(['xdotool', 'mousemove', 
                               '--', str(random.randint(150, 1100)), 
                               str(random.randint(150, 750))], 
                              capture_output=True, timeout=2)
                time.sleep(random.uniform(0.2, 0.8))
        except:
            pass
    
    def simulate_window_switch(self):
        """Simulate application switching"""
        try:
            # Alt+Tab to switch windows
            subprocess.run(['xdotool', 'key', 'Alt+Tab'], 
                          capture_output=True, timeout=2)
            time.sleep(random.uniform(0.5, 1.5))
        except:
            pass
    
    def perform_local_ai_activity(self):
        """Perform locally-generated AI activity"""
        activity_types = ["coding", "writing", "commands", "documentation"]
        activity_type = random.choice(activity_types)
        
        # Generate content using local AI
        content = self.generate_local_ai_content(activity_type)
        
        # Log activity
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.activity_log.append({
            "timestamp": timestamp,
            "type": activity_type,
            "ai_model": self.model,
            "local_ai": True
        })
        
        print(f"[{timestamp}] 🧠 Local AI ({self.model}) generated {activity_type} activity")
        
        # Simulate the activity
        self.simulate_typing(content)
        
        # Random additional behaviors
        if random.random() < 0.4:
            self.simulate_mouse_movement()
        
        if random.random() < 0.15:
            self.simulate_window_switch()
    
    def run(self, duration_minutes=0):
        """Main execution loop"""
        print(f"🧠 Local AI Screensaver Started")
        print(f"🤖 Using Ollama with model: {self.model}")
        print(f"📝 Topic: {self.topic}")
        print(f"⏱️  Interval range: {self.interval_range[0]}-{self.interval_range[1]} seconds")
        print(f"🌐 Completely offline - No internet required")
        
        if duration_minutes > 0:
            print(f"⏰ Duration: {duration_minutes} minutes")
        else:
            print("🔄 Duration: Forever (press Ctrl+C to stop)")
        print("-" * 60)
        
        start_time = time.time()
        end_time = start_time + (duration_minutes * 60) if duration_minutes > 0 else float('inf')
        
        try:
            while time.time() < end_time:
                self.perform_local_ai_activity()
                
                # Calculate next interval (unpredictable)
                next_interval = random.randint(*self.interval_range)
                elapsed = int(time.time() - start_time)
                
                if duration_minutes > 0:
                    remaining = int(end_time - time.time())
                    print(f"✅ Local AI activity complete. Next in {next_interval}s | Elapsed: {elapsed//60}:{elapsed%60:02d} | Remaining: {remaining//60}:{remaining%60:02d}")
                else:
                    print(f"✅ Local AI activity complete. Next in {next_interval}s | Elapsed: {elapsed//60}:{elapsed%60:02d}")
                
                time.sleep(next_interval)
                
        except KeyboardInterrupt:
            print("\n🛑 Local AI Screensaver stopped by user.")
        except Exception as e:
            print(f"❌ Error occurred: {e}")
            sys.exit(1)
        
        print("🏁 Local AI Screensaver Ended")
        print(f"📊 Total activities performed: {len(self.activity_log)}")

def main():
    parser = argparse.ArgumentParser(description='Local AI-powered screensaver using Ollama')
    parser.add_argument('-t', '--topic', type=str, default='software development',
                       help='Work topic for AI content generation')
    parser.add_argument('-m', '--model', type=str, default='llama2',
                       help='Ollama model to use (llama2, codellama, mistral, etc.)')
    parser.add_argument('-i', '--interval', type=int, nargs=2, default=[30, 90],
                       help='Interval range in seconds (min max, default: 30 90)')
    parser.add_argument('-d', '--duration', type=int, default=0,
                       help='Duration in minutes (0 = forever, default: 0)')
    
    args = parser.parse_args()
    
    ai_screensaver = LocalAIScreensaver(
        topic=args.topic,
        model=args.model,
        interval_range=tuple(args.interval)
    )
    
    ai_screensaver.run(duration_minutes=args.duration)

if __name__ == "__main__":
    main()