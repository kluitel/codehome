#! /usr/bin/python
while True:
    s = raw_input("Enter a string of at least 4 characters: ")
    if s == 'q':
        break
    if len(s) < 4:
        print ("value is too small")
        continue
    print("The string was of sufficient length")
    raise SystemExit # try this from the OS