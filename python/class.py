class Circle:
    def __init__(self, w, c, t, s):
        """weight（重さ）はグラム"""
        self.weight = w
        self.color = c
        self.toudo = t
        self.smell = s
        print("Created!")

    
apple = Apple(200, "red", 15, 10)
print(apple.weight)
print(apple.color)
print(apple.toudo)
print(apple.smell)
