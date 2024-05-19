from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.graph_products = nx.Graph()

    def get_years(self):
        return DAO.get_all_year()

    def get_colors(self):
        return DAO.get_colors()

    def build_graph(self,a,c):
        self.graph_products.clear()
        self.add_nodes(c)
        self.add_edges(a)
        print("grafo creato")

    def add_nodes(self,c):
        nodes = DAO.get_nodes(c)
        self.graph_products.add_nodes_from(nodes)

    def add_edges(self,a):
        pass

    def get_num_nodes(self):
        return self.graph_products.number_of_nodes()

    def get_num_edges(self):
        return self.graph_products.number_of_edges()
