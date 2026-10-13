from langgraph.graph import StateGraph
from langgraph.prebuilt import tools_condition, ToolNode
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.state.state import State
from langgraph.graph import START, END
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node
from src.langgraphagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):

        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("Chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "Chatbot")
        self.graph_builder.add_edge("Chatbot", END)

        return self.graph_builder

    def chatbot_with_tools_build_graph(self):
        # Implement the logic for building the graph for the "Chatbot with Tools" use case
        tools = get_tools()
        tool_node = create_tool_node(tools)

        llm = self.llm

        obj_chatbot_with_node = ChatbotWithToolNode(llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)

        self.graph_builder.add_node("Chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)
        self.graph_builder.add_edge(START, "Chatbot")
        self.graph_builder.add_conditional_edges("Chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "Chatbot")

    def setup_graph(self, usecase: str):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "Chatbot with Web":
            self.chatbot_with_tools_build_graph()
        else:
            raise ValueError(f"Unsupported use case: {usecase !r}")

        return self.graph_builder.compile()
