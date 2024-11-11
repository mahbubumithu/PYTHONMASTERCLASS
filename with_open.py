with open("logs.txt") as mylogfile:
    for lines in mylogfile:
        if "WARNING" in lines:
            print(lines)