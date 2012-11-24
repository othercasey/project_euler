fish = 3879284

fish_net = []

def hook(number):
    x = 2
    while number >= x:
        if number % x == 0:
            fish_net.append(x)
            number = number / x
        x = x + 1

hook(fish)
print "Here's the mama fish: " + str(fish)
print "Look at these prime baby fish I caught in my net!" + str(fish_net)
print "I like this one best, though: " + str(fish_net[-1])