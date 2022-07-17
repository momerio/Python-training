import random
answer = random.randint(1, 10)
while True:
    inputText = int(input("input>>"))
    if inputText < answer:
        print("output: low")
    elif inputText > answer:
        print("output: high")
    else:
        print("output: just!")
        break
