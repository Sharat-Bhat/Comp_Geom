// Finds out if the point is in the interior or in the exterior on the given polygon
// Polygon dimension is mentioned in first line and coordinates are in anti-clockwise direstions

#include<iostream>
#include<fstream>
#include<math.h>
#include<stdlib.h>
#define PI 3.14159

using namespace std;

int main()
{
	ifstream infile;
	infile.open("interior_exterior_input.txt");
	int n;
	infile>>n;
	double* x = new double[n];
	double* y = new double[n];
	for(int i=0; i<n; i++)
	{
		infile>>x[i]>>y[i];
	}
	double x1, y1;
	while(infile>>x1>>y1)
	{
		double ang1, ang2, ang, sum = 0;
		for(int i=0; i<n; i++)
		{
			int j = (i+1)%n;
			ang1 = atan2(y[i] - y1, x[i] - x1);
			ang2 = atan2(y[j] - y1, x[j] - x1);
			ang = ang2-ang1;
			if(ang <= -PI)
			{
				ang += 2*PI;
			}
			else if(ang >= PI)
			{
				ang -= 2*PI;
			}
			sum +=ang;
		}
		if(abs(sum-2*PI) < 0.1)
		{
			cout<<x1<<" "<<y1<<" inside"<<endl;
		}
		else if(abs(sum) < 0.1)
		{
			cout<<x1<<" "<<y1<<" outside"<<endl;
		}
		else
		{
			cout<<x1<<" "<<y1<<endl;
		}
	}
	return 0;
}