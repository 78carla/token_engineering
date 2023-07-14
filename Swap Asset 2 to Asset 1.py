# Swap from Asset 2 to Asset 1
genesis = {
    "AMM":{"r1":100,"r2":1000,"s":100,"fee":0.0},
    "Trader":{"r1":100,"r2":100,"s":0},
    "LP":{"r1":0,"r2":0,"s":100}
    }

def swapToAsset1(state,inputs):
    agent = inputs[0]
    dA2 = inputs[1]
    feeFactor = (1-state["AMM"]["fee"])
    dA1 = state["AMM"]["r1"]/(state["AMM"]["r2"]+dA2*feeFactor)*dA2*feeFactor
    if dA2>0 and state[agent]["r2"]-dA2 >= 0 :
        state["AMM"]["r1"]-=dA1
        state[agent]["r1"]+=dA1
        state["AMM"]["r2"]+=dA2
        state[agent]["r2"]-=dA2


swapToAsset1(genesis, ["Trader", 10])

print(genesis)

