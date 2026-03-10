#include <iostream>
using namespace std;
int temerature_Conversion() {
    float fahrenheit;
    int celsius;

    cout << "Temperature Conversion" << endl;
     cout<<"----------------------" << endl;    
     cout<<"F = fahrenheit" << endl;
     cout<<"C = celsius" << endl;
     cout<<"enter F or C to convert: ";
     char unit;
     cin>>unit;


    if(unit == 'F' || unit == 'f') {
        cout << "Enter temperature in Fahrenheit: ";
        cin >> fahrenheit;
        celsius = (fahrenheit - 32) * 5/9;
        cout << "Temperature in Celsius: " << celsius << endl;
    }
    else if(unit == 'C' || unit == 'c') {
        cout << "Enter temperature in Celsius: ";
    cin >> celsius;

    fahrenheit = (celsius * 9/5) + 32;

        cout << "Temperature in Fahrenheit: " << fahrenheit << endl;
    }
    else {
        cout << "Invalid unit. Please enter 'F' or 'C'." << endl;
    }
    return 0;
}

int main() {
    temerature_Conversion();
    if (temerature_Conversion() == 0) {
        cout << "Temperature conversion successful." << endl;
    } else {
        cout << "Temperature conversion failed." << endl;
    }

    cout<<"Do you want to convert another temperature? (y/n): ";
    char choice;
    cin>>choice;
    if(choice == 'y' || choice == 'Y') {
        temerature_Conversion();
    } else {
        cout << "Exiting the program." << endl;
    }
   

    

    return 0;
}