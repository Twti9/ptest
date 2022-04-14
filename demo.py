#开发时间：2022/4/12 21:32
import random,string
def gen_random(length):
    num_of_numeric = random.randint(1,length-1)
    num_of_letter = length-num_of_numeric
    numeric = [random.choice(string.digits) for i in range(num_of_numeric)]
    letter  = [random.choice(string.ascii_letters) for i in range(num_of_letter)]
    all_digits= numeric+letter
    random.shuffle(all_digits)
    result = ''.join([i for i in all_digits])
    return result
if __name__ == '__main__':
    print(gen_random(5))