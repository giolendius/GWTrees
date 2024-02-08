from  trees_and_percolation import Tree, rdsq

max_off = 4


for i in range(1, 100):
    p = i/100
    seq = rdsq(30, 0, max_off)
    T = Tree(seq)
    m = max_off/2
    T.generate_field(p)
    print(f"""m ={m}. p={p}. {T.percolation()}""")


