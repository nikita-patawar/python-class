
def filterX(Task,Elements):
    Result = list()
    for No in Elements:
        Ret = Task(No)

        if(Ret == True):
            Result.append(No)
    return Result


def mapX(Task,Elements):
    Result = list()
    for No in Elements:
        Ret = Task(No)
        Result.append(Ret)
    return Result

def reduceX(Task,Elements):
    Sum = 0
    for no in Elements:
        Sum = Task(Sum,no)
    return Sum