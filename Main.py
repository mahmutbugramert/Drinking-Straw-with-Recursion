
glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
if straw_pos % 2 == 0:
    q = 2*glass_size-straw_pos+4
else:
    q = 2 * glass_size - straw_pos + 3
# this if statement determines number of glasses.
def whole_glass(g, m):
# this is the function which draws whole one glass.
    if g == 0:
        return
    def space1(n):
    # space functions draw spaces.
        print(" ", end="")
        if n == 1:
            return
        space1(n-1)

    def func(a):
    # this function draws straw above the glass.
        if a == straw_pos:
            print("o")
        if a == 1:
            return
        func(a - 1)
        space1(a-1)
        print("o")

    func(straw_pos)

    def space2(n):
    # space functions draw spaces.
        if n == 1:
            return
        space2(n - 1)
        print(" ", end="")

    def star(k):
    # this function draws stars.
        if k == glass_size:
            print("*", end="")
            print("*", end="")
            return
        star(k+1)
        print("*", end="")
        print("*", end="")

    def mostar(p):
    # this function draws spaces before the straw inside the glass.
        if p == 0:
            return
        print(" ", end="")
        mostar(p-1)

    def nostar(f):
    # this function draws spaces after the straw inside the glass
        if f == 0:
            return
        print(" ", end="")
        nostar(f-1)

    def func2(a, b):
    # this function draws upper part of glass.
        if a == 1:
            return
        func2(a - 1, b - 1)
        space2(a-1)
        print("\\", end="")
        if a <= m:
        # this if determines whether to draw stars or straw.
            mostar(straw_pos-1)
            print("o", end="")
            nostar(2 * (glass_size - b) - straw_pos)
        else:
            star(a-1)
        print("/")

    func2(glass_size+1, glass_size-1)

    def space3(n):
    # space functions draw spaces.
        if n == 0:
            return
        print(" ", end="")
        space3(n-1)

    space3(glass_size)
    print("--")

    def func3_5(a):
    # this function draws lower part of glasses.
        if a == 0:
            return
        space3(glass_size)
        print("||")
        func3_5(a-1)

    func3_5(glass_size)

    whole_glass(g - 1, m+1)
whole_glass(q / 2, 1)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
