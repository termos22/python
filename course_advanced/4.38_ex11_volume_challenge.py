length = int(input("Please input rectangular prism length: "))
width = int(input("Please input rectangular prism width: "))
height = int(input("Please input rectangular prism height: "))

def rectangular_prism_volume(len, wid, hei):
    return len * wid * hei


print("The volume of the rectangular prism is", rectangular_prism_volume(length, width, height), "cubic feet.")
print("The volume of the rectangular prism is " + str(rectangular_prism_volume(length, width, height)) + " cubic feet.")

