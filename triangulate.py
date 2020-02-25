import random, math, operator
import matplotlib.pyplot as plt

class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		# self.angle = None

	def angle(self, p):
		angle = math.atan2(p.y - self.y, p.x - self.x)
		if angle > math.pi:
			angle -= 2*math.pi
		if angle < -math.pi:
			angle += 2*math.pi
		return angle

class Edge:

	def __init__(self, p1, p2):
		self.start = p1
		self.end = p2

	def angle(self, p):
		theta1 = math.atan2(self.start.y - p.y, self.start.x - p.x)
		theta2 = math.atan2(self.end.y - p.y, self.end.x - p.x)
		theta = theta2 - theta1
		if theta > math.pi:
			theta -= 2*math.pi
		elif theta < -math.pi:
			theta += 2*math.pi
		return theta

	def left_side_point(self, p):
		if self.angle(p) > 0:
			return True
		else:
			return False

	def intersect(self, e):
		opp1 = (self.left_side_point(e.start) != self.left_side_point(e.end))
		opp2 =  (e.left_side_point(self.start) != e.left_side_point(self.start))
		return opp2 and opp1

	def mid_point(self):
		mid_x = (self.start.x + self.end.x)/2
		mid_y = (self.start.y + self.end.y)/2
		return Point(mid_x, mid_y)

class Polygon:

	def __init__(self, poly):
		self.numVertices = len(poly)
		self.points = poly

	def inside(self, p):
		thresh = 0.01
		ref = math.atan2(self.points[-1].y - p.y, self.points[-1].x - p.x)
		total = 0
		n = len(self.points)
		for i in range(n):
			ang = math.atan2(self.points[i].y - p.y, self.points[i].x - p.x)
			diff = ang - ref
			if diff > math.pi:
				diff -= 2*math.pi
			if diff < -math.pi:
				diff += 2*math.pi
			total += diff
			ref = ang
		if abs(total) < thresh:
			print("The point is outside")
			return False
		elif abs(total - 2*math.pi) < thresh:
			print("The point is inside")
			return True
		else:
			print("Nothing")
			return False

def random_polygon():
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

	if len(points) <=3:
		return points
	# print(points[0].x, points[0].y)
	x_avg = sum(point.x for point in points)/len(points)
	y_avg = sum(point.y for point in points)/len(points)
	for point in points:
		# if point == points[0]:
			# point.angle = -math.pi
		point.angle = math.atan2(point.y - y_avg, point.x - x_avg)
	points.sort(key = lambda x: x.angle)
	# max_angle = points[len(points) - 1].angle
	# min_angle = point[1]
	# print(x_avg, y_avg)
	return points

def triangulate(points):
	diag = []
	print(len(points))
	# if len(points) == 3:
	# 	return diag
	polygon = Polygon(points)
	n = len(points)
	for k in range(n-3):
		new_n = len(points)
		for i in range(new_n):
			found = True
			e = Edge(points[i-2], points[i-1])
			if e.left_side_point(points[(i)]):
				e1 = Edge(points[i-2], points[i])
				mid = e1.mid_point()
				if not polygon.inside(mid):
					continue
				for j in range(new_n-4):
					e2 = Edge(points[(i-4-j)], points[(i-3-j)])
					if e1.intersect(e2):
						found = False
						break
				if found:
					diag.append(e1)
					points.remove(points[i-1])
					break
	# for edge in diag:
		# print(edge.start.x, edge.start.y, edge.end.x, edge.end.y)
	return diag






if __name__ == "__main__":
	# poly1 = []
	poly1 = random_polygon()
	temp_poly = []
	temp_poly += poly1
	diagonals = triangulate(temp_poly)
	x_poly1 = [point.x for point in poly1]
	x_poly1.append(x_poly1[0])
	# print(x_poly1)
	y_poly1 = [point.y for point in poly1]
	y_poly1.append(y_poly1[0])
	# print(y_poly1)
	plt.scatter(x_poly1, y_poly1, label = "circles", color = "green", marker = "o")
	plt.plot(x_poly1, y_poly1, label = "Polygon")
	for e in diagonals:
		x = [float(e.start.x), float(e.end.x)]
		y = [float(e.start.y), float(e.end.y)]
		plt.plot(x, y, label = "Diagonal")
	plt.xlabel("X-Axis")
	plt.ylabel("Y-Axis")
	plt.title("Triangulation")
	plt.legend()
	plt.show()
