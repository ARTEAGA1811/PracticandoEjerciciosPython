import gameOfLife2

class Test_GameOfLife2_Solucionar:
    def test_solucionar_1(self):
        gameOfLife2.solucionar(["Hello, world!", "foo bar", "This is a Text", "Foo bar", "This is a Text", "This is a Text", "Foo bar"], "rgb(20%,10%,30%)")

    def test_solucionar_2(self):
        gameOfLife2.solucionar([["*", ["a", "b", "043", "foo bar"], [-1, 0.5, 1, 2, 3, 4, 5], "*"], [["a", "b", "043", "foo bar"], ["a", "b", "043", "foo bar"], ["foo bar", -0.353, "**text**", 4653], [10, -45.9, 103.5, 0.955674]], [["foo bar", -0.353, "**text**", 4653], "*", [-1, 0.5, 1, 2, 3, 4, 5], [-1, 0.5, 1, 2, 3, 4, 5]], [[-1, 0.5, 1, 2, 3, 4, 5], "*", [-1, 0.5, 1, 2, 3, 4, 5], ["a", "b", "043", "foo bar"]], [["foo bar", -0.353, "**text**", 4653], [-1, 0.5, 1, 2, 3, 4, 5], "*", ["foo bar", -0.353, "**text**", 4653]], ["*", ["a", "b", "043", "foo bar"], "*", "*"], [["a", "b", "043", "foo bar"], "*", "*", ["a", "b", "043", "foo bar"]]], "hsl(10%,20%,40%)")

    def test_solucionar_3(self):
        gameOfLife2.solucionar([[[10, -45.9, 103.5, 0.955674], ["a", "b", "043", "foo bar"], ["foo bar", -0.353, "**text**", 4653], ["foo bar", -0.353, "**text**", 4653]], [[10, -45.9, 103.5, 0.955674], "*", [-1, 0.5, 1, 2, 3, 4, 5], [10, -45.9, 103.5, 0.955674]], [["a", "b", "043", "foo bar"], "*", ["foo bar", -0.353, "**text**", 4653], [-1, 0.5, 1, 2, 3, 4, 5]], [["foo bar", -0.353, "**text**", 4653], [10, -45.9, 103.5, 0.955674], "*", [10, -45.9, 103.5, 0.955674]], [["a", "b", "043", "foo bar"], ["foo bar", -0.353, "**text**", 4653], ["a", "b", "043", "foo bar"], "*"], [["foo bar", -0.353, "**text**", 4653], ["foo bar", -0.353, "**text**", 4653], ["foo bar", -0.353, "**text**", 4653], "*"], [["foo bar", -0.353, "**text**", 4653], "*", "*", "*"]], "hsl(10%,20%,40%)")

    def test_solucionar_4(self):
        gameOfLife2.solucionar(["Foo bar", "Hello, world!", "Hello, world!", "Foo bar", "foo bar", "Hello, world!", "Hello, world!"], "rgb(20%,10%,30%)")

    def test_solucionar_5(self):
        gameOfLife2.solucionar([[["foo bar", -0.353, "**text**", 4653], [10, -45.9, 103.5, 0.955674], ["a", "b", "043", "foo bar"], "*"], ["*", "*", "*", [-1, 0.5, 1, 2, 3, 4, 5]], ["*", [-1, 0.5, 1, 2, 3, 4, 5], "*", [-1, 0.5, 1, 2, 3, 4, 5]], ["*", ["a", "b", "043", "foo bar"], [-1, 0.5, 1, 2, 3, 4, 5], ["foo bar", -0.353, "**text**", 4653]], [[-1, 0.5, 1, 2, 3, 4, 5], ["a", "b", "043", "foo bar"], ["a", "b", "043", "foo bar"], [-1, 0.5, 1, 2, 3, 4, 5]], [["foo bar", -0.353, "**text**", 4653], [-1, 0.5, 1, 2, 3, 4, 5], [10, -45.9, 103.5, 0.955674], "*"], ["*", [10, -45.9, 103.5, 0.955674], [10, -45.9, 103.5, 0.955674], "*"]], "rgb(0,100,200)")

    def test_solucionar_6(self):
        gameOfLife2.solucionar([], "")

