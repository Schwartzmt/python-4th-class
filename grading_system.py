#Grading Systems

print("Enter marks for these subjects: ")

math=int(input("Math: "))

eng=int(input("Eng: "))

french=int(input("French: "))

music=int(input("music: "))

aviation=int(input("Aviation: "))

av_score=(math+eng+french+music+aviation)/5

print("av_score: ",av_score)

av_grade=""

if av_score>=90 and av_score<=100:

  print("A")

elif av_score<=80 and av_score<=99:

  print("B")

elif av_score>=70 and av_score<=79:

  print("C")

elif av_score>=60 and av_score<=69:

  print("D")

elif av_score>=50 and av_score<=59:

  print("E")
