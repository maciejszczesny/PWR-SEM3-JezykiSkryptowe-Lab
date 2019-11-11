import pickle
output_file = open("myfile.bin", "wb")
myint = 42
mystring = "Hello, world!"
pickle.dump(myint, output_file) #serializacja zapis inta jako bajty
pickle.dump(mystring, output_file)
output_file.close()

input_file = open("myfile.bin", "rb")
myint = pickle.load(input_file) #odczyt bajtów do inta
mystring = pickle.load(input_file)
print (myint)
print (mystring)
input_file.close()
