from graphviz import Digraph
dot = Digraph(comment="The Round Table")
dot.node("A","King Arthur")
dot.node("B","Sir B")
dot.node("L","Sir L")
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
# The Round Table
digraph {A [label="King Arthur"]B [label="Sir Bedevere the Wise"]
    L [label="Sir Lancelot the Brave"]
    A -> B
    A -> L
    B -> L [constraint=false]
}