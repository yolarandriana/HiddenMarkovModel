import numpy as np





states = np.array([1, 2])
transitions = [['s1', '11', '12'],
                        ['s2', '21','22']]
transitionMatrix = [[.3, 0.2,0.8],
                             [.7, 0.1,0.9]]

emissions = np.array(['a', 'b'])

startprobability = np.array([.3, .7])

emission_probability = [[.4, .6], #a,b given state 1
                                [.9, .1]] #a, b given state 2 


def forward(sequence): #aba #how likely
    answers = [[0,0, 0],
                            [0,0, 0]]
    probs = [0, 0, 0]
    keys = np.array([[1, 1, 1],
                        [2, 2, 2]])
    i = -1
    if len(sequence) > 3:
        return("3 letter sequences only please")
    for char in sequence:
        i+=1
        if char == "a":
            for state in range(1, 3):
                for trans in range(2):
                    probs[i] += emission_probability[state - 1][0] * transitionMatrix[trans][state -1]
        elif char == "b":
            for state in range(1, 3):
                for trans in range(2):
                    probs[i] += emission_probability[state - 1][1] * transitionMatrix[trans][state -1]

        else:
            return "Only include a's and b's in your sequence"
    return probs[0] * probs[1] * probs[2]


def viturbi(sequence): #most likely state sequence
    answers = [[0,0, 0],
                            [0,0, 0]]
    probs = np.array([0, 0, 0])
    keys = np.array([[1, 1, 1],
                        [2, 2, 2]])
    i = int(0)
    j = int(0)
    seqstr = ""
    if len(sequence) > 3:
        return("3 letter sequences only please")
    if sequence[0] == "a":
        for state in range(1, 3):
            answers[state - 1][0] += max(emission_probability[state - 1][0] * transitionMatrix[0][state -1], emission_probability[state - 1][0] * transitionMatrix[1][state -1])

    if sequence[0] == "b":
        for state in range(1, 3):
            answers[state - 1][0] += max(emission_probability[state - 1][1] * transitionMatrix[0][state -1], emission_probability[state - 1][1] * transitionMatrix[1][state -1])
    currentstate = max(answers[0][0], answers[1][0])
    if currentstate == answers[0][0]:
        currentstate = int(1)
    else:
        currentstate = int(2)
    


    for char in sequence[1:]:
        i += 1
       
        answers[currentstate][i] += max(answers[currentstate][i -1], answers[currentstate - 1][i-1]) * transitionMatrix[currentstate][i]

    while j < 3:
        currentstate = max(answers[0][j], answers[1][j])
        if currentstate == answers[0][j]:
            currentstate = int(1)
        else:
            currentstate = int(2)
        j+=1
        seqstr += str(currentstate)
    return seqstr
        


print(forward("aba"))
print(viturbi("aba"))
