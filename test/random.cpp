// compile with:  g++ -o random_mean random_mean.cc `root-config --cflags --glibs`

# include <cstdlib>  // needed to convert string argument to integer
# include <iostream>
# include "TRandom.h"
# include "time.h"

using namespace std;

void random_mean(Int_t nums)
{
  TRandom *R = new TRandom(time(0));
  Double_t *seed = new Double_t[nums];
  for (Int_t i = 0; i < nums; i++)
  {
    seed[i] = R->Rndm();
  }
  Double_t mean = 0.0;
  for (Int_t i = 0; i < nums; i++)
  {
    mean += seed[i];
  }
  mean /= nums;
  cout << "mean = " << mean << endl;
}

void random_mean()
{
  random_mean(100000000); // on default, take 1E8 numbers
}

# ifndef __CINT__  // the following code will be invisible for the interpreter

int main(int argc, char **argv)
{
  
  if (argc == 1)  // no parameter given
  {
    random_mean();
  }
  else
  {
    Int_t parameter = (Int_t) strtof(argv[1], NULL);  // convert the second parameter to an integer
    random_mean(parameter);
  }
}

# endif