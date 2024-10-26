#include <iostream>

int main(){
    
    char op;
    double num1;
    double num2;
    double result;

    std::cout << "Enter Either (+ - * /): ";
    std::cin >> op;

    std::cout << "Enter First Number: ";
    std::cin >> num1;

    std::cout << "Enter Second Number: ";
    std::cin >> num2;

    switch(op){
        case '+':
            result = num1 + num2;
            std::cout << "result: " << result << '\n';
            break;

        case '-':
            result = num1 - num2;
            std::cout << "result: " << result << '\n';
            break;

        case '*':
            result = num1 * num2;
            std::cout << "result: " << result << '\n';
            break;

        case '/':
            result = num1 / num2;
            std::cout << "result: " << result << '\n';
            break;

        default:
            std::cout << "invalid respond";
    }
    
    std::cin.ignore();
    std::cin.get();
    return 0;
} 