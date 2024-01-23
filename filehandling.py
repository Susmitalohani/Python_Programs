# -----------------------file handling:
# file:file is a collection of data and information store in a disk permanently
# two types of file:text file:store data in form of character
                #   :binary file:store data in form of bytes(image,pdf,video)
# method of storing data:file handling,database
# file handling:create,read,write,delete,append,update data which is inside file
# syntax:
# mode:purpose of opening file (default read linxa) 
# x in mode:creating file
# r:reading data inside file
# w:writing context into file
# a:append
# r+:read and write deutaoi garxa
# w+:deutaii garxa 
# ekchoti file banaesake pachi ani puraii location diramna pardaina file name matraii diye hunxa
# folder aru nai xa bahne chai puraii path dina parxa natra read gardaina but if same folder mai kam bhaeraxa bahne chai filenam ematraii lekhda hunxa
'''
open("filename",mode="",buffering,encode)
statement operation for file handling
close()
'''

#----------------------example:
# f=open("susmita.txt",mode="a")
# sabai line read garxa and print in form of list
# a=f.readlines()
# # first line matraii read garxa
# a=f.readline()
# f.write("We have reached file handling chapter\n")
# f.write("Myself susmita")
# f.write("Susmita")

# --variable
# f=open("susmita.txt","r",encoding="utf-8")
# print(f.name)
# print(f.mode)
# print(f.buffer)
# print(f.encoding)
# print(f.closed)

# -------method
# f=open("susmita.txt","r")
# a=f.readable()
# print(a)

# ------file close
# f=open("susmita.txt","w")
# f.write("Hi")
# f.close()
# print(f.closed)

# we can also use try catch inside file handling code
# try:
#     f=open("susmita.txt","r")
#     f.write("Hi")
# except:
#     print("W lekhnai paro")
# finally:
#     f.close()
#     # error ayepani finally le file close garxa so that tala ko code run hunu bhanda pahila file close hunxa 
# print("This is most imp code")

# ---------with statement
# with le chai close lekhna xutayeni close garxa affai 
# with open("susmita.txt","w")as f:
#     f.write("Nepal is landlocked country")
# print(f.closed)

# tell()
# seek()
