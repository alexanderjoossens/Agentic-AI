import sys
from blog_post.crew import BlogWritingCrew

from crewai import LLM


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI Agents'
    }
    BlogWritingCrew().crew().kickoff(inputs=inputs)