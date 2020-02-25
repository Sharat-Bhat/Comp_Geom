import random, operator, math
import matplotlib.pyplot as plt

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.angle = None


def polygon_creator(points):
	if len(points) <=3:
		return points
	print(points[0].x, points[0].y)
	x_avg = sum(point.x for point in points)/len(points)
	y_avg = sum(point.y for point in points)/len(points)
	for point in points:
		# if point == points[0]:
			# point.angle = -math.pi
		point.angle = math.atan2(point.y - y_avg, point.x - x_avg)
	points.sort(key = lambda x: x.angle)
	# max_angle = points[len(points) - 1].angle
	# min_angle = point[1]
	print(x_avg, y_avg)
	return points

if __name__ == "__main__":
	points = []
	# x_polygon = []
	# y_polygon = []
	n = random.randrange(3, 30)
	# n = 60
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