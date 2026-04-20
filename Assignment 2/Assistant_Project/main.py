import engine
import brain
import json
import os

WAKE_WORD = "nexus"
MEMORY_FILE = "memory.json"

def manage_memory(action, data=None):
    """Handles Phase 4: Data Persistence."""
    if action == "save":
        with open(MEMORY_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        return "Memory stored."
    elif action == "load":
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, 'r') as f:
                return json.load(f)
        return {"user_name": "User", "preferences": []} # Default state

def main():
    memory = manage_memory("load")
    
    engine.speak(f"Nexus systems online. Hello {memory.get('user_name')}, I am listening.")

    while True:
        raw_audio = engine.listen()
        
        if WAKE_WORD in raw_audio:
            engine.speak("How can I help?") # Sensory cue
            
            command = engine.listen()
            
            if "goodbye" in command or "sleep" in command:
                engine.speak("Going into standby mode. Goodbye!")
                break
            
            if command == "error_unknown":
                engine.speak("I'm sorry, I didn't quite catch that.")
            elif command == "error_network":
                engine.speak("I'm having trouble connecting to the network.")
            
            else:
                response = brain.process_command(command, memory)
                
                manage_memory("save", memory)
                
                engine.speak(response)

if __name__ == "__main__":
    main()