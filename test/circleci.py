"""
This script uses Helium to automatically start Chrome and navigate to localhost:1331, and it then selects the 'Try Me!!!!!!' button.
After which it checks to see if the string 'Welcome to my World!' exists.

If all goes well, it prints "Test passed!". Otherwise, it prints "Test failed :(".
"""

from helium.api import *
start_chrome("localhost:1313")
click("Try Me!!!!!")
if 'Welcome to my World!' in get_driver().page_source:
	print('Test passed!')
else:
	print('Test failed :(')
kill_browser()
