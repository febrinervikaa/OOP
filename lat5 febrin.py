class py_solution:
    def reverse_word(self, s):
        return ' '.join(reversed(s.split()))
    
x=input(55)
print(py_solution().reverse_words(x))