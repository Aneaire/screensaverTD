#!/bin/bash
# Script to switch between normal and test hypridle configurations

CONFIG_DIR="/home/aneaire/.local/share/omarchy/config/hypr"
NORMAL_CONFIG="$CONFIG_DIR/hypridle.conf"
TEST_CONFIG="$CONFIG_DIR/hypridle-test.conf"

echo "Hypridle Configuration Switcher"
echo "================================"

if [ "$1" = "test" ]; then
    echo "Switching to TEST configuration (1-minute timeout)..."
    cp "$TEST_CONFIG" "$NORMAL_CONFIG"
    echo "Restarting hypridle..."
    pkill hypridle
    sleep 2
    hypridle &
    echo "✓ Test configuration active!"
    echo "  - Screensaver starts after 1 minute"
    echo "  - Lock after 1.5 minutes"
    echo "  - Screen off after 2 minutes"
    echo ""
    echo "Now test your screensaver script:"
    echo "  ./screensaver.py -d 3 -i 10"
    echo ""
    echo "If working, screen should NOT lock after 1 minute"

elif [ "$1" = "normal" ]; then
    echo "Switching back to NORMAL configuration..."
    # Restore original (we need to recreate it)
    cat > "$NORMAL_CONFIG" << 'EOF'
general {
    lock_cmd = omarchy-lock-screen                         # lock screen and 1password
    before_sleep_cmd = loginctl lock-session               # lock before suspend.
    after_sleep_cmd = hyprctl dispatch dpms on             # to avoid having to press a key twice to turn on the display.
    inhibit_sleep = 3                                      # wait until screen is locked
}

listener {
    timeout = 150                                             # 2.5min
    on-timeout = pidof hyprlock || omarchy-launch-screensaver # start screensaver (if we haven't locked already)
}

listener {
    timeout = 300                      # 5min
    on-timeout = loginctl lock-session # lock screen when timeout has passed
}

listener {
    timeout = 330                                            # 5.5min
    on-timeout = hyprctl dispatch dpms off                   # screen off when timeout has passed
    on-resume = hyprctl dispatch dpms on && brightnessctl -r # screen on when activity is detected
}
EOF
    echo "Restarting hypridle..."
    pkill hypridle
    sleep 2
    hypridle &
    echo "✓ Normal configuration restored!"

else
    echo "Usage:"
    echo "  $0 test    - Switch to 1-minute test configuration"
    echo "  $0 normal  - Restore normal 2.5/5 minute configuration"
    echo ""
    echo "Current status:"
    if grep -q "timeout = 60" "$NORMAL_CONFIG"; then
        echo "  ✓ Test configuration is active"
    else
        echo "  ✓ Normal configuration is active"
    fi
fi