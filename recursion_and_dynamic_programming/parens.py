def parens(leftParen, rightParen, output=""):
    if leftParen < 0 or rightParen < leftParen:
        return

    if leftParen == 0 and rightParen == 0:
        print(output)

    parens(leftParen-1, rightParen, output+"(")
    parens(leftParen, rightParen-1, output+")")

parens(3, 3)