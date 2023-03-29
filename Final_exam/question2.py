def average():
    test1 = int(input("Enter the score for test 1:"))
    test2 = int(input("Enter the score for test 2:"))
    test3 = int(input("Enter the score for test 3:"))
    avg = (test1+test2+test3)/3
    avg_round = round(avg,2)
    print("Averge score:", avg_round)

    if avg >= 90:
        return "Letter grade:A"
    elif avg >=80 and avg <=90:
        return "Letter grade:B"
    elif avg >=70 and avg <=80:
        return "Letter grade:C"
    elif avg >=60 and avg <=70:
        return "Letter grade:D"
    elif avg < 60:
        return "Letter grade:F"




message = average()
print(message)