import copy

genesis = {
    "AMM":{"r_1":400,"r_2":400,"s":400,"fee":0.0},
    "Trader":{"r_1":100,"r_2":100,"s":0},
    "LP":{"r_1":0,"r_2":0,"s":400}
    }

# Definisce Swap da Token 1  a Token 2
def swapToAsset2(state,inputs):
    agent = inputs[0]
    dA1 = inputs[1]
    feeFactor = (1-state["AMM"]["fee"])
    dA2 = state["AMM"]["r_2"]/(state["AMM"]["r_1"]+dA1*feeFactor)*dA1*feeFactor
    if dA1>0 and state[agent]["r_1"]-dA1 >= 0 :
        state["AMM"]["r_1"]+=dA1
        state[agent]["r_1"]-=dA1
        state["AMM"]["r_2"]-=dA2
        state[agent]["r_2"]+=dA2
    print("*********")
    print(state["AMM"]["r_1"])
    print(state["AMM"]["r_2"])


# Definisce Swap da Token 2  a Token 1
def swapToAsset1(state,inputs):
    agent = inputs[0]
    dA2 = inputs[1]
    feeFactor = (1-state["AMM"]["fee"])
    # dA1 = state["AMM"]["r_1"]/(state["AMM"]["r_2"]+dA2*feeFactor)*dA2*feeFactor
    k = state["AMM"]["r_1"] + state["AMM"]["r_2"]
    dA1 = dA2
    if dA2>0 and state[agent]["r_2"]-dA2 >= 0:
         state["AMM"]["r_2"]+=dA2
         state[agent]["r_2"]-=dA2
         state["AMM"]["r_1"]-=dA1
         state[agent]["r_1"]+=dA1
    print("---------")
    print(state["AMM"]["r_1"])
    print(state["AMM"]["r_2"])


def evolve(state, actionStack):
    history = [copy.deepcopy(state)]
    for action in actionStack:
        action[0](state,action[1])
        history.append(copy.deepcopy(state))
    return history


actionList = [
        [ swapToAsset2 , [  "Trader" , 20 ]],
        [ swapToAsset1 , [  "Trader" , 20 ]]
    ]


print("!!!!!!!")
print(genesis)

i = 1
while i <= 299:
    evolve(genesis, actionList)
    print("=========")
    print(genesis)
    i += 1

print(genesis)
