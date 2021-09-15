//
//  md5.cpp
//  
//
//  Created by Madhu RAJAGOPAL on 11/9/21.
//

#include <cstdint>
#include "md5.hpp"

MD5::md5()
{
  count[0] = 0;
  count[1] = 0;
  
  // Initialize variables:
  a0 = 0x67452301   // A
  b0 = 0xefcdab89   // B
  c0 = 0x98badcfe   // C
  d0 = 0x10325476   // D
}

MD5::~md5()
{}

uint32_t MD5::F(uint32_t x, uint32_t y, uint32_t z)
{
  return x&y | ~x&z;
}

uint32_t MD5::G(uint32_t x, uint32_t y, uint32_t z)
{
  return x&z | y&z;
}

uint32_t MD5::H(uint32_t x, uint32_t y, uint32_t z)
{
  return y ^ (x | ~z);
}

uint32_t MD5::I(uint32_t x, uint32_t y, uint32_t z)
{
  return (x << n) | (x >> (32 - n));
}

void MD5::FF(uint32_t &a, uint32_t b, uint32_t c, uint32_t d, uint32_t x, uint32_t s, uint32_t ac)
{
  a = rotate_left(a + F(b,c,d) + x + ac, s);
}

void MD5::GG(uint32_t &a, uint32_t b, uint32_t c, uint32_t d, uint32_t x, uint32_t s, uint32_t ac)
{
  
}
void MD5::HH(uint32_t &a, uint32_t b, uint32_t c, uint32_t d, uint32_t x, uint32_t s, uint32_t ac)
{
  
}
void MD5::II(uint32_t &a, uint32_t b, uint32_t c, uint32_t d, uint32_t x, uint32_t s, uint32_t ac)
{
  
}


void MD5::transform(const uint8_t block[blocksize])
{
  uint32_t a = a0, b = b0, c = c0, d = d0, x[16];
  decode (x, block, blocksize);

}

void MD5::update(const char input[]; int32_t length)
{
  int32_t index = count[0] / 8 % blocksize;
  
  if ((count[0] += (length << 3)) < (length << 3))
    count[1]++;
  count[1] += length >> 29;
  int32_t firstpart = 64 - index;
  
  int32_t i;
  if(legnth >= firstpart)
  {
    memcpy(&buffer[inde], input, firstpart);
    transform(buffer);
  }
}
