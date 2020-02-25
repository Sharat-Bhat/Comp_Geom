import random, math
import matplotlib.pyplot as plt

dimen = 1000

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Edge:
	def __init__(self, p1, p2):
		self.start = p1
		self.end = p2

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

def random_orthogonal_polygon(n):
	points = []
	points.append(Point(dimen, dimen))
	points.append(Point(-dimen, dimen))
	points.append(Point(-dimen, -dimen))
	points.append(Point(dimen, -dimen))
	i = 4
	while i < n:
		i += 2
		m = len(points)
		j = random.randrange(m)
		while right_turn(points[(j-1)%m], points[j%m], points[(j+1)%m]):
			j = random.randrange(m)
		quadrant = None
		if points[(j-1)%m].x ==	points[(j)%m].x:
			if points[(j-1)%m].y < points[(j)%m].y:
				quadrant = 1
			else:
				quadrant = 3
		else:
			if points[(j-1)%m].x < points[(j)%m].x:
				quadrant = 4
			else:
				quadrant = 2
		# point1 = None, point2 = None, point3 = None
		if quadrant == 1:
			point1 = Point(random.uniform(points[(j+1)%m].x, points[j].x), points[j].y)
			point3 = Point(points[j].x, random.uniform(points[(j-1)%m].y, points[j].y))
			point2 = Point(point3.x, point1.y)
		elif quadrant == 2:
			point1 = Point(points[j].x, random.uniform(points[(j+1)%m].y, points[j].y))
			point3 = Point(random.uniform(points[(j)%m].x, points[(j-1)%m].x), points[j].y)
			point2 = Point(point3.x, point1.y)
		elif quadrant == 3:
			point1 = Point(random.uniform(points[(j)%m].x, points[(j+1)%m].x), points[j].y)
			point3 = Point(points[j].x, random.uniform(points[(j)%m].y, points[(j-1)%m].y))
			point2 = Point(point3.x, point1.y)
		elif quadrant == 4:
			point1 = Point(points[j].x, random.uniform(points[(j)%m].y, points[(j+1)%m].y))
			point3 = Point(random.uniform(points[(j-1)%m].x, points[(j)%m].x), points[j].y)
			point2 = Point(point3.x, point1.y)
		points[j] = point1
		points.insert(j, point2)
		points.insert(j, point3)
	return points

if __name__ == "__main__":
	n = random.randrange(3, 50)
	print(n)
	orthogonal_polygon = random_orthogonal_polygon(n)
	x_orthogonal_polygon = [point.x for point in orthogonal_polygon]
	x_orthogonal_polygon.append(x_orthogonal_polygon[0])
	y_orthogonal_polygon = [point.y for point in orthogonal_polygon]
	y_orthogonal_polygon.append(y_orthogonal_polygon[0])
	plt.scatter(x_orthogonal_polygon, y_orthogonal_polygon, label = "circles", color = "green", marker = "o")
	plt.plot(x_orthogonal_polygon, y_orthogonal_polygon, label = "Orthogonal Polygon")
	plt.xlabel('X-Axis')
	plt.ylabel('Y-Axis')
	plt.title('Random Orthogonal Polygon')
	plt.legend()
	plt.show()