import re
def LInput(text,reg):
    val = input(text)
    if (not re.search(reg,val)) == False:
        print(not(re.search(reg,val)))
        print('非法输入，请重新输入')
        LInput(text,reg)
    else:
        return val
LInput('input:',r'^[a-z]{1,2}$')