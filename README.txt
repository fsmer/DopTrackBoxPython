READ ME

Modes:
Loop all satellites
	This mode has as output a plot and text file that shows all satellites 
	on the time that the run button is pressed. 

Loop x satellites
	This mode has as output a groundtrack plot and a text file with the 
	selected satellites from the satellites tab on the chosen time relative 
	to the time that the run button is pressed.

Make YML files
	This  mode has as output .yml files for the selected satellites for the 
	chosen time relative to the time that the run button is pressed. The files 
	are set in a seperate folder (YML), this folder is emptied every time the 
	Make YML files is executed. 

Live
	This mode has as output a plot that is continuously updated until the figure 
	is closed. The red dot is the satellite selected from the satellite tab.

Possible errors:
Run does not work
	One of the added TLE is not right, solution: delete all  custom TLE's 
The custom satellite is not added, solution: restart program
The new location is not added, solution: restart program