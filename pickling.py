import pickle
pickle_off = open("model.pkl","rb")
emp = pickle.load(pickle_off)
print(emp)