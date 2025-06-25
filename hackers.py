import os
import time
import random
import sys
from datetime import datetime

# Set of characters for Matrix-style effect
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Time prefix to simulate log timestamps
def timestamp():
    return f"[{datetime.now().strftime('%H:%M:%S')}]"

# Manual typing simulation
def type_line(text, delay_range=(0.01, 0.03)):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(*delay_range))
    print()

# Generate fake command lines
def hacker_command():
    commands = [
        "nmap -sS 203.115.{}.{}",
        "ssh root@203.115.{}.{}",
        "scp -r /data/files root@203.115.{}.{}:/root/",
        "ping -c 4 203.115.{}.{}",
        "curl -X POST http://203.115.{}.{}:8080/inject",
        "python3 exploit.py --target 203.115.{}.{}",
        "cat /var/log/auth.log",
        "./ddos_attack.sh --ip 203.115.{}.{}",
    ]
    cmd = random.choice(commands)
    return cmd.format(random.randint(0, 255), random.randint(0, 255))

# Matrix scroll effect
def matrix_scroll(duration=5):
    start = time.time()
    while time.time() - start < duration:
        line = "".join(random.choices(chars, k=random.randint(50, 70)))
        print(f"{timestamp()} {line}")
        time.sleep(0.02)

# Countdown then reveal prank
def countdown_then_reveal(seconds=10):
    print("\n\033[1;31m")  # Red text
    type_line("[!] CRITICAL ERROR: SYSTEM BREACH DETECTED")
    type_line("[!] INITIATING SELF-DESTRUCT PROTOCOL")
    print()
    for i in range(seconds, 0, -1):
        print(f"   💥 SYSTEM WIPE IN: {i} seconds...", end='\r', flush=True)
        time.sleep(1)
    print("\n")
    time.sleep(0.5)
    type_line("⚠️  RELAX. THIS IS JUST A PRANK! 😆", delay_range=(0.03, 0.05))
    time.sleep(2)
    print("\033[0m")  # Reset text color
    clear()
    print("✅ System restored. No hack occurred. All safe.")
    time.sleep(2)

def hacker_screen():
    clear()
    print("\033[1;32m")  # Green hacker terminal
    print("╔════════════════════════════════════════════════════════════╗")
    print("║      CONNECTING TO REMOTE NODE: BACOOR, CAVITE (PH)        ║")
    print("╚════════════════════════════════════════════════════════════╝\n")
    time.sleep(1)

    fake_intro = [
        "Establishing secure shell...",
        "Handshake accepted.",
        "Logged in as: root@target",
        "Locating GPS coordinates...",
        "Coordinates: 14.4594° N, 120.9326° E",
        "Injecting payload into device...",
        "Payload injected successfully.",
        "Downloading logs: camera_feed.mp4, banking_info.db",
        "Bypassing firewall...",
        "Access level: ROOT ✅"
    ]

    for line in fake_intro:
        type_line(f"{timestamp()} {line}")
        time.sleep(0.2)

    print(f"\n{timestamp()} Running terminal commands...\n")
    time.sleep(1)

    # Simulate typing hacker commands
    for _ in range(10):
        cmd = hacker_command()
        type_line(f"$ {cmd}")
        time.sleep(0.3)

    print(f"\n{timestamp()} 🔍 Scanning live data stream...\n")
    matrix_scroll(duration=5)

    countdown_then_reveal(10)

if __name__ == "__main__":
    hacker_screen()