hmm = {"red": 4, "yellow": 5}


# def key_magic(diqt,key):
# return (f"{key} " * key[val]).split()


# print(lon)


# def bruh(**kwargs):
#     lon = list()
#     for key, val in kwargs.items():
#         lon += (f"{key} * {key[val]}").split()
#     return lon


# print(bruh(blu=5, ef=5))


def hmm(**kwargs):
    for key in kwargs.keys():
        print(key, kwargs[key])


hmm(mwah=4, k=5)
