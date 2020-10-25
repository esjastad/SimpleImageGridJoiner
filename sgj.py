#Copyright (C) 2020 Erik Jastad - All Rights Reserved

import cv2
import numpy as np
import sys

def joiner(source,size):
	ifile = source + '0' + '.png'     #filename
	img = cv2.imread(ifile, 1)		  #load first image
	height = img.shape[0]			  #get image height/width
	width = img.shape[1]			
	val = int(np.sqrt(int(size)))	  #Get square value of user defined size (#of images) to use in x,y loop
	target = np.zeros((height * val,width * val,3), np.uint8)	#Make the blank canvas
	iter = 0						  #Current Image

	#Loop through images in a square fashion
	for y in range (val):
		for x in range (val):
			#Load up image to copy
			ifile = source + str(iter) + '.png'
			img = cv2.imread(ifile, 1)
			#Copy loaded image to canvas with appropriate offsets
			target[y*height:y*height+height,x*width:x*width+width] = img
			#Increment to next image
			iter=iter+1

	#Write the result
	cv2.imwrite(source + 'JOINED.png', target)
	

if __name__ == "__main__":
	print('==================================================')
	print('Image Joiner by Erik Jastad')
	print('==================================================')

	#Check if arguments were provided
	if len(sys.argv) < 2:
		print('Missing source group name and/or grid size arguments')
		sys.exit()
	
	#grab the arguments passed
	path_file_image_source = sys.argv[1]
	grid_size = sys.argv[2]
	
	#Start the image joining
	joiner(path_file_image_source,grid_size)
	
	print("Image Joining Complete")