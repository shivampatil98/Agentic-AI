from langgraph.graph import Stategraph
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.state.state import State
from langgraph.graph import Stategraph START, END


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = Stategraph(State)

    def basic_chatbot_graph(self):
        self.graph_builder.add_node("Chatbot", BasicChatbotNode(self.llm, "model"))
        self.graph_builder.add_edge("START", "Chatbot")
        self.graph_builder.add_edge("Chatbot", "END")
        return self.graph_builder

    def setup_graph(self, use_case):