def multiples(lw, up, diver):
    diff = diver-lw
    for i in range(lw+diff, up, diver):
        print (i)

divnum = int(input("Enter the number to be divided by: "))
lwrange = int(input("Enter lower range limit: "))
uprange = int(input("Enter upper range limit: "))


multiples(lwrange, uprange, divnum)