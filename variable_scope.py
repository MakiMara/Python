def test():      #ako je varijabla unutar f-je def. sa keyword global
    global x     #ona ce biti globalna iako je napisana unutar specificne funkcije
    x=20         #ako nije definisana sa keyword global a unutar f-je je - local scope
    print(x)

def test2():
    print(x)

test()
test2()


def parent():
    x=20
    print(x)
    def child():
        y=30
        print(y)
        def grand_child():
            z=40
            print(z)
        grand_child()
    child()
parent()