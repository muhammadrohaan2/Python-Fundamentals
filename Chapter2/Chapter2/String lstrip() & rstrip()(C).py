text = " Engineering".lstrip()
print(text)

text = "Engineering ".rstrip()
print(text)

text = " Engineering ".strip()
print(text)

text = "Data Engineering".strip()
print(text)

text = "###ABC###".strip("#")
print(text)

text = "  Engineering"
print(len(text))
print(len(text.strip()))

print (len(text) - len(text.strip()))
print (len(text) == len(text.strip()))


text = "Engineering"
nr_of_spaces = len(text) - len(text.strip())
is_clean = len(text) ==len(text.strip())
print ("Nr of spaces:", nr_of_spaces)
print ("Is my data clean?:", is_clean)