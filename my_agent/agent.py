from google.adk.agents.llm_agent import Agent

def get_weather(city: str):
    """Fetches real-time weather for a city."""
    return f"The weather in {city} is sunny, 25°C."

def get_time(city: str):
    """Fetches the current local time for a city."""
    return f"The current time in {city} is 2:00 PM."

root_agent = Agent(
    model='gemini-flash-latest',
    name='root_agent',
    instruction="""
    Help users get city information. 
    If a user asks for multiple pieces of information (e.g., weather AND time), 
    always call tools in parallel.
    """,
    tools=[get_weather, get_time]
)