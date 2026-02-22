from langchain_core.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

# 1️ Input schema
class MultiplyInput(BaseModel):
    a: int = Field(..., description="The first number to multiply")
    b: int = Field(..., description="The second number to multiply")

# 2️ Tool definition
class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiplies two numbers together"
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b

# 3️ Create instance
multiply_tool = MultiplyTool()

# 4️ Invoke
result = multiply_tool.invoke({"a": 5, "b": 10})
print(result)