def create_file(name):
    file_name = 'my_name.txt'  # Name of the file to be created
    with open(file_name, 'w') as file:
        file.write(name)
#Assigning name
my_name = "Arjun Vadakkekarayil Sojan"
write_name_file(my_name)
