#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

struct Node{
   Node* next;
   Node* prev;
   int value;
   int key;
   Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
   Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{
   
   protected: 
   map<int,Node*> mp; //map the key to the node in the linked list
   int cp;  //capacity
   Node* tail; // double linked list tail pointer
   Node* head; // double linked list head pointer
   virtual void set(int, int) = 0; //set function
   virtual int get(int) = 0; //get function

};
class LRUCache : protected Cache
{
//    map<int,Node*> mp;
//    int cp;  
//    Node* tail; 
//    Node* head; 
public:
    LRUCache(int capacity)   
    {
        this->cp = capacity;
        Node* temp;
        for(int i=0 ; i<capacity ;i++)
        {
            //init
            temp = new Node(nullptr,nullptr, i,0);
            mp.insert({i,temp});
        }
        
        for(int i=1 ; i<capacity ;i++)
        {
            if(i == capacity-1)
            {
                mp[i]->next = nullptr;
                mp[i]->prev = mp[i-1];
                break;
            }
            else if( i ==0 )
            {
                mp[i]->prev = nullptr;
                mp[i]->next = mp[1];
                continue;
            }
            
            //assign
            mp[i]->next = mp[i+1];
            mp[i]->prev = mp[i-1];
        }
        
        head = mp[0];
        tail = mp[capacity-1];
        
    }
    int get (int index)
    {
        if(index > cp)
        {
            return -1;
        }
        
        return mp[index]->value;
    }
    
    void set(int index, int value)
    {
        if(index > cp)
        {
            return;
        }
        
        mp[index]->value = value;
    }
    
};


int main() {
   int n, capacity,i;
   cin >> n >> capacity;
   LRUCache l(capacity);
   for(i=0;i<n;i++) {
      string command;
      cin >> command;
      if(command == "get") {
         int key;
         cin >> key;
         cout << l.get(key) << endl;
      } 
      else if(command == "set") {
         int key, value;
         cin >> key >> value;
         l.set(key,value);
      }
   }
   return 0;
}
