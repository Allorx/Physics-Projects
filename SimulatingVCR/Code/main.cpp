#include <math.h>
#include <iostream>
#include <fstream>
#include <complex>

using namespace std;

const complex<long double> i(0, 1.0);
const long double pi = acos(-1.0);
// variables

long double a = 0.045;
long double *ptr_a = &a;
long double b = 0.015;
long double *ptr_b = &b;

const long double gamma1 = 12;
//const long double gamma1 = 5870.84148728;
const long double permitivity = 1.41 * 1.41;
long double phi = pi / 4.0;
long double *ptr_phi = &phi;
long double phiVar = 0;
long double *ptr_phiVar = &phiVar;

long double psi = 0.0 * pi / 180.0;

const long double lambda = 0.004;
const long double c = 299792458.0;
const long double Beta = sqrt(1.0 - (1.0 / (gamma1 * gamma1)));
const long double omega = (2.0 * pi * c) / lambda;
const long double alpha = (pi / 2.0) - phi - psi;

//angle
long double theta_p = -20.0 * pi / 180.0;
long double *ptr_theta_p = &theta_p;

long double h = b / cos(alpha);

long double Kval()
{
    return sqrt(1.0L + pow(gamma1 * Beta * sin(theta_p - alpha) * sin(phiVar), 2.0L));
}

complex<long double> Pval()
{
    return cos(alpha) - Beta * sqrt(permitivity - pow(sin(theta_p - alpha), 2.0L)) + i * pow(gamma1, -1.0L) * Kval() * sin(alpha);
}

complex<long double> SigmaVal()
{
    return sin(alpha) + Beta * cos(phiVar) * sin(theta_p - alpha) - i * pow(gamma1, -1.0L) * Kval() * cos(alpha);
}

long double PartA1()
{
    return ((exp(2.0L) * pow(Beta, 2.0L)) / (4.0L * pow(pi, 2.0L) * c)) * (pow(cos(theta_p - alpha), 2.0L) / norm(Pval())) * norm((permitivity - 1.0L) / permitivity);
}

complex<long double> PartA2()
{
    return 1.0L - ((Pval() * exp(i * (omega / (Beta * c)) * SigmaVal() * a * (1.0L / tan(phi))) + SigmaVal() * (1.0L / tan(phi)) * exp(-i * a * (omega / (Beta * c)) * Pval())) / (Pval() + SigmaVal() * (1.0L / tan(phi))));
}

long double PartA()
{
    return PartA1() * norm(PartA2());
}

complex<long double> PartB1()
{
    return permitivity / (permitivity * cos(theta_p - alpha) + sqrt(permitivity - pow(sin(theta_p - alpha), 2.0L)));
}

complex<long double> PartB2()
{
    complex<long double> p1 = cos(alpha) * (pow(gamma1, -1.0L) * sin(theta_p - alpha) - i * Kval() * cos(phiVar) * sqrt(permitivity - pow(sin(theta_p - alpha), 2.0L)));
    complex<long double> p2 = sin(alpha) * (i * Kval() * sin(theta_p - alpha) + pow(gamma1, -1.0L) * cos(phiVar) * sqrt(permitivity - pow(sin(theta_p - alpha), 2.0L)));
    complex<long double> p3 = gamma1 * Beta * sin(theta_p - alpha) * sqrt(permitivity - pow(sin(theta_p - alpha), 2.0L)) * pow(sin(phiVar), 2.0L);
    return p1 + p2 - p3;
}

long double PartB3()
{
    long double p1 = norm(sqrt(permitivity) / (cos(theta_p - alpha) + sqrt(permitivity - pow(sin(theta_p - alpha), 2.0L))));
    long double p2 = pow(gamma1 * sin(phiVar), 2.0L) * (pow(sin(theta_p - alpha), 2.0L) + norm(sqrt(permitivity - pow(sin(theta_p - alpha), 2.0L))));
    return p1 * p2;
}

long double PartB4()
{
    return 1.0L - pow(Beta, 2.0L) * pow(cos(theta_p - alpha), 2.0L) + 2.0L * Beta * pow(gamma1, -2.0L) * sin(alpha) * sin(theta_p - alpha) * cos(phiVar) - pow(gamma1, -2.0L) * pow(sin(alpha), 2.0L) * (pow(Kval(), 2.0L) - pow(gamma1, -2.0L));
}

long double PartB()
{
    return norm(PartB1()) * norm(PartB2()) + PartB3() * PartB4();
}

long double PartC1()
{
    return exp(-2.0L * (omega / (gamma1 * Beta * c)) * (h + a * 1.0L / tan(phi)) * Kval() * cos(alpha));
}

long double PartC2()
{
    return pow(Kval(), 2.0L) * (1.0L - pow(Beta, 2.0L) * pow(cos(theta_p - alpha), 2.0L) + pow(Beta, 2.0L) * pow(sin(alpha), 2.0L) * (1.0L - pow(sin(theta_p - alpha), 2.0L) * pow(sin(phiVar), 2.0L)) + 2.0L * Beta * sin(alpha) * cos(phiVar) * sin(theta_p - alpha));
}

long double PartC()
{
    return PartC1() / PartC2();
}

long double SpectralAD()
{
    /*returns spectral angular distribution split into parts from eq 16:
      - A is first part of eq, B is inner brackets part, C is last part of eq.
      - Numbered in chunks.
    */
    return PartA() * PartB() * PartC();
}

int main()
{
    // Outputs spectral angular distribution to data.txt at regular intervals of granularity from -20 to 70 deg.
    int granularity = 5000;
    ofstream myfile;
    myfile.open("data.txt");
    *ptr_a = 0.01;
    for (int i = 0; i < granularity; i++)
    {
        myfile << a << " " << SpectralAD() << endl;
        *ptr_a += 0.035 / granularity;
        //*ptr_theta_p += 90 * pi / (180 * granularity);
    }

    myfile.close();

    // 3D plot
    granularity = 1000;
    *ptr_theta_p = -20.0 * pi / 180;
    ofstream dfile;
    dfile.open("data3D.txt", ios::app);
    *ptr_a = 0.01;
    for (int j = 0; j < granularity; j++)
    {
        for (int i = 0; i < granularity; i++)
        {
            dfile << theta_p * 180 / pi << " " << SpectralAD() << " " << a << endl;
            *ptr_theta_p += 90 * pi / (180 * granularity);
        }
        *ptr_a += 0.035 / granularity;
        *ptr_theta_p = -20.0 * pi / 180;
    }
    dfile.close();
    return 0;
}