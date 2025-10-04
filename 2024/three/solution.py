import re
def get_commands(corrupted_text):
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    match = re.findall(pattern, corrupted_text)
    print(match)
    return match
def calculate(text):
    result=0
    previous="do()"
    for i in text:
        if i == "don't()" or i=="do()":
            previous=i
            continue
        if previous == "don't()":
            continue
        nums=re.findall(r'\d{1,3}',i)
        num1=int(nums[0])
        num2=int(nums[1])
        result+=num1*num2
    return result

with open('input.txt', 'r') as f:
    corrupted_text = f.read()

print(calculate(get_commands(corrupted_text)))