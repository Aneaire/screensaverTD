#!/usr/bin/env python3
"""
AI-Powered Intelligent Screensaver
Uses AI to generate contextual, unpredictable work-related activity.
Much harder to detect than simple mouse jigglers.
"""

import time
import random
import subprocess
import json
import argparse
import sys
from datetime import datetime
import threading

class AIScreensaver:
    def __init__(self, topic="software development", interval_range=(20, 60)):
        self.topic = topic.lower()
        self.interval_range = interval_range
        self.activity_log = []
        
        # AI-generated content templates based on topic
        self.content_generators = {
            "software development": self.generate_dev_activity,
            "writing": self.generate_writing_activity,
            "research": self.generate_research_activity,
            "design": self.generate_design_activity,
            "data analysis": self.generate_data_activity,
            "general": self.generate_general_activity
        }
        
        # Common work applications to simulate
        self.applications = [
            "code", "terminal", "browser", "notes", "slack", "email",
            "documentation", "git", "docker", "database", "api", "testing"
        ]
        
    def generate_dev_activity(self):
        """Generate realistic software development activity"""
        activities = [
            {
                "type": "typing",
                "content": [
                    "def calculate_metrics(data):",
                    "return sum(data) / len(data)",
                    "",
                    "# TODO: Add error handling",
                    "if not data:",
                    "    raise ValueError('Empty dataset')",
                    "",
                    "class DataProcessor:",
                    "    def __init__(self, config):",
                    "        self.config = config",
                    "        self.cache = {}"
                ],
                "app": "code"
            },
            {
                "type": "typing",
                "content": [
                    "git commit -m 'Fix: resolve memory leak in data processing'",
                    "git push origin feature/performance-improvements",
                    "npm run test:coverage",
                    "docker-compose up -d redis postgres",
                    "kubectl apply -f deployment.yaml"
                ],
                "app": "terminal"
            },
            {
                "type": "typing",
                "content": [
                    "// Implementing new authentication middleware",
                    "const authMiddleware = (req, res, next) => {",
                    "  const token = req.headers.authorization?.split(' ')[1];",
                    "  if (!token) return res.status(401).json({ error: 'No token' });",
                    "  ",
                    "  try {",
                    "    const decoded = jwt.verify(token, process.env.JWT_SECRET);",
                    "    req.user = decoded;",
                    "    next();",
                    "  } catch (error) {",
                    "    res.status(401).json({ error: 'Invalid token' });",
                    "  }",
                    "};"
                ],
                "app": "code"
            }
        ]
        return random.choice(activities)
    
    def generate_writing_activity(self):
        """Generate realistic writing/editing activity"""
        activities = [
            {
                "type": "typing",
                "content": [
                    "The implementation of our new strategy requires careful consideration of",
                    "several key factors that will impact the overall success of the project.",
                    "First and foremost, we need to establish clear communication channels",
                    "between all stakeholders to ensure alignment and transparency.",
                    "",
                    "Additionally, the timeline should be realistic, accounting for potential",
                    "challenges and allowing for flexibility when unexpected issues arise."
                ],
                "app": "notes"
            },
            {
                "type": "typing",
                "content": [
                    "## Executive Summary",
                    "",
                    "This quarter's performance exceeded expectations with a 23% increase in",
                    "productivity and a 15% reduction in operational costs. The key drivers",
                    "behind this improvement include:",
                    "",
                    "- Automation of repetitive tasks",
                    "- Streamlined workflow processes", 
                    "- Enhanced team collaboration tools",
                    "- Data-driven decision making"
                ],
                "app": "documentation"
            }
        ]
        return random.choice(activities)
    
    def generate_research_activity(self):
        """Generate realistic research activity"""
        activities = [
            {
                "type": "typing",
                "content": [
                    "Research Question: How does machine learning impact user engagement?",
                    "",
                    "Methodology:",
                    "- Analyze user interaction data from Q1-Q4 2023",
                    "- Compare engagement metrics before and after ML implementation",
                    "- Control group: Users without ML features",
                    "- Sample size: 10,000 active users",
                    "",
                    "Expected outcomes:",
                    "- 15-20% increase in session duration",
                    "- Improved content relevance scores",
                    "- Higher conversion rates"
                ],
                "app": "notes"
            },
            {
                "type": "typing",
                "content": [
                    "SELECT user_id, session_duration, pages_visited, conversion_rate",
                    "FROM user_analytics",
                    "WHERE date BETWEEN '2023-01-01' AND '2023-12-31'",
                    "AND ml_features_enabled = true",
                    "GROUP BY user_id",
                    "ORDER BY session_duration DESC",
                    "LIMIT 1000;"
                ],
                "app": "database"
            }
        ]
        return random.choice(activities)
    
    def generate_design_activity(self):
        """Generate realistic design activity"""
        activities = [
            {
                "type": "typing",
                "content": [
                    "# Design System Updates",
                    "",
                    "## Color Palette",
                    "- Primary: #3B82F6 (Blue 500)",
                    "- Secondary: #10B981 (Emerald 500)", 
                    "- Accent: #F59E0B (Amber 500)",
                    "- Neutral: #6B7280 (Gray 500)",
                    "",
                    "## Typography",
                    "- Headings: Inter, 600 weight",
                    "- Body: Inter, 400 weight",
                    "- Code: JetBrains Mono"
                ],
                "app": "design"
            },
            {
                "type": "mouse",
                "description": "Adjusting design elements in Figma",
                "movements": 15,
                "app": "design"
            }
        ]
        return random.choice(activities)
    
    def generate_data_activity(self):
        """Generate realistic data analysis activity"""
        activities = [
            {
                "type": "typing",
                "content": [
                    "import pandas as pd",
                    "import numpy as np",
                    "import matplotlib.pyplot as plt",
                    "import seaborn as sns",
                    "",
                    "# Load and clean dataset",
                    "df = pd.read_csv('sales_data.csv')",
                    "df['date'] = pd.to_datetime(df['date'])",
                    "df = df.dropna()",
                    "",
                    "# Monthly sales trend",
                    "monthly_sales = df.groupby(df['date'].dt.to_period('M')).sum()",
                    "plt.figure(figsize=(12, 6))",
                    "sns.lineplot(data=monthly_sales, x='date', y='revenue')"
                ],
                "app": "code"
            },
            {
                "type": "typing",
                "content": [
                    "Key Insights from Q3 Analysis:",
                    "",
                    "1. Revenue growth: 18% YoY",
                    "2. Customer retention: 87% (up from 82%)",
                    "3. Average order value: $127.50 (+12%)",
                    "4. Top performing product: Enterprise Plan",
                    "5. Churn rate: 3.2% (industry average: 5.1%)"
                ],
                "app": "notes"
            }
        ]
        return random.choice(activities)
    
    def generate_general_activity(self):
        """Generate general office work activity"""
        activities = [
            {
                "type": "typing",
                "content": [
                    "Team Meeting Notes - " + datetime.now().strftime("%Y-%m-%d"),
                    "",
                    "Attendees: John, Sarah, Mike, Lisa",
                    "",
                    "Action Items:",
                    "- [ ] Review Q4 budget proposal (John)",
                    "- [ ] Update project timeline (Sarah)", 
                    "- [ ] Prepare client presentation (Mike)",
                    "- [ ] Schedule follow-up meeting (Lisa)",
                    "",
                    "Next meeting: Friday 2:00 PM"
                ],
                "app": "notes"
            },
            {
                "type": "typing",
                "content": [
                    "Email draft:",
                    "",
                    "Hi Team,",
                    "",
                    "I hope this email finds you well. I wanted to follow up on our",
                    "discussion from yesterday's meeting regarding the upcoming project",
                    "deadline.",
                    "",
                    "Based on our conversation, I've updated the timeline and would",
                    "appreciate your review and feedback by end of day tomorrow.",
                    "",
                    "Please let me know if you have any questions or concerns.",
                    "",
                    "Best regards,",
                    "[Your Name]"
                ],
                "app": "email"
            }
        ]
        return random.choice(activities)
    
    def get_activity_generator(self):
        """Get the appropriate activity generator for the topic"""
        for key, generator in self.content_generators.items():
            if key in self.topic:
                return generator
        return self.generate_general_activity
    
    def simulate_typing(self, text_lines, wpm=60):
        """Simulate realistic typing with variable speed"""
        for line in text_lines:
            # Type the line character by character
            for char in line:
                # Variable typing speed (40-80 WPM)
                delay = random.uniform(60/wpm/60, 80/wpm/60)  # Convert to seconds
                time.sleep(delay)
                
                # Occasional typos and corrections (5% chance)
                if random.random() < 0.05:
                    time.sleep(random.uniform(0.1, 0.3))  # Pause to notice typo
                    time.sleep(random.uniform(0.2, 0.5))  # Correction time
            
            # Pause between lines (thinking time)
            time.sleep(random.uniform(0.5, 2.0))
    
    def simulate_mouse_movement(self, movements=5):
        """Simulate realistic mouse movements"""
        try:
            for _ in range(movements):
                # Random mouse movement
                subprocess.run(['xdotool', 'mousemove', 
                               '--', str(random.randint(100, 1200)), 
                               str(random.randint(100, 800))], 
                              capture_output=True, timeout=2)
                time.sleep(random.uniform(0.1, 0.5))
        except (subprocess.TimeoutExpired, FileNotFoundError):
            # Fallback: just update activity file
            pass
    
    def simulate_window_switch(self):
        """Simulate switching between applications"""
        try:
            # Simulate Alt+Tab
            subprocess.run(['xdotool', 'key', 'Alt+Tab'], 
                          capture_output=True, timeout=2)
            time.sleep(random.uniform(0.5, 1.0))
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
    
    def perform_activity(self):
        """Perform a single AI-generated activity"""
        generator = self.get_activity_generator()
        activity = generator()
        
        # Log the activity
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.activity_log.append({
            "timestamp": timestamp,
            "type": activity["type"],
            "app": activity.get("app", "unknown")
        })
        
        print(f"[{timestamp}] Performing {activity['type']} activity in {activity.get('app', 'application')}")
        
        if activity["type"] == "typing":
            self.simulate_typing(activity["content"])
        elif activity["type"] == "mouse":
            self.simulate_mouse_movement(activity.get("movements", 5))
        
        # Occasionally switch windows (20% chance)
        if random.random() < 0.2:
            self.simulate_window_switch()
        
        # Update activity file for basic tracking
        with open('/tmp/ai_screensaver_activity', 'w') as f:
            f.write(f"Activity: {activity['type']} at {timestamp}\n")
    
    def run(self, duration_minutes=0):
        """Main execution loop"""
        print(f"🤖 AI Screensaver Started")
        print(f"📝 Topic: {self.title()}")
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
                # Perform AI-generated activity
                self.perform_activity()
                
                # Calculate next interval (unpredictable)
                next_interval = random.randint(*self.interval_range)
                
                # Show status
                elapsed = int(time.time() - start_time)
                remaining = int(end_time - time.time()) if duration_minutes > 0 else 0
                
                if duration_minutes > 0:
                    print(f"✅ Activity complete. Next in {next_interval}s | Elapsed: {elapsed//60}:{elapsed%60:02d} | Remaining: {remaining//60}:{remaining%60:02d}")
                else:
                    print(f"✅ Activity complete. Next in {next_interval}s | Elapsed: {elapsed//60}:{elapsed%60:02d}")
                
                # Wait for next activity
                time.sleep(next_interval)
                
        except KeyboardInterrupt:
            print("\n🛑 AI Screensaver stopped by user.")
        except Exception as e:
            print(f"❌ Error occurred: {e}")
            sys.exit(1)
        
        print("🏁 AI Screensaver Ended")
        print(f"📊 Total activities performed: {len(self.activity_log)}")
    
    def title(self):
        """Title case the topic"""
        return ' '.join(word.capitalize() for word in self.topic.split())

def main():
    parser = argparse.ArgumentParser(description='AI-powered intelligent screensaver')
    parser.add_argument('-t', '--topic', type=str, default='software development',
                       help='Work topic for contextual activity (software development, writing, research, design, data analysis, general)')
    parser.add_argument('-i', '--interval', type=int, nargs=2, default=[20, 60],
                       help='Interval range in seconds (min max, default: 20 60)')
    parser.add_argument('-d', '--duration', type=int, default=0,
                       help='Duration in minutes (0 = forever, default: 0)')
    
    args = parser.parse_args()
    
    # Validate topic
    valid_topics = ['software development', 'writing', 'research', 'design', 'data analysis', 'general']
    if args.topic not in valid_topics:
        print(f"⚠️  Unknown topic '{args.topic}'. Using 'general' instead.")
        args.topic = 'general'
    
    # Create and run AI screensaver
    ai_screensaver = AIScreensaver(
        topic=args.topic,
        interval_range=tuple(args.interval)
    )
    
    ai_screensaver.run(duration_minutes=args.duration)

if __name__ == "__main__":
    main()