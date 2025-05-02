with open("input.txt", "w") as f:
    f.write("This is a test of the text file. An example of the task.")
with open("input.txt", "r") as f:
    data = f.read()
words = data.split()
new_words = [word for word in words if word.lower() not in ['a', 'an', 'the']]
with open("output.txt", "w") as f:
    f.write(" ".join(new_words))