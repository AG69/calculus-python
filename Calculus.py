r = 1
while r == 1:
    print('')
    li = []
    lii = []
    def slope(a, b, c):
        s = (b-1)
        d = (b*a)
        if a == 1:
            if b == 2:
                return 2*c
            else:
                return b*(c**s)
        elif a == 0:
           return "This line will lie on the 'x' axis, so it will not have a slope :("
        else:
            if b == 2:
                return d*c
            else:
                return d*(c**s)

    def integ(a, b, k, j):
        if a == 1:
            return(j**(b+1))/(b+1) - ((k**(b+1))/(b+1))
        elif a == 0:
            return("This line will lie on the 'x' axis, so the area is 0 :(")
        else:
            return(a*(j**(b+1)))/(b+1) - ((a*(k**(b+1)))/(b+1))

    c = (input("Please type out all coefficients of x with spaces. ")).split()
    p = (input("Please type out all powers of x with spaces ")).split()
    for i in range(len(c)):
        c[i] = int(c[i])
    for i in range(len(c)):
        p[i] = int(p[i])
    e = int(input("Whats x? "))
    si = int(input("Slope or Integral? 1 for slope, 2 for integral: "))

    if si == 1:
        for z in range(len(c)):
            li.append(slope(c[z], p[z], e))
        li[z] = int(li[z])
        print(sum(li))
        r = int(input("Do u want to do it again? 1 for yes, 2 for no. "))
    if si == 2:
        f = int(input("If u want integral, from what is the higher limit? "))
        l = int(input("If u want integral, from what is the lower limit? "))
        for z in range(len(c)):
            lii.append(integ(c[z], p[z], l, f))
        lii[z] = int(lii[z])
        print(sum(lii))
        r = int(input("Do u want to do it again? 1 for yes, 2 for no. "))


