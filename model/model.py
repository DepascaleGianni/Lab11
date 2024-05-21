from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.graph_products = nx.Graph()
        self._all_products = DAO.get_all_products()
        self._idProducts = {}
        for el in self._all_products:
            self._idProducts[el.Product_number] = el


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
        for prod1 in list(self.graph_products.nodes):
            p1 = prod1.Product_number
            for prod2 in list(self.graph_products.nodes):
                p2 = prod2.Product_number
                if DAO.has_edge(a,p1,p2)[0][0] > 0:
                    w = DAO.get_weight(a,p1,p2)[0][0]
                    self.graph_products.add_edge(prod1,prod2,weight = w)

    def get_num_nodes(self):
        return self.graph_products.number_of_nodes()

    def get_num_edges(self):
        return self.graph_products.number_of_edges()

    def get_max_edges(self):
        edges = sorted(self.graph_products.edges(data=True), key=lambda edge: edge[2].get('weight', 1))
