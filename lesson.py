import re

s = 'sadjfhldks+dasd     ----- 327149041?><~]0 FHDIJADKdddfghjkddd'
result = re.search(r"d..h", s)
print(result)

