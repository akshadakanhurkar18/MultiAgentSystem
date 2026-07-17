from google.adk.agents import Agent

from .prompt import PLANNER_PROMPT

planner_agent = Agent(
    name="PlannerAgent",
    model="groq/llama-3.3-70b-versatile",
    description="Creates an action plan",
    instruction=PLANNER_PROMPT,
)