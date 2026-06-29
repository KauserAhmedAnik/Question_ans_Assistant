from langchain_community.agent_toolkits import create_sql_agent
from config import llm
from scripts.SQL_connections import (
    hospital_db,
    institution_db,
    restaurant_db,
)
hospital_agent = create_sql_agent(
    llm=llm,
    db=hospital_db,
    agent_type="openai-tools",
    verbose=True
)

institution_agent = create_sql_agent(
    llm=llm,
    db=institution_db,
    agent_type="openai-tools",
    verbose=True
)

restaurant_agent = create_sql_agent(
    llm=llm,
    db= restaurant_db,
    agent_type="openai-tools",
    verbose=True
)

print("✅ All SQL Agents Created")