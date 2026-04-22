import google.generativeai as genai # pip install -q -U google-generativeai # python -m pip install -U google-generativeai
import skills  # Import your skills file

genai.configure(api_key="YOUR_API_KEY_HERE")    # I have forgotten my Gemini API key

def call_llm(query):
    """Phase 2: LLM Fallback for general questions."""
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return "Nexus is having trouble reaching the cloud brain right now."

def process_command(query, memory):
    """Router: Directs query to Automation, Memory, or LLM."""
    query = query.lower()
    
    if "remember" in query:
        fact = query.replace("remember", "").strip()
        
        if "preferences" not in memory or not isinstance(memory["preferences"], list):
            memory["preferences"] = []
            
        memory["preferences"].append(fact)
        return f"I've noted that down for you: {fact}"

    if "open" in query:
        return skills.launch_app(query)
        
    elif "search" in query or "play" in query:
        return skills.web_search(query)
        
    elif "battery" in query or "system" in query:
        return skills.system_stats()
        
    elif "weather" in query:
        return skills.get_weather("local")
    
    else:
        return call_llm(query)