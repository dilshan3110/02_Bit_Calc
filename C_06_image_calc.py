# Ask user for width and loop until they
# enter a number that is more than zero
def int_check(question, low ):
    error = "Please enter a number that is worth more than zero\n"
    while True:

        try:
            # ask tbe user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# calculates how many bits are needed to represent an integer
def image_calc():
    # Get the image dimensions
    width = int_check("Width: ", 1)
    height = int_check("Height:", 1)

    # calculate the number of pixels and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # Set up answer and return it
    answer = (f"Number of pixels: {width} x {height} = {num_pixels} "
             f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


# Main Routine goes here
image_ans = image_calc()
print(image_ans)
