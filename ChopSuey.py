#ChopSuey, Copyright 2010 Peter Hajas
#
#A utility for crazy people with lots of monitors and no good solutions for chopping up wallpapers for them
#Requires the Python Image Library (http://www.pythonware.com/products/pil/) to do its awesomeness

import os, sys
import Image

class Monitor:
	def __init__(self,pixelWidth, pixelHeight, inchScreenWidth, inchScreenHeight, name):
		self.pW = pixelWidth
		self.pH = pixelHeight
		self.iW = inchScreenWidth
		self.iH = inchScreenHeight
		self.n = name
print "ChopSuey, not at all inspired by that one song."
print sys.argv[1]

#Create the image object and related variables
image = Image.open(sys.argv[1])
size = image.size #size is a 2-element array of the width and height

#Aha! Now we have to ask the user some stuff about what kind of monitors they have
print "We're going to ask you some questions about your monitors."
print "At any time, type 'done' and we'll move on!"
monitorList = []
while True:
	print "Do you have a monitor that you'd like to add? You've told ChopSuey about %d monitors." % len(monitorList)
	s = raw_input('> ')
	if s == 'done':
		print "Awesome! You told ChopSuey about %d monitor(s)." % len(monitorList)
		break
	if s == 'yes':
		#Create a new monitor object and add it to our list
		pixelWidth = raw_input('How many pixels wide is your display (e.g. 1920)? > ')
		pixelHeight = raw_input('How many pixels tall is your display (e.g. 1080)? > ')
		inchScreenWidth = raw_input('How many inches wide is the screen part of your display (e.g. 20)? > ')
		inchScreenHeight = raw_input('How many inches tall is the screen part of your display (e.g. 12)? > ')
		name = raw_input('Finally, what would you like to call this display (e.g. Samsung SyncMaster)? > ')
		newMonitor = Monitor(pixelWidth, pixelHeight, inchScreenWidth, inchScreenHeight, name)
		monitorList.append(newMonitor)

print "We're going to take a look now at the borders between monitors"