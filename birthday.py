import webbrowser
import os
import time

html_file = os.path.abspath("birthday.html")

print("🎂 Starting Birthday Surprise...")

time.sleep(1)

webbrowser.open("file://" + html_file)

print("💖 Birthday surprise opened!")