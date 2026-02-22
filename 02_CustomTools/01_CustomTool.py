from langchain_core.tools import tool

#step 1: create a function that performs the desired action
@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers together."""
    return a * b
#step 2: invoke the tool
result = multiply.invoke({"a": 5, "b": 10})
print(result)
print(multiply.name)
print(multiply.args)
print(multiply.description)
print(multiply.args_schema.model_json_schema())
