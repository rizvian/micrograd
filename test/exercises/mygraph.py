from graphviz import Digraph

class NNGraph():
    
    def __init__(self, p_parms = [], p_shape='record'):
        self.parms = p_parms
        self.shape = p_shape 

    def gv_graph(self):
        def create_graph():
            for i, lp in enumerate(self.parms):
                dot.node (lp.tag, label = f"{lp.tag} = {lp.value}|{lp.grad}", shape = self.shape)

            for lp in self.parms:
                if len(lp.children) > 0:
                    dot.edge(lp.children[0].tag, lp.tag)
                    dot.edge(lp.children[1].tag, lp.tag)

                    
        dot = Digraph(graph_attr={"rankdir":"LR"})
        create_graph()
        return dot
        


        


    