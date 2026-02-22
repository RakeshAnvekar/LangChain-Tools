from langchain_core.tools import tool
# Custom tool using the @tool decorator

@tool
def add(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b

@tool
def subtract(a: int, b: int) -> int:
    """Subtracts the second number from the first number."""
    return a - b

class MathToolKit:
    def get_tools(self):
        return [add, subtract]
    

# Example usage
toolkit = MathToolKit()
tools = toolkit.get_tools()
result_add = tools[0].invoke({"a": 5, "b": 3})
result_subtract = tools[1].invoke({"a": 5, "b": 3})
print(f"Addition Result: {result_add}")
print(f"Subtraction Result: {result_subtract}")

for tool in tools:
    print(f"Tool Name: {tool.name}")
    print(f"Tool Description: {tool.description}")
    print(f"Tool Arguments Schema: {tool.args_schema.model_json_schema()}")
   