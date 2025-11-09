#!/bin/bash
# Enhanced launcher with AI-powered screensaver option

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🤖 Intelligent Screensaver Launcher"
echo "=================================="
echo "1) Basic Screensaver (15 minutes)"
echo "2) Basic Screensaver (30 minutes)" 
echo "3) Basic Screensaver (1 hour)"
echo "4) Basic Screensaver (forever)"
echo "5) 🤖 AI Screensaver - Software Development"
echo "6) 🤖 AI Screensaver - Writing/Content"
echo "7) 🤖 AI Screensaver - Research"
echo "8) 🤖 AI Screensaver - Design"
echo "9) 🤖 AI Screensaver - Data Analysis"
echo "10) 🤖 AI Screensaver - General Office Work"
echo "11) Custom duration"
echo "12) Exit"
echo ""

read -p "Choose an option (1-12): " choice

case $choice in
    1)
        "$SCRIPT_DIR/screensaver.py" -d 15 -i 30
        ;;
    2)
        "$SCRIPT_DIR/screensaver.py" -d 30 -i 30
        ;;
    3)
        "$SCRIPT_DIR/screensaver.py" -d 60 -i 30
        ;;
    4)
        "$SCRIPT_DIR/screensaver.py" -i 30
        ;;
    5)
        "$SCRIPT_DIR/ai-screensaver.py" -t "software development" -d 30 -i 20 60
        ;;
    6)
        "$SCRIPT_DIR/ai-screensaver.py" -t "writing" -d 30 -i 20 60
        ;;
    7)
        "$SCRIPT_DIR/ai-screensaver.py" -t "research" -d 30 -i 20 60
        ;;
    8)
        "$SCRIPT_DIR/ai-screensaver.py" -t "design" -d 30 -i 20 60
        ;;
    9)
        "$SCRIPT_DIR/ai-screensaver.py" -t "data analysis" -d 30 -i 20 60
        ;;
    10)
        "$SCRIPT_DIR/ai-screensaver.py" -t "general" -d 30 -i 20 60
        ;;
    11)
        read -p "Enter duration in minutes: " duration
        "$SCRIPT_DIR/screensaver.py" -d $duration -i 30
        ;;
    12)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid option"
        exit 1
        ;;
esac