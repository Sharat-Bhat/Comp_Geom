import random, operator, math
import matplotlib.pyplot as plt

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Edge:
	def __init__(self, p1, p2):
		self.start = p1
		self.end = p2

def line_eq(e):
	abc = []
	a = e.end.y - e.start.y
	abc.append(a)
	b = e.start.x - e.end.x
	abc.append(b)
	c = e.start.x*(e.end.y - e.start.y) - e.start.y*(e.end.x - e.start.x)
	abc.append(c)
	return abc

def line_intersect(e1, e2):
	abc1 = line_eq(e1)
	abc2 = line_eq(e2)
	d = abc1[0]*abc2[1] - abc1[1]*abc2[0]
	dx = abc1[2]*abc2[1] - abc1[1]*abc2[2]
	dy = abc1[0]*abc2[2] - abc1[2]*abc2[0]
	intersection = Point(dx/d, dy/d)
	return intersection

def angle_subtended(e, p):
	ang1 = math.atan2(p.y - e.start.y, p.x - e.start.x)
	ang2 = math.atan2(p.y - e.end.y, p.x - e.end.x)
	ang = ang2 - ang1
	if ang > math.pi:
		ang -= 2*math.pi
	if ang < -math.pi:
		ang += 2*math.pi
	return ang	

def same_side(e, p1, p2):
	ang1 = angle_subtended(e, p1)
	ang2 = angle_subtended(e, p2)
	if ang1*ang2 > 0:
		return True
	else:
		return False

def random_point(v, e, inside):
	a3 = random.random()
	a2 = 1 - a3
	a1 = random.random()
	# print(inside)
	if not inside:
		a1 = -a1
	x = (a1*v.x + a2*e.start.x + a3*e.end.x)/(a1+1)
	y = (a1*v.y + a2*e.start.y + a3*e.end.y)/(a1+1)
	if (x > 1000 or x < -1000) or (y > 1000 or y < -1000):
		return None
	point = Point(x,y)
	# print(point.x, point.y)
	return point

def random_convex_polygon(n):
	points = []
	apex = []
	if n < 3:
		for i in range(n):
			x = random.uniform(-1000, 1000)
			y = random.uniform(-1000, 1000)
			point = Point(x, y)
			points.append(point)
			# print("Hi")
		return points
	else:
		for i in range(3):
			x = random.uniform(-1000, 1000)
			y = random.uniform(-1000, 1000)
			point = Point(x, y)
			# print(point.x, point.y)
			points.append(point)
			# print("Hi")

		temp_e = Edge(points[0], points[1])
		if angle_subtended(temp_e, points[2]) < 0:
			points[0], points[1] = points[1], points[0]
		# The triangle must be anti clockwise now
		apex = points
		# temp = apex.pop()
		# apex.insert(0, temp)
		apex = apex[-1:]+apex[:-1]
		i = 3
		while i < n:
			x_convex_polygon = [point.x for point in points]
			# print("point_x")
			# print(x_convex_polygon)
			y_convex_polygon = [point.y for point in points]
			# print("point_y")
			# print(y_convex_polygon)
			x_apex = [point.x for point in apex]
			# print("apex_x")
			# print(x_apex)
			y_apex = [point.y for point in apex]
			# print("apex_y")
			# print(y_apex)
			m = len(apex)
			j = random.randrange(m)
			# j = (int)(m/2)
			e = Edge(points[j%m], points[(j+1)%m])
			if same_side(e, apex[j], points[(j+2)%m]):
				new_point = random_point(apex[j], e, False)
			else:
				new_point = random_point(apex[j], e, True)
			while(not new_point):
				j = random.randrange(m)
				# j = (int)(m/2)
				e = Edge(points[j%m], points[(j+1)%m])
				if same_side(e, apex[j], points[(j+2)%m]):
					new_point = random_point(apex[j], e, False)
				else:
					new_point = random_point(apex[j], e, True)
				# print("j = %d", j)
			# m +=1
			apex.pop(j)
			j = (j+1)%m
			points.insert(j, new_point)
			# print("Hi")
			k  = j			
			m = len(points)
			e_3 = Edge(points[(j-3)%m], points[(j-2)%m])
			e_2 = Edge(points[(j-2)%m], points[(j-1)%m])
			e_1 = Edge(points[(j-1)%m], points[(j)%m])
			e1 = Edge(points[(j)%m], points[(j+1)%m])
			e2 = Edge(points[(j+1)%m], points[(j+2)%m])
			e3 = Edge(points[(j+2)%m], points[(j+3)%m])
			temp = line_intersect(e1,e_2)
			apex.insert((j-1)%(len(apex)+1), temp)
			temp = line_intersect(e2,e_1)
			apex.insert((j)%(len(apex)+1), temp)
			apex[(j+1)%len(apex)] = line_intersect(e1, e3)
			apex[(j-2)%len(apex)] = line_intersect(e_1, e_3)
			# x = random.uniform(-1000, 1000)
			# y = random.uniform(-1000, 1000)
			# for j in range(len(points)):
			# 	m = len(points)
			# 	e = Edge(points[j%m], points[(j+1)%m])
			# 	e1 = Edge(points[(j-1)%m], points[j%m])
			# 	e2 = Edge(points[(j+1)%m], points[(j+2)%m])
			i = i+1
		return points

if __name__ == "__main__":
	n = random.randrange(3, 50)
	# n = 10
	print(n)
	convex_polygon = random_convex_polygon(n)
	# x_apex = [point.x for point in apex]
	# y_apex = [point.y for point in apex]
	x_convex_polygon = [point.x for point in convex_polygon]
	# print(x_convex_polygon)
	x_convex_polygon.append(x_convex_polygon[0])
	y_convex_polygon = [point.y for point in convex_polygon]
	# print(y_convex_polygon)
	y_convex_polygon.append(y_convex_polygon[0])
	plt.scatter(x_convex_polygon, y_convex_polygon, label = "circles", color = "green", marker = "o")
	# plt.scatter(x_apex, y_apex, label = "circles", color = "red", marker = "o")
	plt.plot(x_convex_polygon, y_convex_polygon, label = "Convex Polygon")
	plt.xlabel('X-Axis')
	plt.ylabel('Y-Axis')
	plt.title('Random Convex Polygon')
	plt.legend()
	plt.show()