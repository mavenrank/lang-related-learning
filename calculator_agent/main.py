from dotenv import load_dotenv

load_dotenv()

from agent import run_agent

if __name__ == "__main__":
    result = run_agent("What is (10 + 5) * 2?")
    print(result["output"])
    print(result["steps"])
