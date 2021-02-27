#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>

using namespace std;

#define PI 3.14159265
#define MAXPOINTS 1000 // xπÊ«‚
#define MAXSTEPS 1000 // t steps
#define MINPOINTS 20

void init_param(void);
void init_line(void);
void update(void);
void printfinal(void);

int nsteps,						// number of time steps
tpoints,						// total points along string
rcode;							// generic return code
float *fxn, *fxnp1, *fxnm1;		// values at time t
float *fxhalf, *fxforth;

void init_param(void)
{
	string tchar;
	tpoints = 0, nsteps = 0;
	while ((tpoints < MINPOINTS) || (tpoints > MAXPOINTS))
	{
		cout << "Enter number of points along vibrating string [" << MINPOINTS << ", " << MAXPOINTS << "]" << endl;
		// cin >> tchar;
		//tpoints = stoi(tchar)
		tpoints = MAXPOINTS * 2 / 3;

		if ((tpoints < MINPOINTS) || (tpoints > MAXPOINTS))
		{
			cout << "Invaild, Please enter value [" << MINPOINTS << ", " << MAXPOINTS << "]" << endl;
		}
	}
	while ((nsteps < 1) || (nsteps > MAXSTEPS))
	{
		cout << "Enter number of time steps [1-" << MAXSTEPS << "]" << endl;
		//cin >> tchar;
		// nsteps = atoi(tchar);
		nsteps = MAXSTEPS * 2 / 3;
		if((nsteps < 1) || (nsteps > MAXSTEPS))
			cout << "Invaild, Please enter value [1-" << MAXSTEPS << "]" << endl;
		cout << "Using points = " << tpoints << ", steps = " << nsteps << endl;
	}
}

void init_line(void)
{
	int i, j;
	double x, fac, k, tmp;
	fac = 2.0*PI;
	k = 0.0;
	tmp = tpoints - 1;				//1period
	for (j = 1; j <= tpoints; j++)	// initial condition f(x,t)
	{
		x = k / tmp;
		fxn[j] = sin(fac*x);
		k += 1.;
	}

	for (i = 1; i <= tpoints; i++)	// initial condition f(x, t-dt) = f(x,t)	
	{
		fxnm1[i] = fxn[i];
	}
}

// Calculate new values using wave equation
// d^2 f(x,t) / dt^2 = gamma (d^2 f(x,t) / dx^2)

void do_math(int i)
{
	double dtime, c, dx, tau, sqtau;
	dtime = 0.3;
	c = 1.0;
	dx = 10;
	tau = (c*dtime / dx);
	sqtau = tau * tau;
	fxnp1[i] = (2.0 * fxn[i]) - fxnm1[i] + (sqtau * (fxn[i - 1] - (2.0*fxn[i]) + fxn[i + 1]));
}

// Update all values along line a specified number of times

void update()
{
	int i, j;
	// Update values for each time step
	for (i = 1; i <= nsteps; i++)				// time t
	{
		for (j = 1; j <= tpoints; j++)			// location x
		{
			if ((j == 1) || (i == tpoints))
			{
				fxnp1[j] = 0.0;
			}
			else
				do_math(j);
		}
	}

	for (j = 1; j <= tpoints; j++)
	{
		fxnm1[j] = fxn[j];		// f(x, t-dt) = f(x,t)
		fxn[j] = fxnp1[j];		// f(x,t) = f(x, t+dt)
		if (i == nsteps / 2)
		{
			for (j = 1; j <= tpoints; j++)
			{
				fxhalf[j - 1] = fxn[j];
			}
		}
		if (i == nsteps / 4)
		{
			for (j = 1; j <= tpoints; j++)
			{
				fxforth[j - 1] = fxn[j];
			}
		}
	}
}

void printfinal()
{
	ofstream fp("final_wave.txt");

	int i;

	fp << setw(15) << "t = T/4 " << setw(15) << "t = T/2 " << setw(15) << "t = T " << endl;
	for (i = 1; i <= tpoints; i++)
	{
		fp << setw(15) << fxforth[i - 1] << setw(15) << fxhalf[i - 1] << setw(15) << fxn[i] << endl;

	}
	fp.close();

}

int main(int argc, char *argv[])
{
	cout << "Staring serial version of wave equation..." << endl;
	init_param();
	fxn = new float[tpoints + 2];
	fxnp1 = new float[tpoints + 2];
	fxnm1 = new float[tpoints + 2];
	fxhalf = new float[tpoints];
	fxforth = new float[tpoints];
	cout << "Initializing points on the line" << endl;
	init_line();
	cout << "Updating all points for all time steps" << endl;
	update();
	cout << "Printing final results" << endl;
	printfinal();
	cout << endl << "Done" << endl << endl;
	getchar();

	return 0;
}