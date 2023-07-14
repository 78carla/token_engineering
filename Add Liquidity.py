#Definisce aggiunta liquidità
genesis = {
    "AMM":{"r_1":100,"r_2":100,"s":100,"fee":0.0},
    "Trader":{"r_1":100,"r_2":100,"s":0},
    "LP":{"r_1":0,"r_2":0,"s":100}
    }


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

actionList = [
        [ addLiquidity , [  "LP" , 5 ]],
        [ addLiquidity , [  "LP" , 5 ]],
        [ addLiquidity , [  "LP" , 5 ]]

print(genesis)