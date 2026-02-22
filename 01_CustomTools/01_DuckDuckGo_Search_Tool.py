from langchain_community.tools import DuckDuckGoSearchRun

searchTool = DuckDuckGoSearchRun()
result=searchTool.invoke("top news in india")
print(result)