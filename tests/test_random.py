import random
import secrets

# getting systemRandom instance out of random class
system_random = random.SystemRandom()

# Secure random number
print(system_random.randint(1, 3000000000000000000000000000000000000000000000000000000000000000000000000))
# Output 22


# Secure random number within a range
#print(system_random.randrange(50, 100))
# Output 59

# secure random choice
#list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(system_random.choice(list1))
# Output 9

# secure random sample
#print(system_random.sample(list1, 3))
# Output [1, 4, 9]

# secure random float
#print(system_random.uniform(5.5, 25.5))
# Output 18.666415244982193

print(secrets.randbits(4))