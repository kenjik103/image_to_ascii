from PIL import Image
import sys

def get_image_array(filepath, new_width = 100):
    """read and return image as a list"""
    image = Image.open(filepath, "r")
    width,height = image.size
    if width > new_width:
        ratio = height/width
        new_height = int(new_width * ratio)
        image = image.resize((new_width,new_height))
    else:
        new_height = height
        new_width = width
    image = image.convert("RGB")
    pixel_colors = []
    for y in range(new_height):
        row = []
        for x in range(new_width):
            r,g,b = image.getpixel((x,y))
            row.append((r,g,b))
        pixel_colors.append(row)
    return pixel_colors


def get_brightness(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (red + green + blue) / 3

def convert_to_ascii(image):
    """given array of pixel values, convert to corresponding ascii values"""
    output_str = ""
    ramp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    for y in range(len(image)):
        for x in range(len(image[0])):
            brightness = get_brightness(image[y][x])
            ascii_val = ramp[int((255 - brightness)/3.75)]
            output_str += ascii_val
        output_str += '\n'
    return output_str

def main():
    input = sys.argv[1:]
    try:
        if len(input) > 1:
            image = get_image_array(input[0], int(input[1]))
        else:
            image = get_image_array(input[0])
        string = convert_to_ascii(image)
        print(string)
    except:
        print("invalid input")

main()
