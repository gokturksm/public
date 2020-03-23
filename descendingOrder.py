def descending_order(num):
    numbers = []
    for i in str(num):
        numbers.append(int(i))
    for i, val in enumerate(numbers):
        for _ in range(i, len(numbers)):
            if numbers[i] > numbers[_]:
                pass
            else:
                temp = numbers[i]
                numbers[i] = numbers[_]
                numbers[_] = temp
    final = ''.join(str(e) for e in numbers) 
    return int(final)
