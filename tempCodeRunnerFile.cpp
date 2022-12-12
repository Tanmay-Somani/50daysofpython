#include<iostream>
using namespace std;
class Marks{
	public:
		int m=0;
	void putdata(int a)
	{
		m=a;
	}
	void sum(Marks a,Marks b,Marks c,Marks d,Marks e)
	{
		m=(a.m)+(b.m)+(c.m)+(d.m)+(e.m);
		cout<<"The sum is "<<m<<endl;
	}
};
int main()
{
	Marks m1,m2,m3,m4,m5,plus;
	m1.putdata(80);
	m2.putdata(50);
	m3.putdata(60);
	m4.putdata(70);
	m5.putdata(40);
	plus.sum(m1,m2,m3,m4,m5);
	return 0;
}