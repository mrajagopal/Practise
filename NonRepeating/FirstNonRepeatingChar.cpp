#include <iostream>
#include <vector>
#include <string>

char find(std::vector<char> v);

char find(std::vector<char> v)
{
  if (v[0] != v[1])
    return v[0];

  for(int i = 1; i < v.size(); i++)
  {
    if ((v[i] != v[i-1]) && (v[i] != v[i+1]))
    return v[i];
  }
  return '\0';
}

int main()
{
  std::cout << "Enter a sequence of repeating and non-repeating characters: ";
  std::string s("");
  std::cin >> s;
  //std::string s("abcdefg");
  std::cout << s << std::endl;
  std::vector<char> v(s.begin(), s.end());

  char c = find(v);
  if (c == '\0')
    std::cout << "There are no unique characters in the string provided" << std::endl;
  else  
    std::cout << "The first unique character is " << c << std::endl; 

  return 0;
}
