input_file= open("Data.txt")
output_file= open("WriteData.txt",'w')

copy_data = input_file.readlines()
print("Actual Data ")
print(copy_data,"\n")


for i in range(0,len(copy_data)):
    if i % 2 == 0:
        output_file.write(copy_data[i])
    else:
        pass

# closing file after writing
output_file.close()

# opening write file in read mode and printing values
output_file= open("WriteData.txt","r")
print("Odd Lines are:")
print(output_file.read())


# closing file
input_file.close()
output_file.close()