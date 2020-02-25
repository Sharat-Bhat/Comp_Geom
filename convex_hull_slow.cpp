#include<iostream>
#include<math.h>
#include<fstream>
#include<stdlib.h>
#include<queue>
#define PI 3.14159

using namespace std;

struct point
{
	double x;
	double y;
};

struct Polygon
{
	vector<struct point> v;
};

bool right_of_line(struct point p1, struct point p2, struct point p)
{
	double ang1 = atan2(p2.y - p1.y, p2.x - p1.x);
	double ang2 = atan2(p.y - p1.y, p.x - p1.x);
	double ang = ang1 - ang2;
	if(ang > PI)
	{
		ang -= 2*PI;
	}
	else if(ang < -PI)
	{
		ang += 2*PI;
	}
	if(ang > 0)
		return true;
	else
		return false;
}

int main()
{
	int n;
	ifstream infile;
	infile.open("convex_hull_slow_input.txt");
	infile>>n;
	struct point* points = new struct point[n];
	vector<struct point>hull;
	for(int i=0; i<n; i++)
	{
		infile>>points[i].x>>points[i].y;
	}
	for(int i=0; i<n; i = (i+1)%n)
	{
		// cout<<endl;
		for(int j=0; j<n; j++)
		{
			if(i != j)
			{
				bool valid = true;
				for(int k=0; k<n; k++)
				{
					if(k!=i && k!=j)
					{
						if(right_of_line(points[i], points[j], points[k]))
						{
							// cout<<points[k].x<<" "<<points[k].y<<" is on right side of line "<<points[i].x<<" "<<points[i].y<<" and "<<points[j].x<<" "<<points[j].y<<endl;
							valid = false;
							break;
						}
					}
				}
				if(valid)
				{
					hull.push_back(points[i]);
					i = j;
					break;
				}
			}
		}
		if(hull.size() > 0)
		{
			struct point temp;
			temp = hull[0];
			if(points[i].x == temp.x && points[i].y == temp.y)
			{
				break;
			}
			i--;
		}
	}
	for(int i=0;  i< hull.size(); i++)
	{
		cout<<hull[i].x<<" "<<hull[i].y<<endl;
	}
	return 0;
}