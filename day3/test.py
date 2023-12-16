import re
#print(re.search(r"@*#*\$*%*&*\**", "...#"))
print(re.findall("@|#|\$|%|&|\*|\+", "...+@#\$,%,&,\*,\+"))
print(re.findall("[^.]|^\d", "...+@#$%&*+"))