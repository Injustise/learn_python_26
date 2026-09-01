def generate_code_v1(code_len = 4):
    import random
    characters = list(range(10)) # 0-9
    characters += [chr(i) for i in range(65, 91)] # A-Z
    characters += [chr(i) for i in range(97, 123)] # a-z
    code = random.sample(characters, code_len)
    return ''.join(str(i) for i in code)

print(generate_code_v1())

def generate_code_v2(code_len = 4):
    import random
    import string
    characters = string.digits + string.ascii_letters # 0-9, a-z-A-Z
    return ''.join(random.sample(characters, code_len))

print(generate_code_v2(4))