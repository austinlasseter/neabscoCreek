def findave(n, diction, student):
    outputlist=[]
    for key in diction.keys():
        if key==student:
            outputlist.append(key)
    scores = diction[outputlist[0]]
    final = "{:.2f}".format(sum(scores)/len(scores))
    return final

if __name__ == '__main__':
    n = 3
    student_marks = {'Krishna': [67, 68, 69],
    'Arjun': [70, 98, 63],
    'Malika': [52, 56, 60],}
    student = 'Malika'
    output = findave(n, student_marks, student)
    print(output)
