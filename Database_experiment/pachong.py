import csv
import random
import string

VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))

def generate_word(length):
    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    return word

def make_csv():
    with open("csv.csv",'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'name', 'age', 'grade', 'phone'])
        for i in range(1000000):
            Id = i
            name = generate_word(10)
            age = random.randint(6,12)
            grade = random.randint(1,6)
            phone = random.choice(['139', '188', '185', '136', '158', '151']) + "".join(random.choice("0123456789") for i in range(8))

            writer.writerow([Id,name,age,grade,phone])

if __name__ == '__main__':
    make_csv()