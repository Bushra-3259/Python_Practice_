from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator (a: float, b: float) -> str: #taking 2 float paramenters & returning a string 
    """Useful for calculating basic arithmetic operations with  numbers."""
    print("The tool has been called.") #to check if the list tool[] is working 
    return f" The sum of {a} and {b} is {a + b}."

@tool
def say_hello (name:str) -> str: #taking 2 float paramenters & returning a string 
    """Useful for greeting a user."""
    print("The tool has been called.") #to check if the list tool[] is working 
    return f" Hello {name}, I hope you are good today."

def main():
    model = ChatOpenAI(temperature=0)

    tools = [calculator, say_hello]
    agent_executor = create_react_agent(model, tools)

    print("Hi, and welcome! I'm your AI companion. Ask me anything — from math to memes. Type 'quit' to make a dramatic exit!")

    while True:
        user_input = input("\n You: ").strip()

        if user_input == "quit":
            break

        print("\nAssistant: ", end=" ")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage (content= user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk ["agent"]["messages"]:
                    print(message.content, end="")

        print()

if __name__ == "__main__":
    main()
