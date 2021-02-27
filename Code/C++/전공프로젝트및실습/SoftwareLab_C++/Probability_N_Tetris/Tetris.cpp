#include <iostream>
using namespace std;

int main()
{
	int hit[6], Ntry = 10000;
	int i;

	for (i = 0; i < 6; i++)
	{
		hit[i] = 0;
	}
	for (i = 0; i < Ntry; i++)
	{
		hit[rand() % 6]++;
	}
	for (i = 0; i < 6; i++)
	{
		cout << "P[" << i + 1 << "] = " << (float)hit[i] / Ntry << endl;
	}

	// Tetris
	float pa = 12.3, pb = 26.5, pc = 17.23, pd = 22.3, pe = 9.2, pf = 12.47;
	float x;
	float Pc, Pd, Pe, Pf;
	Pc = pa + pb + pc; Pd = Pc + pd; Pe = Pd + pe; Pf = 100.0;
	for (i = 0; i < 6; i++)
	{
		hit[i] = 0;
	}
	for (i = 0; i < Ntry; i++)
	{
		x = (float)rand() / RAND_MAX * 100.; // 0~100 RV
		if (x < pa)
			hit[0]++;
		else if (x < pa + pb)
			hit[1]++;
		else if (x < Pc)
			hit[2]++;
		else if (x < Pd)
			hit[3]++;
		else if (x < Pe)
			hit[4]++;
		else
			hit[5]++;

	}
	cout << endl;
	for (i = 0; i < 6; i++)
	{
		cout  << "P[" << i + 1 << "] = " << (float)hit[i] / Ntry * 100. << endl;
	}


	getchar();
	return 0;
}