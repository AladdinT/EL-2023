#include <iostream>
#include <forward_list>

int main ()
{
    std::forward_list<int>mylist{1,2,3,4,5};
    auto it=mylist.begin();
    std::advance(it,2);
    
    std::cout << it._M_node << std::endl;
    std::cout << &(*it) << std::endl;
    std::cout << (it._M_next())._M_node << std::endl;

    std::cout << *it << std::endl;
    std::cout << *(it._M_next()) << std::endl;


    return 0;
}