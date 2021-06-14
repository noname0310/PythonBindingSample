#xorshift method https://en.wikipedia.org/wiki/Xorshift
class fastrand:
    def __init__(self):
        self.rctr = 0x01234567
        self.x = 0x000069649
        self.y = 0x269553665
        self.z = 0x016781328
        self.i0 = 0x55555555
        self.i1 = 0x242218098
        self.i2 = 0x007276769
        self.i3 = 0x034465708
    def rand(self):
        self.rctr  = self.rctr % 0xFFFFFFFF
        self.rctr ^= 0xAAAAAAAA

        self.x ^= self.i0
        self.y ^= self.x
        self.z ^= self.y

        self.x ^= self.i1
        self.y ^= self.i2
        self.z ^= self.i3

        self.rctr ^= 0xFFFFFFFF
        self.rctr ^= (self.rctr << 13)
        self.rctr ^= self.x
        self.x ^= self.y
        self.rctr ^= (self.rctr >> 7)
        self.rctr ^= self.y
        self.y ^= self.z
        self.rctr ^= (self.rctr << 17)
        self.rctr ^= self.z
        self.z ^= self.x

        return float(self.rctr % 0xFFFFFFFF)/0xFFFFFFFF

def mc_pi(acc: int) -> float:  
    rng = fastrand()
    hit_count: int = 0
    count: int = 0
    for _ in range(0, acc):
        x: float = rng.rand()
        y: float = rng.rand()
        if x * x + y * y <= 1. :
            hit_count += 1
        count += 1
        
    return float(hit_count) / float(count) * 4.0
