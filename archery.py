import math


N = int(raw_input("Enter N:"))
R_i = raw_input("Enter R's seperated by a space: ")
M = int(raw_input("Enter M: "))
coor_list = []
if M > 1:
	for i in range(M):
		coordinate = raw_input("Enter coordinates: ")
		coor_list.append(coordinate)
else:
	coordinate = raw_input("Enter coordinates: ")
	coor_list.append(coordinate)


#Split the radius' into a list of integers
R_list = [int(n) for n in R_i.split()]
#Split the coordinates into a list of lists
for i in range(len(coor_list)):
	temp_list = [int(n) for n in coor_list[i].split()]
	coor_list[i] = temp_list

count = 0

#function that will determine if a line and circle intersect
def do_they_intersect(radius,x1,y1,x2,y2):
	global count
	#figure out which of the two points is closer to the center
	first_point_distance = math.sqrt((x1)**2 + (y1)**2)
	second_point_distance = math.sqrt((x2)**2 + (y2)**2)
	print first_point_distance, second_point_distance, radius
	#find distance between the two points:
	between_distance = math.sqrt((x1- x2)**2 + (y1 - y2)**2)
	#Check if the inner point is within the circle, if the inner point is within the circle
	#check if outer point is outside of it
	#if inner point not in the cirlce, then they do not touch
	if first_point_distance < second_point_distance:
		if first_point_distance < radius and second_point_distance > radius:
			count += 1
	else:
		if second_point_distance > radius and first_point_distance < radius:
			count += 1
	print count

#Check each arrow with each circle
for i in range(len(R_list)):
	for n in range(len(coor_list)):
		do_they_intersect(R_list[i],coor_list[n][0],coor_list[n][1],coor_list[n][2],coor_list[n][3])

print count