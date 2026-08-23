
# Day 01 — AI Platform Fundamentals

Date: 2026-08-14

Summary
- Short, structured notes from Day 1 learning about AI platforms, LLMs, agents, tools, and how they fit together in an enterprise.

Key Concepts
- AI Platform: reusable infrastructure for building, deploying, operating, and governing AI applications and agents.
- LLM: a reasoning/generation engine — excellent at language tasks but not a substitute for data access or action execution.
- Tools: connectors and APIs that give the LLM access to systems (databases, Git, Kubernetes, lineage, etc.).
- Agent: orchestrator that decides which tools to call and how to combine results to fulfill a goal.

Why an LLM Alone Is Not Enough
- Limitation #1 — Knowledge: an LLM does not automatically know private organizational data (schemas, source code, deployments).
  - Solution: RAG, knowledge graphs, vector DBs, enterprise data sources.
- Limitation #2 — Actions: an LLM cannot perform operations on external systems by itself.
  - Solution: tool calling (MCP), APIs, and secure action agents.

AI Platform vs ML Engineer (Roles)
- ML Engineer: builds and evaluates models, works on training, serving, pipelines, inference optimization.
- AI Platform Engineer: builds shared infra and services (RAG, memory, orchestration, security, observability, scaling) so developers can build agents and apps faster.

Role of the LLM (Not "just" smarter features)
- Acts as the reasoning and generation layer:
  - Understands natural language, reasons about tasks, chooses tools, interprets tool outputs, and generates structured responses.
- Should not be responsible for security, orchestration, or long-term memory storage.

Components & Where Responsibilities Live
- Security: API gateway, IAM/RBAC, secrets management.
- Context: context builder, RAG pipelines, memory store.
- Knowledge: vector DB, relational DBs, knowledge graphs.
- Orchestration: agent orchestrator, workflows (LangGraph, MCP).
- Actions: tools for DB, Git, Kubernetes, CI/CD, ticketing.
- Scalability & Reliability: Kubernetes, queues, autoscaling, retries, circuit breakers.
- Observability & Governance: OpenTelemetry, Prometheus, Grafana, audit logs, policies.

Simple Architecture (text diagram)

USER → API GATEWAY (Auth, Rate limit)
      → AGENT PLATFORM (orchestrator, context builder, memory)
      → Tools & Data (RAG, Neo4j, Git, DBs, Kubernetes)
      → LLM
      → Response

Enterprise Connections (examples)
- Knowledge sources: Git repos, databases, data warehouses, internal docs, data catalogs.
- Operational systems: Kubernetes, CI/CD, Jira, monitoring, internal APIs.
- AI infra: LLM providers, vector DBs, knowledge graphs, eval tooling.

Day 1 Exercise (requested thought exercise)
Given: "Find all APIs that use the customer_id column and list impacted applications if the column changes." Answer these five questions concisely.

1) Why can't the LLM answer this directly?
- Because it lacks direct access to enterprise systems and up-to-date private data (schemas, source code, deployed services). Tools + data are required.

2) What information would the platform need?
- Database schema and column usage, source-code references, API endpoint definitions, service-to-application mapping, dependency/lineage graph, deployment metadata.

3) Which components would retrieve that information?
- Database tool (schema, column usage), Git/source-code search tool, API catalog or gateway, lineage/dependency tool (graph DB), and deployment/Kubernetes tool.

4) Where would an Agent help?
- The agent plans the investigation, chooses which tools to call in what order, aggregates results, re-queries as needed, and composes the final impact analysis.

5) Final flow (refined):
- User → Agent → Plan → Select & Call Tools (DB, Git, Lineage, K8s) → Observe Results → Reason → Validate → Final Answer

Day 1 Mental Model (four statements)
1. LLM = reasons and generates.
2. Data = provides knowledge/context.
3. Tools = give the AI access to external systems and actions.
4. Agent = decides what to do and orchestrates the process.
5. AI Platform = provides shared infrastructure (security, RAG, memory, observability, governance) for AI apps and agents.

Quick Recommendations / Next Steps
- Keep these notes as `docs/Day01_Notes.md` and update them after each learning day.
- Create a small checklist for the exercise; try implementing a simple agent that runs a `git grep` and a mock DB schema query next.

Status
- Day 1: Complete

References & Notes
- Key terms: RAG, MCP, vector DB, knowledge graph, agent orchestrator, LLM providers (OpenAI/Anthropic/Google).

Action Items (short)
- Save these notes (done).
- Turn exercise into a small repo task next.

RAG / Context	🟡
Tools	🟢
Agent	🟢
Agent loop	🟢
Enterprise AI architecture	🟢

Day 1: COMPLETE ✅

You don't need to search YouTube or read 20 articles tonight. You've understood the fundamental concept we needed.