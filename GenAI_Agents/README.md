

# GenAI Agents: Comprehensive Repository for Development and Implementation 🚀

This repository serves as a comprehensive resource for learning, building, and sharing GenAI agents, ranging from simple conversational bots to complex, multi-agent systems.

## Introduction

Generative AI agents are at the forefront of artificial intelligence, revolutionizing the way we interact with and leverage AI technologies. This repository is designed to guide you through the development journey, from basic agent implementations to advanced, cutting-edge systems.

## GenAI Agent Implementations

Explore list of GenAI agent implementations, sorted by categories:

1. **Conversational Agent**

   - **[LangChain](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/simple_conversational_agent.ipynb)**
   
   
    #### Overview 🔎
    A context-aware conversational AI maintains information across interactions, enabling more natural dialogues.

    #### Implementation 🛠️
    Integrates a language model, prompt template, and history manager to generate contextual responses and track conversation sessions.

2. **Data Analysis Agent**

   - **[LangChain](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/simple_data_analysis_agent_notebook.ipynb)**
   
   #### Overview 🔎
   An AI-powered data analysis agent interprets and answers questions about datasets using natural language, combining language models with data manipulation tools for intuitive data exploration.
   #### Implementation 🛠️
   Integrates a language model, data manipulation framework, and agent framework to process natural language queries and perform data analysis on a synthetic dataset, enabling accessible insights for non-technical users.

### 🔧 Framework Tutorial: LangGraph

3. **[Introduction to LangGraph: Building Modular AI Workflows](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/langgraph-tutorial.ipynb)**
   
   #### Overview 🔎
   This tutorial introduces LangGraph, a powerful framework for creating modular, graph-based AI workflows. Learn how to leverage LangGraph to build more complex and flexible AI agents that can handle multi-step processes efficiently.

   #### Implementation 🛠️
   Step-by-step guide on using LangGraph to create a StateGraph workflow. The tutorial covers key concepts such as state management, node creation, and graph compilation. It demonstrates these principles by constructing a simple text analysis pipeline, serving as a foundation for more advanced agent architectures.

