#Grading Systems

print("Enter marks for these subjects: ")

math=int(input("Math: "))

eng=int(input("Eng: "))

french=int(input("French: "))

music=int(input("music: "))

aviation=int(input("Aviation: "))

av_score=(math+eng+french+music+aviation)/5

av_grade=""

if av_score>=70 and av_score<=100:

  av_grade="A"

elif av_scre<=60 and av_score<=69:

  av_grade="B"

elif av_score>=50 and av_score<=59:

  av_grade="C"

elif av_score>=40 and av_score<=49:

  av_grade="D"

elif av_score>=30 and av_score<=39:

  av_grade="Fail"

if math or eng or french or music or aviation <0 and math or eng or french or music or aviation >100:

  print("Enter a valid input!...")

else:

  print("Your average grade is: ",av_grade)

  print("Average score is: ",av_score)