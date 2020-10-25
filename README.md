# SimpleImageGridJoiner
Joins a square grid of images together into a larger image.  

Image file naming format should be:
*MyImageName0.extension
*MyImageName1.extension
*MyImageName2.extension
*etc  

Important! you must have a square number of images, 4,9,16,25,etc  

This program takes in two arguments, the file name without the number or extension, so MyImageName0.extension should be fed as an argument as just MyImageName and the program will append 0.png, 1.png etc as it loads and loops through the files.  The second argument is the number of images, again this should be a perfect square number!

example usage: python sgj.py MyImageName 9

An output file will be generated with the name MyImageNameJOINED.png
