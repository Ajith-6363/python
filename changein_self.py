class change:
    def __init__(ajith,age):
        ajith._age=age
    def greet(ajith):
        print(f"Hello {ajith._age}")
a=change(25)
a.greet()
 