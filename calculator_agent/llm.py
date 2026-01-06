from langchain_openai import ChatOpenAI

def get_llm():
    return ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        model="mistralai/devstral-2512:free",
        temperature=0.0,
    )
