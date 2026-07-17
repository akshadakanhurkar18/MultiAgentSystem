from google.adk.agents import Agent

from .prompt import RESEARCH_PROMPT

research_agent = Agent(
    name="ResearchAgent",
    model="groq/llama-3.3-70b-versatile",
    description="Researches user questions",
    instruction=RESEARCH_PROMPT,
)