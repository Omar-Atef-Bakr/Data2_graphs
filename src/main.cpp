#include <iostream>
using namespace std;

extern "C" {
    __declspec(dllexport) int fun();
    __declspec(dllexport) int main();
}


int fun() {
    cout << "msa msa 3al f5ad el kwayesa" << endl;
    return 1;
}

int main()
{
    std::cout << "Hello world!" << std::endl;
}


