
og_numbers = []
with open('numbers.txt', 'r') as fin:
    for line in fin:
        og_numbers.append(int(line))
small_to_big = sorted(og_numbers)
big_to_small = list(reversed(small_to_big))

for num in big_to_small:
    i = 0
    j = 0
    print(num)
    print(small_to_big[j])
    print(small_to_big[i])
    
    while small_to_big[j] + num < 2020:
        while small_to_big[i] + num < 2020:
            print(i, j)
            print(small_to_big[j] + small_to_big[i] + num)
            if small_to_big[j] + small_to_big[i] + num < 2020:
                i+=1
            elif small_to_big[j] + small_to_big[i] + num == 2020:
                print(small_to_big[j])
                print(small_to_big[i])
                print(num)
                print(small_to_big[i] * small_to_big[j] * num)
                quit()
            else:
                break
        j+=1
        i=j
