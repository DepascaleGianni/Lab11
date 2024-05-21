from model.model import Model

m = Model()

m.build_graph(2018,"White")
print(m.get_num_nodes())
print(m.get_num_edges())