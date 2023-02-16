def students_credits(*args):
    courses = {}

    for i in range(len(args)):
        line = args[i].split('-')
        course = line[0]
        credits = int(line[3])
        maxTestPoints = int(line[2])
        points = int(line[1])

        if(course not in courses):
            courses[course] = 0

        reachedPoints = (points / maxTestPoints) * 100
        currentCredit = (credits * reachedPoints) / 100
        courses[course] = currentCredit
        
    output = []

    sortedDictionary = sorted(courses.items(), key=lambda x: (-float(x[1])))
    sumOfGrades = sum(courses.values())

    if(sumOfGrades >= 240):
        diploma = f"Diyan gets a diploma with {sumOfGrades:.1f} credits."
        output.append(diploma)
    else:
        noDiploma = f"Diyan needs {240 - sumOfGrades:.1f} credits more for a diploma."
        output.append(noDiploma)

    for i in range(len(sortedDictionary)):
        output.append(f"{sortedDictionary[i][0]} - {sortedDictionary[i][1]:.1f}")

    return '\n'.join(output)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
