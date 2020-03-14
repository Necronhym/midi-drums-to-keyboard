import pyautogui
import os
dev = os.open('../../../../../../dev/midi4', os.O_RDWR)
while True:
	s = os.read(dev, 32)
	#Nothing is in use
	if( 'xf8' in str(s) ):
		continue
	#Kicks:
	if( 'x99$' in  str(s) ):
		pyautogui.press('1')
	if( 'x99,' in  str(s) ):
		pyautogui.press('2')
	#Snare
	if( 'x99&' in  str(s) ):
		pyautogui.press('3')
	#Brass:
	if( 'x993' in  str(s) ):
		pyautogui.press('4')
	if( 'xb9' in  str(s) ):
		pyautogui.press('5')
	#Toms:
	if( 'x990' in  str(s) ):
		pyautogui.press('6')
	if( 'x99-' in  str(s) ):
		pyautogui.press('7')
	if( 'x99+' in  str(s) ):
		pyautogui.press('8')
