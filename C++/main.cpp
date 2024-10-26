#include <iostream>

int main(){

    // end of day 1 //
    std::string name;
    int age;

    std::cout << "What Your Name: ";
    std::getline(std::cin, name);

    std::cout << "What Your Age: ";
    std::cin >> age;

    std::cout << name << '\n'; 
    std::cout << age << '\n';
    return 0;
} 