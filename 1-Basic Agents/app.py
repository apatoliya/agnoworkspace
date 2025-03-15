from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools

import os
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')


agent=Agent(
    model=OpenAIChat(id='gpt-4o'),
    description='You are an assistant',
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

agent.print_response('Tell me the recent news related to stock market',stream=True )