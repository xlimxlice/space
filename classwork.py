def findAverage(dictionary):
    for key in dictionary:

        sumArray = 0
        for i in dictionary[key]:
            sumArray = sumArray + i
        avg = round(sumArray / len(dictionary[key]), 2)

        print(f'the average score for {key} i {str(avg)}')

dictionary = {
    'valentine': [10,10,10],
    'romeo': [2,2,2],
    'julliet': [2,3,3]
}
findAverage(dictionary)