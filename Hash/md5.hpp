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
  MD5();
  ~MD5();
  std::string hexdigest() const;
  MD5& finalize();
  void update(const unsigned char input[], int32_t length);
  void update(const char input[], uint8_t length);
  
private:
  bool finalized;
  uint32_t state[4];
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
  uint32_t rotateLeft(uint32_t x, uint32_t n);
  void transform(const uint8_t block[blocksize]);

  void decode(uint32_t output[], const uint8_t input[], uint32_t len);
  void encode(uint8_t output[], const uint32_t input[], uint32_t len);

//  std::string md5(const std::string str);
};

#endif /* md5_hpp */
