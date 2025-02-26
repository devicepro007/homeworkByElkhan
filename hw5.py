import colorama as clrm

print(clrm.Style.BRIGHT + "All functions in `colorama`:" + clrm.Style.RESET_ALL)

for i in range(len(dir(clrm))):
    if i == 1 or i == 3 or i == 4:
        print("    " + clrm.Back.CYAN + clrm.Style.BRIGHT + dir(clrm)[i] + clrm.Style.RESET_ALL)

    else:
        print(f"    {dir(clrm)[i]}")

print(f"\n\n{dir(clrm)[1]}\n{dir(clrm)[3]}\n{dir(clrm)[4]}")