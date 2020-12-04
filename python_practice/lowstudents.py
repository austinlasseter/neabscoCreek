def lowstudents(*args):
    webster={}
    for i in args[0]:
        webster[i[0]] = i[1]
    lowest=min(list(webster.values()))
    newlist=[i for i in webster.values() if i > lowest]
    second = min(newlist)
    second_lowest=[]
    for key, value in webster.items():
        if value==second:
            second_lowest.append(key)
    return second_lowest
    # indexkey = scores.index(min(scores))
    # lowestp=people[indexkey]
    # lowests=scores[indexkey]
    #
    # newpeople=[i for i in people if i !=lowestp]
    # newscores=[i for i in scores if i !=lowests]
    #
    # newmin = min(newscores)
    # finaltups = [(i,j) for (i,j) in args[0] if j!=newmin]

if __name__ == '__main__':
    for i in range(5):
        marksheet=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
    output = lowstudents(marksheet)
    for i in sorted(output):
        print(i)
