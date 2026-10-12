class BasicChatbotNode:

    def __init__(self, llm: str, model: str):
        self.llm = llm
        self.model = model

    def process(self, state: State) -> dict:
        # Implement the logic for the basic chatbot using the specified LLM and model
        # For example, you can use the LLM to generate a response based on the input_text
        return {"messages": self.llm.invoke(state['messages'])}