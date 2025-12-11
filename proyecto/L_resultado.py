import json

with open("z_resultado_raiz.json","r") as f:
    union_t=json.load(f)
with open("z_resultado_no_raiz.json","r") as f:
    union_t2=json.load(f)

print("-----------------------------------------------------------------")
print("Con raiz:")
print(union_t)
print("-----------------------------------------------------------------")
print("Sin raiz:")
print(union_t2)
print("-----------------------------------------------------------------")
print("-----------------------------------------------------------------")
total=list(set(union_t) & set(union_t2))
print(total)
print("-----------------------------------------------------------------")