chain = [5, 4, 0, 3, 1, 6, 2]
chain_ = []
idx = 0

count = 0
max_len = 0

while sorted(chain) != sorted(chain_):
    sub_chain = []

    connect = False

    while not connect:
        node = chain[idx]

        if node not in sub_chain:
            sub_chain.append(node)
            idx = node
        else:
            connect = True
            chain_ += sub_chain
            temp = list(set(chain) - set(chain_))
            if len(temp) > 0:
                idx = chain[temp[0]]
    
    max_len = max(max_len, len(sub_chain))

print("The longest length  is", max_len)
