terus = True
while terus:
    name = str(input("Input namamu : "))
    college = str(input("Input kampusmu: "))
    print("Informasimu :")
    print("Namamu :", name)
    print("Kampusmu :", college)
    mau_terus = str(input('Mau lanjut daftar lagi gak? y / n : '))
    if(mau_terus == "n"):
        terus = False
    else:
        terus = True
        print("==================================")
