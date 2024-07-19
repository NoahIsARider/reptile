#include<iostream>
#include<string>
using namespace std;
class MyInput
{
private:
	string data[10];

public:
	MyInput(string in)  // 把输入的字符串按逗号分成单独的字符串
	{
		int j = 0;
		string temp = "";
		for (int i = 0; i < in.size(); i++)
		{
			if (in[i] == '/')
			{
				data[j++] = temp;
				temp = "";
			}
			else
				temp = temp + in[i];
		}
		data[j] = temp;
	}
	string GetInput(int index)
	{
		return data[index];
	}
};
void main()
{
	string plus;
	string web[100] = { ""};
	string time[100] = { "" };
	int i = 0;
	while (cin >> plus)
	{
		MyInput in(plus);
		if (in.GetInput(0)[0] == '2')
			web[i] = "https://edition.cnn.com" + plus;
		else 
			web[i] = "https://edition.cnn.com" + plus;
		
	
			time[i] = in.GetInput(1)+'-'+ in.GetInput(2) +'-'+ in.GetInput(3);
		i++;
	}
	cout << i<<endl;
	for (int m = 0; m < i; m++)
	{
		cout <<"'"<< web[m]<<"'" <<"," << endl;
	}
	for (int m = 0; m < i; m++)
	{
		cout << time[m]<<endl;
	}
}
