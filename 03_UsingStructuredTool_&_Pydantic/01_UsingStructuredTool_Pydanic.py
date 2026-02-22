from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

# 1️ Define input schema
class MultiplyInput(BaseModel):
    a: int = Field(..., description="The first number to multiply")
    b: int = Field(..., description="The second number to multiply")

# 2️ Define function
def multiply_func(a, b) -> int:
    return a * b

# 3️ Create tool
multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Multiplies two numbers together",
    args_schema=MultiplyInput
)

# 4️ Test
result = multiply_tool.invoke({"a": 3, "b": 4})
print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args_schema.model_json_schema())