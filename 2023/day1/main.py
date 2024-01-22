
file = open("./input", "r")

number_dict = {'one':'o1e','two':'t2o','three':'t3e','four':'f4r','five':'f5e','six':'s6x',
               'seven':'s7n','eight':'e8t','nine':'n9e'}

def main():
    sum = 0
    digits = []
    lines = file.readlines()
    
    for line in lines:
        for key in number_dict.keys():
            if line.startswith(key):
                line = line.replace(key, number_dict[key])
            line = line.replace(key, number_dict[key])
        for char in line:
            if char.isdigit():
                digits.append(char)
        two_num = str(digits[0]) + str(digits[-1])
        digits.clear()
        sum += int(two_num)
    print(sum)

main()
