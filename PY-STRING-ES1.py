# devsmachna
# Esercizio 8

def multi_list(l):
    return [
        [x for x in l if isinstance(x, str)],
        [x for x in l if isinstance(x, (int, float, complex)) and not isinstance(x, bool)],
        [x for x in l if isinstance(x, bool)]
    ]