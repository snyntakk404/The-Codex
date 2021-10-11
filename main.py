import os

codex = {
  "what is the codex": "The codex is a project to store large amounts of info on any task",
  "how do i add to the codex": "look in codex.txt"
  }

while True:
  search = input("search the codex: ")
  os.system("clear")

try:
  print(codex[search.lower()])
  input("press enter when done reading: ")
  os.system("clear")
except:
  print("nothing in the codex matched this search")
  input("press enter: ")
  os.system("clear")