def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    data = [line[:-1] for line in lines]
    people = []
    for line in data:
        tmp = line.split(" = ")
        people.append(tmp)
    print(people)
    
a = int(str(people[1][1])[0:32])+int(str(people[2][1])[0:32])
print(a)
while not isPrime(a):
    a += 1

print(a)