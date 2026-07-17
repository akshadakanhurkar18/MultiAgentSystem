from google.adk.agents import Agent

from .prompt import SUMMARY_PROMPT

summarizer_agent = Agent(
    name="SummarizerAgent",
    model="groq/llama-3.3-70b-versatile",
    description="Summarizes information",
    instruction=SUMMARY_PROMPT,
)