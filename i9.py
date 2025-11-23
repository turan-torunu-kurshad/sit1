import pandas as np
list1=["a","d"] 

list_str=["dkdlkw","jodwkwij","nhdikjdk","jnkkjwsnbj"]
dict1={
    "a1":[1,3,2],
    "a2":[4,5,6],
    "a3":[7,8,9],
    "a4":[10,11,12]    

}
dict2_tak_values={
    "z1" : 1 ,
    "z2" : 2 ,
    "z3" : 3 ,
    "z4" : 4 ,
    "z5" : 5 ,
    "z6" : 4 ,
}
mat=[[1,2,3,4,5],[6,7,8,9,10]]
o=np.Series(list1)
o.index=["a","b"]
print(o.describe)

