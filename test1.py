stuin =input()
if "$" in stuin or "USD" in stuin :
    if stuin[-1] == "$": print(stuin + "美元转化人民币"+str(int(stuin[:-1])*6.78))
    else:print(stuin + "美元转化人民币" + str(int(stuin[:-3]) * 6.78))
elif "RMB" in stuin or "¥" in stuin  :
    if stuin[-1] == "¥":print(stuin + "人民币10转化美元" + str(round(int(stuin[:-1]) / 6.78,2)))
    else:print(stuin + "人民币转化美元" + str(round(int(stuin[:-3]) / 6.78,2)))