4. **[Scientific Paper Agent - Literature Review](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/scientific_paper_agent_langgraph.ipynb)**
   
   #### Overview 🔎
   An intelligent research assistant that helps users navigate, understand, and analyze scientific literature through an orchestrated workflow. The system combines academic APIs with sophisticated paper processing techniques to automate literature review tasks, enabling researchers to efficiently extract insights from academic papers while maintaining research rigor and quality control.

   #### Implementation 🛠️
   Leverages LangGraph to create a five-node workflow system including decision making, planning, tool execution, and quality validation nodes. The system integrates the CORE API for paper access, PDFplumber for document processing, and advanced language models for analysis. Key features include a retry mechanism for robust paper downloads, structured data handling through Pydantic models, and quality-focused improvement cycles with human-in-the-loop validation options.

    #### Additional Resources 📚
    - **[YouTube Explanation](https://youtu.be/Bc4YtpHY6Ws)** 
    - **[Blog Post](https://open.substack.com/pub/diamantai/p/nexus-ai-the-revolutionary-research?r=336pe4&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false)**

5. **[Customer Support Agent (LangGraph)](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/customer_support_agent_langgraph.ipynb)**
   
    #### Overview 🔎
    An intelligent customer support agent using LangGraph categorizes queries, analyzes sentiment, and provides appropriate responses or escalates issues.

    #### Implementation 🛠️
    Utilizes LangGraph to create a workflow combining state management, query categorization, sentiment analysis, and response generation.

6. **[Essay Grading Agent (LangGraph)](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/essay_grading_system_langgraph.ipynb)**
   
    #### Overview 🔎
    An automated essay grading system using LangGraph and an LLM model evaluates essays based on relevance, grammar, structure, and depth of analysis.

    #### Implementation 🛠️
    Utilizes a state graph to define the grading workflow, incorporating separate grading functions for each criterion.

7. **[Travel Planning Agent (LangGraph)](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/simple_travel_planner_langgraph.ipynb)**
    
    #### Overview 🔎
    A Travel Planner using LangGraph demonstrates how to build a stateful, multi-step conversational AI application that collects user input and generates personalized travel itineraries.

    #### Implementation 🛠️
    Utilizes StateGraph to define the application flow, incorporates custom PlannerState for process management.

8. **[GenAI Career Assistant Agent](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/agent_hackathon_genAI_career_assistant.ipynb)**

    #### Overview 🔎
    The GenAI Career Assistant demonstrates how to create a multi-agent system that provides personalized guidance for careers in Generative AI. Using LangGraph and Gemini LLM, the system delivers customized learning paths, resume assistance, interview preparation, and job search support.

    #### Implementation 🛠️
    Leverages a multi-agent architecture using LangGraph to coordinate specialized agents (Learning, Resume, Interview, Job Search) through TypedDict-based state management. The system employs sophisticated query categorization and routing while integrating with external tools like DuckDuckGo for job searches and dynamic content generation.

    #### Additional Resources 📚
    - **[YouTube Explanation](https://www.youtube.com/watch?v=IcKh0ltXO_8)** 
    
9. **[Project Manager Assistant Agent](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/project_manager_assistant_agent.ipynb)**

    #### Overview 🔎
    An AI agent designed to assist in project management tasks by automating the process of creating actionable tasks from project descriptions, identifying dependencies, scheduling work, and assigning tasks to team members based on expertise. The system includes risk assessment and self-reflection capabilities to optimize project plans through multiple iterations, aiming to minimize overall project risk.

    #### Implementation 🛠️
    Leverages LangGraph to orchestrate a workflow of specialized nodes including task generation, dependency mapping, scheduling, allocation, and risk assessment. Each node uses GPT-4o-mini for structured outputs following Pydantic models. The system implements a feedback loop for self-improvement, where risk scores trigger reflection cycles that generate insights to optimize the project plan. Visualization tools display Gantt charts of the generated schedules across iterations.

    #### Additional Resources 📚
    - **[YouTube Explanation](https://www.youtube.com/watch?v=R7YWjzg3LpI)** 

10. **[Content Intelligence: Multi-Platform Content Generation Agent](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/ContentIntelligence.ipynb)**

    #### Overview 🔎
    Content Intelligence demonstrates how to build an advanced content generation system that transforms input text into platform-optimized content across multiple social media channels. The system employs LangGraph for workflow orchestration to analyze content, conduct research, and generate tailored content while maintaining brand consistency across different platforms.

    #### Implementation 🛠️
    Implements a sophisticated workflow using LangGraph to coordinate multiple specialized nodes (Summary, Research, Platform-Specific) through the content generation process. The system features TypedDict and Pydantic models for state management, integration with Tavily Search for research enhancement, and platform-specific content generation using GPT-4. The implementation includes parallel processing for multiple platforms and customizable content templates.

    #### Additional Resources 📚
    - **[YouTube Explanation](https://www.youtube.com/watch?v=DPMtPbKmWnU)** 

11. **[Memory-Enhanced Conversational Agent](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/memory_enhanced_conversational_agent.ipynb)**
   
    #### Overview 🔎
    A memory-enhanced conversational AI agent incorporates short-term and long-term memory systems to maintain context within conversations and across multiple sessions, improving interaction quality and personalization.

    #### Implementation 🛠️
    Integrates a language model with separate short-term and long-term memory stores, utilizes a prompt template incorporating both memory types, and employs a memory manager for storage and retrieval. The system includes an interaction loop that updates and utilizes memories for each response.

12. **[Multi-Agent Collaboration System](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/multi_agent_collaboration_system.ipynb)**
    
    #### Overview 🔎
    A multi-agent collaboration system combining historical research with data analysis, leveraging large language models to simulate specialized agents working together to answer complex historical questions.

    #### Implementation 🛠️
    Utilizes a base Agent class to create specialized HistoryResearchAgent and DataAnalysisAgent, orchestrated by a HistoryDataCollaborationSystem. The system follows a five-step process: historical context provision, data needs identification, historical data provision, data analysis, and final synthesis.

13. **[Self-Improving Agent](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/self_improving_agent.ipynb)**
    
    #### Overview 🔎
    A Self-Improving Agent using LangChain engages in conversations, learns from interactions, and continuously improves its performance over time through reflection and adaptation.

    #### Implementation 🛠️
    Integrates a language model with chat history management, response generation, and a reflection mechanism. The system employs a learning system that incorporates insights from reflection to enhance future performance, creating a continuous improvement loop.

14. **[Internet Search and Summarize Agent](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/search_the_internet_and_summarize.ipynb)**
    
    #### Overview 🔎
    An intelligent web research assistant that combines web search capabilities with AI-powered summarization, automating the process of gathering information from the internet and distilling it into concise, relevant summaries.

    #### Implementation 🛠️
    Integrates a web search module using DuckDuckGo's API, a result parser, and a text summarization engine leveraging OpenAI's language models. The system performs site-specific or general searches, extracts relevant content, generates concise summaries, and compiles attributed results for efficient information retrieval and synthesis.

15. **[Multi agent research team - Autogen](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/research_team_autogen.ipynb)**

    #### Overview 🔎
    This technique explores a multi-agent system for collaborative research using the AutoGen library. It employs agents to solve tasks collaboratively, focusing on efficient execution and quality assurance. The system enhances research by distributing tasks among specialized agents.

    #### Implementation 🛠️
    Agents are configured with specific roles using the GPT-4 model, including admin, developer, planner, executor, and quality assurance. Interaction management ensures orderly communication with defined transitions. Task execution involves collaborative planning, coding, execution, and quality checking, demonstrating a scalable framework for various domains.

    #### Additional Resources 📚
    - **[comprehensive solution with UI](https://github.com/yanivvak/dream-team)** 
    - **[Blogpost](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/build-your-dream-team-with-autogen/ba-p/4157961)**


16. **[Self-Healing Codebase System](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/self_healing_code.ipynb)**

    #### Overview 🔎
    An intelligent system that automatically detects, diagnoses, and fixes runtime code errors using LangGraph workflow orchestration and ChromaDB vector storage. The system maintains a memory of encountered bugs and their fixes through vector embeddings, enabling pattern recognition for similar errors across the codebase.

    #### Implementation 🛠️
    Utilizes a state-based graph workflow that processes function definitions and runtime arguments through specialized nodes for error detection, code analysis, and fix generation. Incorporates ChromaDB for vector-based storage of bug patterns and fixes, with automated search and retrieval capabilities for similar error patterns, while maintaining code execution safety through structured validation steps.

    #### Additional Resources 📚
    - **[YouTube Explanation](https://www.youtube.com/watch?v=ga7ShvIXOvE)**

17. **[DataScribe: AI-Powered Schema Explorer](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/database_discovery_fleet.ipynb)**
    
    #### Overview 🔎
    An intelligent agent system that enables intuitive exploration and querying of relational databases through natural language interactions. The system utilizes a fleet of specialized agents, coordinated by a stateful Supervisor, to handle schema discovery, query planning, and data analysis tasks while maintaining contextual understanding through vector-based relationship graphs.
    
    #### Implementation 🛠️
    Leverages LangGraph for orchestrating a multi-agent workflow including discovery, inference, and planning agents, with NetworkX for relationship graph visualization and management. The system incorporates dynamic state management through TypedDict classes, maintains database context between sessions using a db_graph attribute, and includes safety measures to prevent unauthorized database modifications.

18. **[AInsight: AI/ML Weekly News Reporter](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/ainsight_langgraph.ipynb)**

    #### Overview 🔎
    AInsight demonstrates how to build an intelligent news aggregation and summarization system using a multi-agent architecture. The system employs three specialized agents (NewsSearcher, Summarizer, Publisher) to automatically collect, process and summarize AI/ML news for general audiences through LangGraph-based workflow orchestration.

    #### Implementation 🛠️
    Implements a state-managed multi-agent system using LangGraph to coordinate the news collection (Tavily API), technical content summarization (GPT-4), and report generation processes. The system features modular architecture with TypedDict-based state management, external API integration, and markdown report generation with customizable templates.

    #### Additional Resources 📚
    - **[YouTube Explanation](https://www.youtube.com/watch?v=kH5S1is2D_0)**

19. **[Blog Writer (Open AI Swarm)](https://github.com/subodh556/Gen_AI/blob/main/GenAI_Agents/all_agents_tutorials/blog_writer_swarm.ipynb)**

    #### Overview 🔎
    A multi-agent system for collaborative blog post creation using OpenAI's Swarm package. It leverages specialized agents to perform research, planning, writing, and editing tasks efficiently.

    #### Implementation 🛠️
    Utilizes OpenAI's Swarm Package to manage agent interactions. Includes an admin, researcher, planner, writer, and editor, each with specific roles. The system follows a structured workflow: topic setting, outlining, research, drafting, and editing. This approach enhances content creation through task distribution, specialization, and collaborative problem-solving.

    #### Additional Resources 📚
    - **[Swarm Repo](https://github.com/openai/swarm)**

20. **[Sophisticated Controllable Agent for Complex RAG Tasks 🤖](https://github.com/NirDiamant/Controllable-RAG-Agent)**

    #### Overview 🔎
    An advanced RAG solution designed to tackle complex questions that simple semantic similarity-based retrieval cannot solve. This approach uses a sophisticated deterministic graph as the "brain" 🧠 of a highly controllable autonomous agent, capable of answering non-trivial questions from your own data.

    #### Implementation 🛠️
    • Implement a multi-step process involving question anonymization, high-level planning, task breakdown, adaptive information retrieval and question answering, continuous re-planning, and rigorous answer verification to ensure grounded and accurate responses.
