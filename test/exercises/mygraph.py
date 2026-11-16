from graphviz import Digraph

class NNGraph():
    
    def __init__(self, p_parms = [], p_shape='record'):
        self.parms = p_parms
        self.shape = p_shape 

    def gv_graph(self):
        def create_graph():
            for i, lp in enumerate(self.parms):
                if i == len(self.parms)-1:
                    print(f"{lp.tag}={lp.grad}")
                    dot.node(lp.tag, label = f'{lp.tag} = {lp.value}|{lp.grad}', shape=self.shape) 

                if len(lp.history)==0:
                    print(f"{lp.tag}={lp.grad}")
                    dot.node(lp.tag, label = f'{lp.tag} = {lp.value}|{lp.grad}', shape=self.shape) 
                else:
                    print(f"{lp.tag}={lp.grad}")
                    dot.node(lp.history[0][0][0], label = 
                             f'{lp.history[0][0][0]} = {lp.history[0][0][1]}|{lp.grad}', 
                             shape=self.shape)
                    dot.node(lp.history[0][1][0], label = 
                             f'{lp.history[0][1][0]} = {lp.history[0][1][1]}|{lp.grad}', 
                             shape=self.shape)
                    dot.edge(lp.history[0][0][0], lp.tag,label=lp.history[0][2][0])
                    dot.edge(lp.history[0][1][0], lp.tag, label = lp.history[0][2][0])
                    
        dot = Digraph(graph_attr={"rankdir":"LR"})
        create_graph()
        return dot
        


        


    