def myfunc(arg):
    '''
    Summary: Write a Python program to compute the person's itinerary.

    Parameters: Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport.
    Returns: compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.
    '''
    # find the item which matches arg[1]
    itinerary=[]
    for i in arg[0]:
        if i[0]==arg[1]:
            itinerary.append(i)

    # for i in arg[0]:
    #     if i == step1:
    #         itinerary.append(i)
    # for i in range(len(arg[0])):
    #     if arg[0][i]== step1:
    #         itinerary.append(arg[0][i])
    for i in range(len(arg[0])+1):
        try:
            if arg[0][i][0]==itinerary[i-1][1]:
                itinerary.append(arg[0][i])
        except:
            pass
    for i in range(len(arg[0])+1):
        try:
            if arg[0][i][0]==itinerary[i-1][1]:
                itinerary.append(arg[0][i])
        except:
            pass

        # else:
        #     itinerary.append('not valid')
    # chain the items into a list
    # compare lexigraphic lengths and return smallest
    return arg[0], arg[1],  itinerary

if __name__=='__main__':
    for arg in [
            [[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'],
            [[('SFO', 'COM'), ('COM', 'YYZ')], 'COM'],
            [[('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'],
            ]:
            print(myfunc(arg))
