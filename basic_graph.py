from typing import TypedDict
from langgraph.graph import StateGraph, END

# Etat partagé
class State(TypedDict):
    message: str

# Noeud 1
def node_1(state):
    print("Node 1")
    return {"message": state["message"] + " Bonjour"}

# Noeud 2
def node_2(state):
    print("Node 2")
    return {"message": state["message"] + " LangGraph"}

# Création du graphe
workflow = StateGraph(State)

workflow.add_node("node1", node_1)
workflow.add_node("node2", node_2)

workflow.set_entry_point("node1")

workflow.add_edge("node1", "node2")
workflow.add_edge("node2", END)

app = workflow.compile()

result = app.invoke({"message": "TP"})
print(result)