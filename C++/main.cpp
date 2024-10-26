#include <iostream>

int main(){
    std::string isyoupass;

    std::cout << "What The PassWord: ";
    std::cin >> isyoupass;

    if(isyoupass == "mimo"){
        std::cout << "Hi Pass!!";
    }

    else if(isyoupass == "zaza"){
        std::cout << "i would let you pass but pass said mimo was the password";
    }

    else{
        std::cout << "GET OU";
    }

    return 0;
} 