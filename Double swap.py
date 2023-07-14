import copy

genesis = {
    "AMM":{"r_1":100,"r_2":100,"s":100,"fee":0.0},
    "Trader":{"r_1":100,"r_2":100,"s":0},
    "LP":{"r_1":0,"r_2":0,"s":100}
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

# Definisce Swap da Token 2  a Token 1
def swapToAsset1(state,inputs):
    agent = inputs[0]
    dA2 = inputs[1]
    feeFactor = (1-state["AMM"]["fee"])
    dA1 = state["AMM"]["r_1"]/(state["AMM"]["r_2"]+dA2*feeFactor)*dA2*feeFactor
    if dA2>0 and state[agent]["r_2"]-dA2 >= 0 :
        state["AMM"]["r_2"]+=dA2
        state[agent]["r_2"]-=dA2
        state["AMM"]["r_1"]-=dA1
        state[agent]["r_1"]+=dA1

#Definisce aggiunta liquidità
def addLiquidity(state, inputs):
    agent = inputs[0]
    R1 = state["AMM"]["r_1"]
    R2 = state["AMM"]["r_2"]
    S = state["AMM"]["s"]
    dA1 = min(inputs[1], R1 / R2 * inputs[2])
    dA2 = min(inputs[2], R2 / R1 * inputs[1])
    if (dA1 <= state[agent]["r_1"] and dA2 <= state[agent]["r_2"]) and (dA1 > 0 and dA2 > 0):
        state[agent]["r_1"] -= dA1
        state[agent]["r_2"] -= dA2
        state["AMM"]["r_1"] += dA1
        state["AMM"]["r_2"] += dA2
        dS = min(dA1 / R1, dA2 / R2) * S
        state["AMM"]["s"] += dS
        state[agent]["s"] += dS

#Definisce rimozione liquidità
def removeLiquidity(state,inputs):
    dS = inputs[1]
    agent = inputs[0]
    if dS > 0 and state[agent]["s"]-dS>=0 and state["AMM"]["s"]-dS>=0:
        DR = (1-dS/state["AMM"]["s"])
        R1=state["AMM"]["r_1"]
        R2=state["AMM"]["r_2"]
        state[agent]["s"]-=dS
        state["AMM"]["r_1"]=R1*DR
        state["AMM"]["r_2"]=R2*DR
        state[agent]["r_1"]+=R1-state["AMM"]["r_1"]
        state[agent]["r_2"]+=R2-state["AMM"]["r_2"]
        state["AMM"]["s"]-=dS


def evolve(state, actionStack):
    history = [copy.deepcopy(state)]
    for action in actionStack:
        action[0](state,action[1])
        history.append(copy.deepcopy(state))
    return history


actionList = [
        [ swapToAsset2 , [  "Trader" , 50 ]],
        [ swapToAsset1 , [  "Trader" , 25 ]]
    ]


evolve(genesis, actionList)

print (genesis)
