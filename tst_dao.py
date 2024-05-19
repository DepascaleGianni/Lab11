from database.DAO import DAO

colors = DAO.get_colors()
#print(colors)
prdo = DAO.get_nodes("Red")
for el in prdo:
    print(el)
print(prdo)