# 1.
# Accept from the user some text.Ensure user enters something else raise an
# exception.
# After that# write#that# text# to# a file and then read
# from this file to write# to another file simultaneously
# 2.
# Reading an image to writing to another file simultaneously

import os

from PIL import Image

class user_input:

    def __init__(self, user_name): #Initialising the attributes
        self.user_name = user_name

    def homework_input(self):
        while True:
            try:
                stored_user = str(input(("Please enter the text\n")))
                #If statement to say if the character length is less than 0
                if (len(stored_user)) == 0:
                    raise Exception
            except Exception:
                print("We do not accept empty texts")
            else:
        # Opening the homework.txt file just created. using w+ to read and write.
                with open("testhomework.txt", "w+") as file:
                # Writing the user input into the file
                    file.write(stored_user)
                    self.new_text = str(file.read()) #This stores a new self
                    print("Thank you for entering your name: ", stored_user)
                    with open("testhomework2.txt", "w+") as file2:
                        file2.write(stored_user)
                        self.new_text = str(file.read())
                        return self.user_name

    def image_writefile(self):
        with open('lol.jpg', 'rb') as f, open('global.png', 'wb') as f2:
            f2.write(f.read())
            image.open('lol.jpg').show()


enteruser = user_input("n")
# enteruser.homework_input()
enteruser.image_writefile()

# def write_user_input(self):
#     self.user_input()
#     with open("user_name.txt", "w+") as file:  # w+ write and read mode (OVERRIDES value)
#         file.write(self.name)  # What is dynamically type, strongly type
#         file.seek(0)
#         self.new_text = str(file.read())
# # repeats previous method but writes on another file
# def again(self):
#     self.write_user_input()
#     with open("user_name_two.txt", "w+") as file:
#         file.write(self.new_text)

