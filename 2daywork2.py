#print("Geçtiğimiz ve kaldığımız dersleri liste şeklinde tutalım.")

lessonCount = int(input("Kaç adet ders notu gireceksiniz."))
passedExams = 0
failedExams = 0


vizeNotList = []
finalNotList = []
lessonResult = []

vizeNotList2 = []
finalNotList2 = []
lessonResult2 = []

for i in range(lessonCount):
    lessonExam1 = float(input(f"{i+1},ders için vize notu giriniz."))
    vizeNotList.append(lessonExam1)
    vizeNotList2.append(f"{i+1}.ders {lessonExam1}")
    
    lessonExam2 = float(input(f"{i+1},ders için final notu giriniz."))
    finalNotList.append(lessonExam2)
    finalNotList2.append(f"{i+1}.ders {lessonExam2}")
    
    totalExamNote = (lessonExam1 * 0.4) + (lessonExam2 * 0.6)
    lessonResult.append(totalExamNote)
    lessonResult2.append(f"{i+1}.ders {totalExamNote}")
    
    if totalExamNote >= 50:
        passedExams += 1
    else:
           failedExams += 1

print()
print(f"{passedExams} adet dersten geçtiniz. {failedExams} adet dersten kaldınız.")
print()
print(f"vize  notları:{vizeNotList}")
print(f"final notları:{finalNotList}")
print(f"ders sonuç notları:{lessonResult}")
print()

print("!!! Her notun önüne kaçıncı ders olduğunu ekledik !!!")
print(f"vize  notları:{vizeNotList2}")
print(f"final notları:{finalNotList2}")
print(f"ders sonuç notları:{lessonResult2}")
