class Counter:
    object_count = 0

    def __init__(self):
        Counter.object_count += 1

    @classmethod
    def display_count(cls):
        print("Total objects created: ", cls.object_count)
    

obj1 = Counter()
obj2 = Counter()

Counter.display_count()