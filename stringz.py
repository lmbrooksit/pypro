from traceback import print_tb

from matplotlib.style.core import library
from datetime import datetime
person = "Jose"
print("my name is {}".format(person))

print(f"my name is {person}")

d = {"a":123, "b":456}

print(f"my number is {d['b']}")

mylist = [0,1,2]

print(f"my number is {mylist[1]}")

library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting on water', 602), ('Teyman', 'Physics', 95), ('Hamlit', 'Mythology', 144)]

print(library)

for book in library:
    print(f"Author of book is {book[0]}")

for author, topic, pages in library:
    print(f"{author:{10}} {topic:{30}} {pages:.>{10}}")

today = datetime(year=2019,month=3,day=1)

print(f'{today:%B %d, %Y}')