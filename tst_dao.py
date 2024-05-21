from database.DAO import DAO

colors = DAO.get_colors()
#print(colors)
prdo = DAO.get_nodes("Red")
edges = DAO.has_edge(2015,109110,1110)
print(edges[0][0])
w = DAO.get_weight(2015,109110,1110)
print(w)