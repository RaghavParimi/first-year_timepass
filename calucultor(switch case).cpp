#include<iostream>
using namespace std;

int main(){
    char op;
    float num1,num2;
    float result;

    cout<<"\n************CALCULATOR************\n";

    cout<<"Enter operator either + ,-,*,/: ";
    cin>>op;

    cout<<"Enter first number: ";
    cin>>num1;
    cout<<"Enter second number: ";
    cin>>num2;

    switch(op){
        case '+':
           result = num1 + num2;
            break;
        case '-':
           result = num1 - num2;
            break;
        case '*':
           result = num1 * num2;
            break;
        case '/':
            result = num1 / num2;
            break;
        default:
            cout<<"Error! operator is not correct";
            break;
    }

    cout<<"Result: "<<result;
    cout<<"\n**********************************";
    return 0;
}