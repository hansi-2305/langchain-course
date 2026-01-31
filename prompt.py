REACT_PROMT_WITH_FORMAT_INSTUCTIONS="""
Answer the following questions as best you can.You have access to the follwoing tools:

{tools}

Use the following format:

Question:the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the aciton
...(this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know thr final answer
Final Answer: the final answer to the original input question formatted according to format_instructions: {format_instructions}

Begin!
Question: {input}
Thought:{agent_scratchpad}

"""