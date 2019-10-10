import os
from PIL import Image


def emoji_converter():
    user_input = input("(1) for Single file (2) for Entire folder: ")

    if user_input == "1":
        second_input = input("Is the file jpg or png? ")
        if second_input == "png":
            image_url = input("Enter filename (case sensitive and must be in the dictionary folder): ")
            path_url = image_url + ".png"
            img = Image.open(path_url)
            emoji_size = img.resize((32,32))
            new_image_name = image_url + "emoji-fied.png"
            emoji_size.save(new_image_name)

        elif second_input == "jpg":
            image_url = input("Enter filename (case sensitive and must be in the dictionary folder): ")
            path_url = image_url + ".jpg"
            img = Image.open(path_url)
            emoji_size = img.resize((32, 32))
            new_image_name = image_url + "emoji-fied.jpg"
            emoji_size.save(new_image_name)

        else:
            print("Invalid file type")
    elif user_input == "2":

        os.makedirs('Emoji-fied', exist_ok=True)
        for filename in os.listdir('.'):
            if not (filename.endswith('.png') or filename.endswith('.jpg')):
                continue
            image = Image.open(filename)
            width, height = image.size

            if width > 32 and height > 32:
                if width > height:
                    height = ((32/width) * height)
                    width = 32
                else:
                    width = ((32/height) * width)
                    height = 32

                print('Resizing %s to 32x32' % filename)
                image = image.resize((32, 32))
            image.save(os.path.join('Emoji-fied', filename))


emoji_converter()
