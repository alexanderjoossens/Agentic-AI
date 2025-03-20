# BlogPost Crew

Welcome to the BlogPost Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Pre-requisites

At first, you'll need to configure your watsonX project. 
You need an IBM Cloud account to create a watsonx.ai project.

### Creating WatsonX project, associating WML instance and retrieving API key

- Log in to your [IBM Cloud account](https://cloud.ibm.com).

- To create an API key, navigate to Manage > Access (IAM) > API Keys. Generate a new API key and save it. This will be your WATSONX_API_KEY.

- Go to [watsonx.ai](https://dataplatform.cloud.ibm.com/wx/home?context=wx) and log in with your IBM Cloud account.

- Create a watsonx.ai project by going to Projects > New Project and fill in the requested information.

- To retrieve your project ID, open your watsonx.ai project. Navigate to the Manage tab. Then, under General Option, copy the Project ID. This will be your WATSONX_PROJECT_ID.

- Associate a WML instance to the project. Select Manage tab > Services & integrations > Associate Service > watsonMachineLearning


## Using Ollama

Go to the Ollama [website](https://ollama.com/) and download and install ollama. After installation and starting it will run in the background. You can find the models that you can download and how to download them on the models list of [website](https://ollama.com/search)

You won't be able to use each model on your laptop as some are still very big.

# Working with CrewAI

Create a virtual environment


## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

```bash
python3.10 -m venv .venv 
source .venv/bin/activate
```

### Install CrewAI

```bash
pip install crewai
```
### install uv:

```bash
pip install uv
```
Next, navigate to your project directory and install the dependencies:

Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your Watsonx project information and api key into the `.env` file**

# Exercise: Multi-Agent Blog Writing Workflow

Overview
In this exercise, you will build and implement a multi-agent workflow using CrewAI to automate the process of researching, writing, optimizing, and publishing a blog post. Your agents will collaborate to generate a well-researched and SEO-optimized article on a given topic.

By the end of this exercise, you will have a fully functional AI-driven blog writing system, where different agents perform specialized tasks and pass information to the next stage in the pipeline.

## Objective
Your goal is to create a multi-step system where each agent plays a specific role:

Research trending topics and gather relevant information.
Generate a blog post based on the research findings.
Optimize the content for SEO to increase visibility.
Proofread and refine the article to improve readability.
Simulate publishing the finalized blog post.


Some agent exemples might be:

🕵️ Researcher → Finds key insights about the given topic.\
✍️ Content Writer → Creates a well-structured blog post.\
🔍 SEO Specialist → Optimizes the post for better search rankings.\
📝 Proofreader → Ensures grammar, clarity, and professionalism.


...

## Your Task

- Set up CrewAI and define five agents, each responsible for a distinct task.
- Implement the workflow, ensuring smooth data passing between agents.
- Run the system with a sample topic and observe how agents collaborate.
- Refine the process, optimizing content at each stage.

**Modify `src/blog_post/config/agents.yaml` to define your agents**\
**Modify `src/blog_post/config/tasks.yaml` to define your tasks**\
**Modify `src/blog_post/crew.py` to add your own logic, tools and specific args**
**Modify `src/blog_post/main.py` to add custom inputs for your agents and tasks**

# Success Criteria

- A blog post is successfully generated and refined
- Each agent functions autonomously, performing its role effectively.
- The workflow is seamless, with information flowing logically between agents.
- The final article is engaging, accurate, and SEO-friendly.

Bonus Challenge

Enhance the workflow by:
✅ Adding a fact-checking agent to verify sources.
✅ Integrating social media distribution to share the post automatically.
✅ ...


## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the blog-post Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The blog-post Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.
