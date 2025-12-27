Project Overview

Mission Pizza AI is a multi-agent system designed to make traditional pizza APIs accessible to AI agents using the Model Context Protocol (MCP).

The system automatically converts an OpenAPI specification into an MCP server and allows AI agents to:

Take pizza orders using natural language

Place orders via MCP tools

Track orders using an order ID

Coordinate delivery scheduling via agent-to-agent (A2A) communication


Detailed project explained video:

https://drive.google.com/file/d/1E2_ToSHn-ytA-9UIBOjYmUt3__EQXp7-/view?usp=drive_link

OpenAPI Specification

The project uses an OpenAPI 3.0 specification located at:

openapi/pizza_openapi.json

Exposed Endpoints

Defines:

	/menu – list pizzas

	/order – place order

	/order/{id} – track order

This OpenAPI file is automatically converted into an MCP server using the MCP generator.

Overall Architecture

The system follows a modular, agent-based architecture:

User
  ↓
Ordering Agent
  ↓
MCP Server (generated from OpenAPI)
  ↓
Mock Backend
  ↑
Scheduling Agent (A2A)


How It Works

1.OpenAPI → MCP

mcp_generator.py reads pizza_openapi.json

Automatically creates MCP tools for menu, order, and tracking

2.Ordering Agent

Accepts user input in natural language

Uses MCP tools to place and track orders

Stores order state and order ID

3.Scheduling Agent (A2A)

Receives order details from ordering agent

Schedules delivery (simulated)

Sends confirmation back to the user

Setup Instructions

1. Create virtual environment

	python -m venv .venv

2. Activate environment

	.venv\Scripts\activate

3. Install dependencies	

	pip install -r requirements.txt

4. Run the application

	python main.py
	
	Always run main.py to start the chatbot
	

Conclusion

This project demonstrates how a traditional pizza API can be transformed into an AI-ready system using MCP and cooperating AI agents, fulfilling all phases of the assignment.

