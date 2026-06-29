from langchain.agents import create_agent
from langchain_core.tools import tool
from Agents.agents import hospital_agent,institution_agent,restaurant_agent
from tool.webSearchTool import search
from config import llm
@tool
def hospital_data(query: str) -> str:
    """Useful for questions about hospitals, doctors, beds, clinics, medical facilities, health, ICUs, and emergencies."""
    return hospital_agent.invoke(query)

@tool
def institution_data(query: str) -> str:
    """Useful for questions about universities, colleges, schools, educational institutions, EIINs, education, and campuses."""
    return institution_agent.invoke(query)

@tool
def restaurant_data(query: str) -> str:
    """Useful for questions about restaurants, food, ratings, addresses, reviews, and cafes."""
    return restaurant_agent.invoke(query)

@tool
def web_search(query: str) -> str:
    """Useful for general knowledge, current events, policies, laws, definitions, explanations, and topics outside the databases."""
    return search.run(query)

# ---------------------------
# List of tools
# ---------------------------

tools = [
    hospital_data,
    institution_data,
    restaurant_data,
    web_search,
]

# ---------------------------
# Create the agent
# ---------------------------

main_agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=(
        "You are a helpful AI assistant. "
        "Choose the appropriate tool based on the user's question. "
        "Use hospital_data for hospital questions, "
        "institution_data for educational institution questions, "
        "restaurant_data for restaurant questions, "
        "and web_search for everything else."
    ),
)

# ---------------------------
# Ask function
# ---------------------------

def ask_agent(question: str):
    print(f"\nRouting question: {question}\n")

    try:
        response = main_agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": question,
                    }
                ]
            }
        )

        return response["messages"][-1].content

    except Exception as e:
        return f"Error: {e}"