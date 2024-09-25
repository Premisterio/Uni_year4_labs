# Catching errors when opening the file
try:

    f = open("tex.txt", "r")
    print(f.read())

# If error is raised when reading the file, raise an error
except Exception as e:
    print(f'{e}')
    exit()

