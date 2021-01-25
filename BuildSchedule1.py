myfile = open("BuildSchedule1.txt")

mylines = myfile.readlines()

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

def basicStructure(day):
	for myline in mylines:
		myline_list = myline.split(",")
		if myline_list[0] in day:
			day_info = myline_list[1:]
			print myline_list[0] + str(day_info)
			
def basicStructureArray(days):
	for day in days:
		basicStructure(day)

basicStructureArray(days)
