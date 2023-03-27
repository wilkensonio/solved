if __name__ == '__main__':
    '''
    input:
    3
    Krishna 67 68 69
    Arjun 70 98 63
    Malika 52 56 60
    Malika

    output: 56.00 
    '''
    n = int(input())  # number of student records
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    total_avg = 0
    # .get() if key does not exist return empty list else iterate list
    for avg in student_marks.get(query_name, []):
        total_avg += avg

    print(f'{total_avg / len(student_marks[query_name]):.2f}')
