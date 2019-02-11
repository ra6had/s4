# Read asc file
# Ignore/remove first 4 lines
# Capture the remainder of the file in columns
# The first and second columns will be the longest
# Split the first and second columns based on the length of the third
# Assign the data_elements_list of the 3rd & 4th columns to the beacon no. as tuples
# Split the parcels column and creat a dictinoary from each parcel string


import xlrd
from tkinter.filedialog import askopenfilename




data_elements_list = []							# This will be a list of elements within a list of lines
filename = askopenfilename()					# GUI select a file and store its path to filename

f = open(filename, 'r')								# Open file as read only
data = f.read()										# Stores the file as a string
data_line_list = data.split("\n") 					# Splits the string to a list, each line is an element




# Split each lines in the data_line_list to a list of elements 
for i in range(len(data_line_list)):
	line = data_line_list[i]						# Read the ith line of the data_line_list
	line_elements_list = line.split()				# Create a list by spliting the ith line
	data_elements_list.append(line_elements_list)	# Append the line_elements_list into the data_elements_list list
		



# Store the header lines in a list and deleted  them from data_element_list
# Delete data_line_list  after using it to populate data_elements_list
header = [data_elements_list[0],data_elements_list[1], data_elements_list[2], data_elements_list[3]]
del data_elements_list[0:4]
del data_line_list




# Capture beacons and their attributes in appropriate lists
beacons = []		# This will be a list of beacon numbers
easting = []		# This will be a list of easting values 
northing = []		# This will be a list of northing values
parcel_data = []	# This will be a list of parcel string lines



for i in range(len(data_elements_list)):
	if len(data_elements_list[i]) == 7:							# This identifies beacon lines
			beacons.append(data_elements_list[i][1])			# Store beacon no.
			easting.append(float(data_elements_list[i][2]))		# Store beacon easting
			northing.append(float(data_elements_list[i][3]))	# Store beacon northing
	elif len(data_elements_list[i]) == 2:						# This identifies parcel_data lines
		parcel_data.append(data_elements_list[i])				# This appends parcel_data lines to parcel_data list


coordinates = dict(zip(beacons,zip(easting, northing)))  # Create a dictionary with beacon as the key


# for line in parcel_data:
	# print(line)
# print('\n')

# This means for sublist in parcel_data, for value in sublist, append value to parcel_list
parcels_list = [val for sublist in parcel_data for val in sublist]


# Remove '-' from parcels_list
for elem in parcels_list:
	if elem == '-':
		parcels_list.remove(elem)

	




# parcel_case = {}
# wb = xlrd.open_workbook(xls)
# sh = wb.sheet_by_index(0)   
# for i in range(379):
    # parcel_no = sh.cell(i,0).value
    # case_no = sh.cell(i,1).value
    # parcel_case[parcel_no] = case_no

# parcel_string = []
# wb2 = xlrd.open_workbook('parcelstring.xlsx')
# sh2 = wb2.sheet_by_index(0)

# for i in range(2651):
    # parcels = sh2.cell(i,0).value
    # parcel_string.append(parcels)

# final_list = [parcel_case.get(item, item) for item in parcel_string]

parcel_case = {}				# Initiate an empty dictionary
xls = askopenfilename()			# GUI get a file and store its path to xls
wb = xlrd.open_workbook(xls)	# store the workbook to wb
sh = wb.sheet_by_index(0)		# store the sheet to sh
rows = sh.nrows()				# Get the number of rows

for i in range(rows):
	parcel_no = sh.cell(i,0).value
	case_no = sh.cell(i,1).value
	parcel_case[parcel_no] = case_no

case_string = [parcel_case.get(item, item) for item in parcel_data] 

print(case_string)
 












