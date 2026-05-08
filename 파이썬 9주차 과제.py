import matplotlib.pyplot as plt

course = {
    'TOEIC': 0,
    'TOEFL': 0,
    'OPIC': 0,
    'TEPS': 0,
    'Speaking': 0
}

while True:
    s = input('수강 희망 강좌를 입력하세요. 종료하려면 q 입력: ')

    if s == 'q':
        break

    choices = s.split(',')

    for a in choices:
        a = a.strip()

        if a in course:
            course[a] += 1
        else:
            print(a, '는 등록되지 않은 강좌입니다.')

print(course)

plt.bar(course.keys(), course.values())
plt.title('Popular English Courses')
plt.xlabel('Course')
plt.ylabel('Number of Students')
plt.show()