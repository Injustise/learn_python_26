score = int(input("请输入您的成绩（0~100）："))
if score == 100:
    assess = 'Perfect！'
elif 90 <= score < 100:
    assess = 'A'
elif 80 <= score < 90:
    assess = 'B'
elif 70 <= score < 80:
    assess = 'C'
elif 60 <= score < 70:
    assess = 'D'
else:
    assess = 'E'
print(assess + '\n')

status_code = int(input("请输入状态码："))
match(status_code):
    case 400 | 405: 
        description = 'Invalid Request'
    case 401 | 403 | 404: 
        description = 'Not Allowed'
    case 418: 
        description = 'I am a teapot'
    case 429: 
        description = 'Too many requests'
    case _: 
        description = 'Unknown Status Code'
print(description)