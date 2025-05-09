def make_sentence(word, pos):
    if pos == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")

    elif pos == 1:
        print(f"It's so nice outside today it makes me want to {word}!")

    elif pos == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Part of speech must be 0, 1, or 2! Can't make a sentence")

word : str = input("Please type a noun, verb, or adjective: ")
print()
print("Is this a noun, verb, or adjective?")
pos : int = int(input("Type 0 for noun, 1 for verb, 2 for adjective:"))

make_sentence(word, pos)