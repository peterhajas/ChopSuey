# ChopSuey, Copyright 2010-2011 Peter Hajas - peterhajas (at) gmail (dot) com
#
# A utility for crazy people with lots of monitors and no good solutions for chopping up wallpapers for them
# Requires the Python Image Library (http://www.pythonware.com/products/pil/) to do its awesomeness
# See the LICENSE file for more copyright information
#
# If you're using this, I'd love to see a picture of your setup! Contact me!

import os, sys
import Image

class Monitor:
	def __init__(self, inchScreenWidth, inchScreenHeight, name):
		self.inchScreenWidth = inchScreenWidth
		self.inchScreenHeight = inchScreenHeight
		self.name = name
		
print "ChopSuey, not at all inspired by that one song."
# Check the number of arguments passed in
if len(sys.argv) != 2:
	print "Pass me an image, why'd you leave the keys up on the table?"
	print "You wanted to?"
	quit()

# Create the image object and related variables
image = Image.open(sys.argv[1])
size = image.size # size is a 2-element array of the width and height

# Aha! Now we have to ask the user some stuff about what kind of monitors they have
print "We're going to ask you some questions about your monitors."
print "At any time, type 'done' and we'll move on!"
print ""
print "Please tell ChopSuey about your monitors from left to right"
print ""
monitorList = []
while True:
	print "Do you have a monitor that you'd like to add? You've told ChopSuey about %d monitor(s)." % len(monitorList)
	s = raw_input('> ')
	if s == 'done':
		print "Awesome! You told ChopSuey about %d monitor(s)." % len(monitorList)
		break
	if s == 'yes':
		# Create a new monitor object and add it to our list
		inchScreenWidth = raw_input('How many inches wide is the screen part of your display (e.g. 20)? > ')
		inchScreenHeight = raw_input('How many inches tall is the screen part of your display (e.g. 12)? > ')
		name = raw_input('Finally, what would you like to call this display (e.g. Samsung SyncMaster)? > ')
		newMonitor = Monitor(inchScreenWidth, inchScreenHeight, name)
		if len(monitorList) > 1:
			newMonitor.leftBorder = raw_input('How thick is the border (in inches) between this screen and the one to the left of it (e.g. 1)? > ')
			newMonitor.topOffsetFromLeft = raw_input('How far off (in inches) is the top of this screen relative to the top of the one to the left of it (e.g. .5)? > ')
		monitorList.append(newMonitor)

print "We're going to take a look now at the borders between your monitors"
n = 0
for i in monitorList:
	if n!= 0:
		# Ask about the border between this display and the one to its left
		i.leftBorder = raw_input('How thick is the border (in inches) between this screen and the one to the left of it (e.g. 1)? > ')
		# Ask about the offset between the current monitor's top and the one to the left of it
		topOffsetFromLeftTop = raw_input('How much higher (in inches) is the top of this screen relative to the top of the one to the left of it (e.g. .5) Lower means negative? > ')# Also ask about the offset between the top of this display and the top of the display to its left
		
	n = n + 1

quit()
	
	
