//
//  md5.hpp
//  
//
//  Created by Madhu RAJAGOPAL on 11/9/21.
//

#ifndef md5_hpp
#define md5_hpp

#include <iostream>

class MD5
{
public:
  md5();
  ~md5();
  
private:
  uint32_t a0;
  uint32_t b0;
  uint32_t c0;
  uint32_t d0;
  uint8_t digest[16];
  uint32_t count[2];
  const static int blocksize = 64;
  uint8_t buffer[blocksize];

  uint32_t F(uint32_t x, uint32_t y, uint32_t z);
  uint32_t G(uint32_t x, uint32_t y, uint32_t z);
  uint32_t H(uint32_t x, uint32_t y, uint32_t z);
  uint32_t I(uint32_t x, uint32_t y, uint32_t z);
  void FF(uint32_t &a, uint32_t b, uint32_t c, uint32_t d, uint32_t x, uint32_t s, uint32_t ac);
  void GG(uint32_t &a, uint32_t b, uint32_t c, uint32_t d, uint32_t x, uint32_t s, uint32_t ac);
  void HH(uint32_t &a, uint32_t b, uint32_t c, uint32_t d, uint32_t x, uint32_t s, uint32_t ac);
  void II(uint32_t &a, uint32_t b, uint32_t c, uint32_t d, uint32_t x, uint32_t s, uint32_t ac);
}

#endif /* md5_hpp */
