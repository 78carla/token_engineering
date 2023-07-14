# A swap from Asset 1 to Asset 2
genesis = {
    "AMM":{"r1":100,"r2":100,"s":100,"fee":0.0},
    "Trader":{"r1":100,"r2":100,"s":0},
    "LP":{"r1":0,"r2":0,"s":100}
    }


def swapToAsset2(state,inputs):
    agent = inputs[0]
    dA1 = inputs[1]
    feeFactor = (1-state["AMM"]["fee"])
    dA2 = state["AMM"]["r2"]/(state["AMM"]["r1"]+dA1*feeFactor)*dA1*feeFactor
    if dA1>0 and state[agent]["r1"]-dA1 >= 0 :
        state["AMM"]["r1"]+=dA1
        state[agent]["r1"]-=dA1
        state["AMM"]["r2"]-=dA2
        state[agent]["r2"]+=dA2


swapToAsset2(genesis, ["Trader", 10])

print(genesis)
