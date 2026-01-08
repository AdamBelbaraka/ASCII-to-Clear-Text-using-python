def ascii_to_text(ascii_text):
    chars = ascii_text.split()
    return ''.join(chr(int(c)) for c in chars)
    
ascii_input = input("ASCII text : ")
clear_text = ascii_to_text(ascii_input)
print("Clear text :", clear_text)
