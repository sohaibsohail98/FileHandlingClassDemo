class Text_File_Handling:

    def __init__(self, file_path, text_storage=None):
        self.file_path = file_path
        self.text_storage = text_storage

    #Going to read in two ways and write in two ways

    def readTextFile(self):
        #open file
        #read the file
        #close the file

        file = open(self.file_path, 'r')
        #self.text_storage = file.read()
        #self.text_storage = file.read(3) #It reads 3 characters in the text file
        self.text_storage = file.readline()
        self.text_storage = file.readline()
        self.text_storage = file.readlines()
        print(file.tell()) #The pointer is at the current position and will start reading from there
        file.seek(0,2) #Telling the pointer to go back at that particular position mentioned.
        for line in file:
            print(line)
        file.close()
        return self.text_storage

    def writeTextFile(self):
        file = open("writer.txt", "w") #two arguments- one is file and the other is mode
        file.write("My first python created file")
        file.close()
        file = open("writer.txt", "a+") #a+ means the append and read mode
        file.write("\n I am overiding the file")
        file.seek(0)
        self.text_storage = file.read() #storing what I read from the file to the instance variable
        file.close()
        print(file.closed) #gives me the status of closure
        print(file.name)
        print(file.mode)
        return self.text_storage


    def readTextFileUsingWith(self):
        #reduce the overhead of closing files
        #open the file and just read it. No overheaf of closing
        #Automatically closes the file and also closes it during the times of excepion being
        with open("order.txt", "r") as file:
            self.text_storage = file.read()
            return self.text_storage

    def writeTextFileUsingWith(self):
        with open("writer.txt", "w+") as file: #w+ means write and read mode
            file.write("Using writer with functionality")
            print(file.tell()) #tells you the current position of your pointer
            file.seek(0) #repositioning the pointer to the beginning of the file
            self.text_storage = file.read()
            return self.text_storage

    def playingWithPythonOSModule(self):
        import os
        print(os.getcwd()) #current workload directory
        # os.remove("writer.txt") #this removes a particular file in the directory
        # print(os.listdir()) #Listing the files within the directory
        # os.rmdir() #This will remove the directory
        os.rename("order.txt", "modified.txt")
        os.chdir("/Users/sohaibsohail/Documents") #-This will change the directory
        os.mkdir("Sohaib") #Making a new directory
        os.rmdir("Sohaib") #Removing the directory

    def playingWithException(self):
        try:
            file = open(self.file_path, "r")
            a = 10
            b = 0
            c = a / b
        except Exception as e:  #This is about the error message
            print(e)
            print("File is not present")

        except FileNotFoundError as e: #never write this as generalised
        else: #If there is no errors
            self.text_storage = file.readline()
            file.close()

        finally: #Prints
            print("Will run for sure!!")
            return self.text_storage

    def raiseException(self):
        try:
            firstValue=int(input("Enter your name"))

            if(len(firstValue))== 0:
                raise Exception #Throwing an exception which python might not have, #Raise will let the user know what the error is

        except Exception:
            print("We do not accept empty names")

        else:
            print("Thank you for entering your name: ", firstValue)



class Homework:
    def __init__(self, file_path, text_storage=None):
        self.file_path = file_path
        self.text_storage = text_storage
    # Creating the class
    def raise_exception_task(self):
        # Start of our Errors and Exceptions code
        #while True:
            try:
                # Asking a input from the user
                first_value = str(input("Enter your name: "))
                # Creating a file called homework to write in
                file = open("homework.txt", "w")
                # Writing the user input into the file
                file.write(first_value)
                # Opening the homework.txt file just created. using w+ to read and write.
                with open("homework.txt", "w+") as file:
                    self.text_storage = file.read()
                    file = open("homework2.txt", "w")
                    file.write(self.text_storage)
                if len(first_value) == 0:
                    raise Exception
            except Exception:
                print("We do not accept empty names!!")
            else:
                print("Thank you for entering your name")
