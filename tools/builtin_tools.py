from langchain_community.tools import DuckDuckGoSearchRun
search = DuckDuckGoSearchRun()
# result = search.invoke('what is the name of US current president')
# print(result)

from langchain_community.tools import ShellTool
search = ShellTool()
# result = search.invoke('whoami')
# print(result)

