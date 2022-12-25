import pickle


# every is object
# pickeling a python object
cars = ["audi","BMW","royal.am","bugatti"]
file = "mycar.pkl"
fileobj = open(file,'wb')
# you want to file object for pickel.dump
pickle.dump(cars,fileobj)
fileobj.close()


file = "mycar.pkl"
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)
# mycar = pickle.loads(fileobj)
print(mycar)
print(type(mycar))


# pickle.load() - takes file object and return corresponding python format (readable)
# pickle.loads() - takes the binary format and retruns python format
# pickle.dumps() - takes the variable and returns binary string