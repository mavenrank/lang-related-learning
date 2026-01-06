from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    ToolMessage,
    BaseMessage,
)
from llm import get_llm
from tools import TOOLS
from state import Step

def run_agent(user_input: str):
    llm = get_llm().bind_tools(list(TOOLS.values()))

    messages: list[BaseMessage] = [
        HumanMessage(content=user_input)
    ]

    steps: list[Step] = []

    while True:
        ai_msg: AIMessage = llm.invoke(messages)
        messages.append(ai_msg)

        if not ai_msg.tool_calls:
            return {
                "output": ai_msg.content,
                "steps": steps,
            }

        for call in ai_msg.tool_calls:
            tool = TOOLS[call["name"]]
            result = tool.invoke(call["args"])

            steps.append(
                Step(
                    tool_name=call["name"],
                    tool_input=call["args"],
                    tool_output=result,
                )
            )

            messages.append(
                ToolMessage(
                    tool_call_id=call["id"],
                    content=str(result),
                )
            )
