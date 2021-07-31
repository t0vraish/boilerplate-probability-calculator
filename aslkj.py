import random

hmm = [
    "phx",
    "faya",
    "mind",
    "trash",
    "t0va",
    "luci",
    "a5eel",
    "2srya",
    "devilmaycry",
    "love",
    "flutter",
]
# meh = random.choice(hmm)
# hmm.remove(meh)
# oh = random.choice(hmm)
# print(f"{meh} asks {oh}")


# def sPiN_bOtTlE(member_list):
#     spare_list = member_list
#     asker = random.choice(member_list)
#     spare_list.remove(asker)
#     rcvr = random.choice(spare_list)
#     return f"+ {asker} ??? {rcvr}\n"

random.shuffle(hmm)
print(hmm)
for name in hmm:
    print(name)
