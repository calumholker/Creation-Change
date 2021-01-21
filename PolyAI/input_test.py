import fileinput

inputs = [line.rstrip('\n') for line in (fileinput.input())]
print (inputs)