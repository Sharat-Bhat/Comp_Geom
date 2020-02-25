import math
import operator
import matplotlib.pyplot as plt
import random

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def right_turn(p1, p2, p3):
	angle1 = math.atan2(p2.y-p1.y, p2.x-p1.x)
	angle2 = math.atan2(p3.y-p2.y, p3.x-p2.x)
	angle = angle1-angle2
	if angle > math.pi:
		angle -= 2*math.pi
	elif angle < -math.pi:
		angle += 2*math.pi
	if angle > 0:
		return True
	else:
		return False

def convex_hull(points):
	if(len(points) <= 3):
		# points.append(points[0])
		return points
	hull = []
	# print("\nk fjtbfbty")
	points.sort(key = operator.attrgetter('x'))
	hull.append(points[0])
	i = -1
	while not (len(hull)>1 and hull[len(hull) -1] == hull[0]):
		# print("{} {}".format(hull[len(hull)-1].x, hull[len(hull)-1].y))
			# print("	{} {}".format(points[i].x, points[i].y))
		hull.append(points[i])
		p2_present = True
		right = False
		for k in range(len(points)):	
			if points[k] != hull[len(hull) -2] and points[k] != hull[len(hull) -1]:
				right = right_turn(hull[len(hull) -2], hull[len(hull) -1], points[k])
				# print("		{} {}  {}".format(points[k].x, points[k].y, right))
				if right:
					p2_present = False
					break
		if p2_present == False:
			hull.pop()
		i = (i+1)%len(points)
	hull.pop()
	return hull



if __name__ == "__main__":
	points = []
	X = []
	Y = []

	## INPUT FROM FILE
	# infile = open("convex_hull_slow_input.txt", "r")
	# n = int(infile.readline())
	# for x in infile:
	# 	x = x.split()
	# 	print(x)
	# 	if len(x) == 2:
	# 		point = Point(float(x[0]), float(x[1]))
	# 		print("{} {}".format(point.x, point.y))
	# 		X.append(point.x)
	# 		Y.append(point.y)
	# 		points.append(point)
	
	## RANDOMLY GENERATED INPUT
	n = random.randrange(3, 100)
	# n = 4
	for i in range(n):
		x = random.uniform(-1000, 1000)
		y = random.uniform(-1000, 1000)
		point = Point(x,y)
		points.append(point)
		X.append(point.x)
		Y.append(point.y)
	# print("\nPoints:")
	# for obj in points:
		# print(obj.x, obj.y, sep = ' ')
	convex = convex_hull(points)
	# print("\nHull:")
	for obj in convex:
		print(obj.x, obj.y, sep = ' ')
	x_hull = [point.x for point in convex]
	x_hull.append(x_hull[0])
	y_hull = [point.y for point in convex]
	y_hull.append(y_hull[0])
	plt.scatter(X, Y, label = "circles", color = "green", marker = "o")
	plt.plot(x_hull, y_hull, label = "Convex Hull")
	plt.xlabel('X-Axis')
	plt.ylabel('Y-Axis')
	plt.title('Convex Hull of my Points!')
	plt.legend()
	plt.show()

