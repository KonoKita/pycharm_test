def delete_nth(order, max_e):
    clean_order = []

    for motif in order:
        if clean_order.count(motif) < max_e:
            clean_order.append(motif)
    return clean_order

order = [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1]
max_e = 3

print(delete_nth(order, max_e))
