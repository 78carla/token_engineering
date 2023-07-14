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


genesis = {
    "AMM":{"r_1":100,"r_2":100,"s":100,"fee":0.0},
    "Trader":{"r_1":100,"r_2":100,"s":0},
    "LP":{"r_1":0,"r_2":0,"s":100}
    }

actionList = [
        [ removeLiquidity , [  "LP" , 5 ]],
        [ removeLiquidity , [  "LP" , 5 ]],
        [ removeLiquidity , [  "LP" , 5 ]]

genesis