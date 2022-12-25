# dictionary is nothing but key value pairs
d1 ={}

print(type(d1))
d2 = {"ansh":{"m":"burger","e":"roti","n":"food"},
      "meet":"alu puri",
      "harshit":"pizza",
      "prit":"dabeli"
    }
print(d2)
#indivisual
print(d2["ansh"])
print(d2["ansh"]["m"])     #print anything so use [] breaket only
#add person in d2

d2["rohan"]="fast food"
d2["romin"]="black coffie"
print(d2)
del d2["romin"]
print(d2)
d3=d2.copy()
del d3["meet"]
print(d3)

print(d2.get("ansh"))
print(d2.update({"roy":"toffee"}))
print(d2)

print(d2.keys())
print(d2.items())
