from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
# from langchain.agents import AgentExecutor
from langgraph.prebuilt import create_react_agent
# from langgraph.prebuilt import create_react_agent (deprecated)
# from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers"""
    # print("Tool has been called.")
    return f"The sum of {a} and {b} is {a+b}"

def main():
    model = ChatOpenAI(temperature=0)
    tools = [calculator]

    # agent_executor = create_agent(model, tools)
    agent = create_react_agent(model, tools)
    # agent_executor = AgentExecutor(agent=agent, tools=tools)

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        result = agent.invoke(
            {"messages": [HumanMessage(content=user_input)]}
        )

        # print("\nAssistant:", result["output"])
        print("\nAssistant:", result["messages"][-1].content)
        
        # print("\nAssistant: ", end="")

        # for chunk in agent_executor.stream(
        #     {"messages": [HumanMessage(content=user_input)]}
        # ):
        #     if "agent" in chunk and "messages" in chunk["agent"]:
        #         for message in chunk["agent"]["messages"]:
        #             print(message.content, end="")
        
        # print()

if __name__ == "__main__":
    main()