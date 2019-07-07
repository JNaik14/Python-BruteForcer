# Characters In Password

char = ('qwertyuiopasdfghjklzxcvbnm')

# I will define a function for each length of password

def two(password):
    for one in char:
        for two in char:
            yield f"{one}{two}"

def three(password):
    for one in char:
        for two in char:
            for three in char:
                yield f"{one}{two}{three}"

def four(password):
    for one in char:
        for two in char:
            for three in char:
                for four in char:
                    yield f"{one}{two}{three}{four}"


# You can add more functions like this for more bigger length of passsword

input_pass = input("Pls Enter the Password : ")

if len(input_pass) == 2:
    for pa in two(input_pass):
        print(pa)
        if pa == input_pass:
            break
if len(input_pass) == 3:
    for pa in three(input_pass):
        print(pa)
        if pa == input_pass:
            break
if len(input_pass) == 4:
    for pa in four(input_pass):
        print(pa)
        if pa == input_pass:
            break
