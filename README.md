# 📘 README --- Tools in LLM & LangChain

## 📌 What are Tools?

A **tool** is simply a **Python function or an API** packaged in a way
that an **LLM can understand and call when needed**.

Tools extend LLM capabilities so they can **interact with the real
world** instead of only generating text.

------------------------------------------------------------------------

## 🤖 What LLMs are good at

-   🧠 Reasoning --- analyzing and thinking through problems
-   ✍️ Language generation --- writing text, summaries, code
-   🎯 Decision making --- choosing next steps based on context

------------------------------------------------------------------------

## 🚫 What LLMs cannot do alone

Without tools, LLMs cannot reliably:

-   Access live data (weather, news, stock prices)
-   Perform precise math
-   Call APIs
-   Run code
-   Interact with databases
-   Perform real-world actions (like booking tickets)

Example: If you ask an LLM to book a train ticket on IRCTC, it can only
do that through tools.

------------------------------------------------------------------------

# 🧩 Tools in LangChain

## 1️⃣ Built-in Tools

Prebuilt and production-ready tools for common tasks.

Examples: - DuckDuckGoSearchRun → Web search
- WikipediaQueryRun → Wikipedia lookup
- PythonREPLTool → Run Python code
- ShellTool → Execute shell commands
- RequestsGetTool → Call APIs
- GmailSendMessageTool → Send emails
- SQLDatabaseQueryTool → Query databases

Use when you need standard functionality quickly.

------------------------------------------------------------------------

## 2️⃣ Custom Tools

User-defined functions or APIs for your specific business logic.

Examples: - Booking tickets - Creating support tickets - Querying
internal data

------------------------------------------------------------------------

# 🧠 How Tools Fit into the Agent Ecosystem

An AI agent is an LLM-powered system that can:

1.  Think
2.  Decide
3.  Take actions

We don't send tool code to the LLM --- only the schema (name, inputs,
description).

------------------------------------------------------------------------

# 🛠️ Ways to Create Tools in LangChain

## 1️⃣ Using @tool Decorator

Easy description: **Quickest way to turn a function into a tool.**

Advantages: - Simple and fast - Minimal boilerplate - Great for
prototypes - Auto schema generation

When to use: - Small utilities - Quick experiments

------------------------------------------------------------------------

## 2️⃣ Structured Tool + Pydantic

Easy description: **Best for tools that need validation and clear input
structure.**

Advantages: - Strong validation - Reliable inputs - Handles complex
parameters

When to use: - Production apps - Business workflows

------------------------------------------------------------------------

## 3️⃣ BaseTool

Easy description: **Full control --- build tools from scratch.**

BaseTool is the abstract base class for all tools.

Advantages: -Async and await, Maximum flexibility - Custom execution logic - Advanced
control

When to use: - Complex tools - Custom agent frameworks

------------------------------------------------------------------------

# 🧮 Quick Comparison

  Approach                Ease     Validation   Flexibility   Best For
  ----------------------- -------- ------------ ------------- --------------------
  @tool                   High     Low          Medium        Quick utilities
  Structured + Pydantic   Medium   High         High          Production tools
  BaseTool                Low      High         Very High     Advanced use cases

------------------------------------------------------------------------
# 🧰 What is a Toolkit?

A **toolkit** is a **collection or bundle of related tools** that serve
a common purpose.
It helps organize tools and makes them reusable.

👉 Easy way to remember:
**Toolkit = Folder of related tools**

------------------------------------------------------------------------

## 📦 Example: Google Drive Toolkit

In LangChain, a toolkit might be **GoogleDriveToolkit**.

It can contain multiple tools such as:

-   **GoogleDriveCreateFileTool** → Upload a file
-   **GoogleDriveSearchTool** → Search files by name or content
-   **GoogleDriveReadFileTool** → Read file content

Using a toolkit makes it easy to plug multiple related capabilities into
an agent at once.

# 🧠 Key Takeaway

LLM = Brain
Tools = Hands
Agent = Brain + Hands working together

With tools, LLMs can act and solve real-world problems.
