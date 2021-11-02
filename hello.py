#include<cstdio>
#include<cstring>
#include <vector>
#include <iostream>

using namespace std;

vector<int>odd;
vector<int>even;


int max_n = 4;

int check_even(int odd_index, int even_index, int max_num);

int check_odd(int odd_index, int even_index, int max_num);

void main() {
   odd.push_back(1);
   odd.push_back(-10);
   odd.push_back(3);
   odd.push_back(0);
   
   even.push_back(101);
   even.push_back(0);
   even.push_back(2);
   even.push_back(100);

   int max_num = 0;
   int sum = max_num;
   for (int i = 0; i < 4; i++) {
      int temp = check_even(i, -1, sum + odd[i]);
      if (temp > max_num)max_num = temp;
   }

   cout << max_num;

}

int check_even(int odd_index, int even_index, int max_num) {
   int sum = max_num;
   for (int i = even_index + 1; i < max_n; i++) {
      if (odd[odd_index] <= even[i]) {
         int temp = check_odd(odd_index, i, sum + even[i]);
         if (temp > max_num)max_num = temp;
      }
   }
   return max_num;
}

int check_odd(int odd_index, int even_index, int max_num) {
   int sum = max_num;
   for (int i = odd_index + 1; i < max_n; i++) {
      if (even[even_index] <= odd[i]) {
         int temp = check_even(i, even_index, sum + odd[i]);
         if (temp > max_num)max_num = temp;
      }
   }
   return max_num;
}