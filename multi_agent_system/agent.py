from google.adk.agents import SequentialAgent

from .research_agent import research_agent
from .summarizer_agent import summarizer_agent
from .planner_agent import planner_agent

root_agent = SequentialAgent(
    name="Coordinator",
    sub_agents=[
        research_agent,
        summarizer_agent,
        planner_agent,
    ],
)