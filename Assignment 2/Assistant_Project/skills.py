import requests
import os
import subprocess
import webbrowser
import psutil   # pip install psutil

def get_weather(city):
    return f"Fetching weather for {city}... (API Key required for real-time data)"

def launch_app(query):
    if "notepad" in query:
        subprocess.Popen(["notepad.exe"])
        return "Opening Notepad."
    elif "chrome" in query:
        os.startfile("chrome.exe") 
        return "Launching Chrome."
    return "Application not recognized."

def web_search(query):
    topic = query.replace("search", "").replace("play", "").strip()
    webbrowser.open(f"https://www.google.com/search?q={topic}")
    return f"Searching for {topic}."

def system_stats():
    cpu = psutil.cpu_percent()
    battery = psutil.sensors_battery().percent
    return f"CPU is at {cpu}% and battery is at {battery}%."