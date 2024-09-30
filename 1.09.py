Qual = {
    "A": 10,
    "B": 8,
    "C": 6,
    "D": 4,
    "E": 2,
}
note = input("Enter a note: A/B/C/D/E\n")
print(Qual[note] if note in Qual else "Note not found")
