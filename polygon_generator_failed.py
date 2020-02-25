"""
	Algorithm:
		Divide the points into upper and lower half planes and then sort the respective 
		points

"""
import random, operator, math
import matplotlib.pyplot as plt

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y



def polygon_creator(points):
	if len(points) <=3:
		return points
	# mean_y = sum(point.y for point in points)/len(points)
	# for point in points:
	# 	print("{} {}".format(point.x, point.y))
	# print("")
	points.sort(key = lambda point: point.y)
	mid = int(len(points)/2)
	init = points[:mid]
	# for point in init:
	# 	print("{} {}".format(point.x, point.y))
	# print("")
	final = points[mid:]
	# for point in final:
	# 	print("{} {}".format(point.x, point.y))
	# print("")
	init.sort(key = lambda point: point.x)
	final.sort(key = lambda point: point.x, reverse = True)
	init = init+final
	# for point in points:
	# 	print("{} {}".format(point.x, point.y))
	# print("")
	# for point in init:
	# 	print("{} {}".format(point.x, point.y))
	return init

if __name__ == "__main__":
	points = []
	# x_polygon = []
	# y_polygon = []
	# n = random.randrange(3, 50)
	n = 6
	for i in range(n):
		x = random.uniform(-1000, 1000)
		y = random.uniform(-1000, 1000)
		point = Point(x, y)
		points.append(point)

	polygon = polygon_creator(points)
	# print("kdgyuk")
	x_polygon = [point.x for point in polygon]
	x_polygon.append(x_polygon[0])
	y_polygon = [point.y for point in polygon]
	y_polygon.append(y_polygon[0])
	plt.scatter(x_polygon, y_polygon, label = "circles", color = "green", marker = "o")
	plt.plot(x_polygon, y_polygon, label = "Polygon")
	plt.xlabel('X-Axis')
	plt.ylabel('Y-Axis')
	plt.title('Polygon from random points')
	plt.legend()
	plt.show()