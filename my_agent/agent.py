from google.adk.agents import LlmAgent
from google.adk.agents import ParallelAgent

# Agent specialized in fetching flight data
flight_agent = LlmAgent(
    name="FlightSearchAgent",
    instruction="You are an expert at finding and booking flights.",
    description="Use this agent for all flight-related inquiries."
)

# Agent specialized in hotel bookings
hotel_agent = LlmAgent(
    name="HotelBookingAgent",
    instruction="You are an expert at finding the best hotels within budget.",
    description="Use this agent for hotel or accommodation queries."
)

# This manager will call both specialists at the same time
trip_manager = ParallelAgent(
    name="TravelCoordinator",
    sub_agents=[flight_agent, hotel_agent]
)

# ADK requires a root_agent to be exposed at module level
root_agent = trip_manager