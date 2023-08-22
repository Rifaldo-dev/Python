import time

def running_text(text, delay):
    while True:
        for i in range(len(text)):
            print(text[i:], end="\r")
            time.sleep(delay)
            print(" " * len(text), end="\r")

text = "Ini adalah contoh running text!"
delay = 0.3  # ini adalah waktu delay text  ny>

running_text(text, delay)
