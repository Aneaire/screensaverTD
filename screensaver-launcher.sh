#!/bin/bash
# Simple launcher for screensaver script

echo "Screensaver Launcher"
echo "=================="
echo "1) Run for 15 minutes"
echo "2) Run for 30 minutes" 
echo "3) Run for 1 hour"
echo "4) Run forever"
echo "5) Custom duration"
echo "6) Exit"
echo ""

read -p "Choose an option (1-6): " choice

case $choice in
    1)
        /home/aneaire/Work/screensaver/screensaver.py -d 15 -i 30
        ;;
    2)
        /home/aneaire/Work/screensaver/screensaver.py -d 30 -i 30
        ;;
    3)
        /home/aneaire/Work/screensaver/screensaver.py -d 60 -i 30
        ;;
    4)
        /home/aneaire/Work/screensaver/screensaver.py -i 30
        ;;
    5)
        read -p "Enter duration in minutes: " duration
        /home/aneaire/Work/screensaver/screensaver.py -d $duration -i 30
        ;;
    6)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid option"
        exit 1
        ;;
esac