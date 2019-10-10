import os
from PIL import Image


# Uses pillow to manipulate images

def emoji_converter():
    # User input for different choices of this simple program
    user_input = input("(1) for Single file (2) for Entire folder: ")

    # Input 1 allows user to edit a specific file
    if user_input == "1":
        second_input = input("Is the file jpg or png? ")                    # User defines file type
        if second_input == "png":
            image_url = input("Enter filename (Must be in the folder): ")   # Input file
            path_url = image_url + ".png"                                   # Renames the file/ adds file type to name
            img = Image.open(path_url)                                      # Pillow loads the image file
            emoji_size = img.resize((32, 32))                               # Resize the image to fit the criteria
            new_image_name = image_url + "-emoji-fied.png"                  # Rename the file to avoid overwriting
            emoji_size.save(new_image_name)                                 # Image saved in folder

        elif second_input == "jpg":
            image_url = input("Enter filename (Must be in the folder): ")
            path_url = image_url + ".jpg"
            img = Image.open(path_url)
            emoji_size = img.resize((32, 32))
            new_image_name = image_url + "-emoji-fied.jpg"
            emoji_size.save(new_image_name)

        else:
            print("Invalid file type")                                      # Stops program if input is invalid

    # Input 2 automatically "emoji-fies" the whole folder
    elif user_input == "2":

        os.makedirs('Emoji-fied', exist_ok=True)                            # Creates a new folder called Emoji-fied
        for filename in os.listdir('.'):                                    # Checks each file in the folder
            if not (filename.endswith('.png') or filename.endswith('.jpg')):    # If file isnt not either jpg or png,
                continue                                                        # it continues to the next file
            image = Image.open(filename)                                    # Loads image
            width, height = image.size

            if width > 32 and height > 32:                                  # Checks if the size of image is > 32
                if width > height:
                    height = ((32 / width) * height)                        # Attempt to even out the image sizes
                    width = 32
                else:
                    width = ((32 / height) * width)
                    height = 32

                print('Resizing %s to 32x32' % filename)
                image = image.resize((32, 32))
            image.save(os.path.join('Emoji-fied', filename))               # Saves image and puts it into the new folder
    else:
        print("Invalid input!")                                                 # Stops program if input is invalid


emoji_converter()
