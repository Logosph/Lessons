import re

name = "Даниил"
surname = "Железин"

print(re.search(r"^\D{2}", name))
print(re.search(r"(ин|ын)\b", surname))
print(re.search(r"(А|З|Л|а|з|л)", name))
