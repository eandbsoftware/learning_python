import pickle
from _0967_OOP_and_Composition import PizzaShop

shop = PizzaShop()
print(shop.server, shop.chef)
pfile = open(r'resources\shopfile.pkl', 'wb')
pickle.dump(shop, pfile)
pfile.close()

obj = pickle.load(open(r'resources\shopfile.pkl', 'rb'))
print(obj.server, obj.chef)
print()

obj.order('LSP')