"""
This script uses Helium to automatically perform a Google search for the term
"Helium", and opens the Wikipedia article on the subject. If all goes well, it
prints "Test passed!". Otherwise, it prints "Test failed :(".
"""
from helium.api import *
start_chrome("localhost:1313")
click("Try Me!!!!!")
if 'Welcome to my World!' in get_driver().page_source:
	print('Test passed!')
else:
	print('Test failed :(')
kill_browser()
