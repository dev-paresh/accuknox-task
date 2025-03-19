# Here what i have implement:
# -----------------------------------------------------------------------------

# I created a Rectangle class because I needed an object that holds length and width while also being iterable.
# I defined the __iter__ method because this makes the class iterable, allowing us to loop over an instance of Rectangle.
# I used a generator function inside __iter__ because it allows me to yield values one at a time, first returning the length in {'length': <VALUE>} format and then the width in {'width': <VALUE>} format.
# I tested iteration using both a for loop and a list comprehension because I wanted to confirm that the object correctly yields values in the expected format.
    

from rectangle import Rectangle

rect = Rectangle(10, 5)

print("Iterating over Rectangle:")
for item in rect:
    print(item)

all_values = [item for item in rect]
print("\nAll values:", all_values)




# sample out put
# ----------------------------------------------------

# Iterating over Rectangle:
# {'length': 10}
# {'width': 5}

# All values: [{'length': 10}, {'width': 5}]