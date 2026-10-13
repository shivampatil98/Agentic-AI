from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:

    def __init__(self, llm: str):
        self.llm = llm


    def process(self, state: State) -> dict:
        # Implement the logic for the chatbot with tools using the specified LLM and tools
        # For example, you can use the LLM to generate a response based on the input_text and available tools
        user_input = state['messages'][-1] if state['messages'] else ""  # Assuming the last message is the user input
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        return {"messages": [llm_response, tools_response]}  # Assuming tools_response is obtained from the tools based on the user input

    def create_chatbot(self, tools):

        llm_with_tools = self.llm.bind_tools(tools) # Assuming the LLM can handle tool integration

        def chatbot_node(state: State):

            return {"messages": [llm_with_tools.invoke(state['messages'])]}

        return chatbot_node