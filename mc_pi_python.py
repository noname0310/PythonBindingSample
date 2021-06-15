#xorshift method https://en.wikipedia.org/wiki/Xorshift
class fastrand:
    def __init__(self, seed=0x956126898):
        self.rctr = seed
    def rand(self):
        self.rctr %=  0xFFFFFFFF
        self.rctr ^= (self.rctr << 13)
        self.rctr %=  0xFFFFFFFF
        self.rctr ^= (self.rctr >> 7)
        self.rctr %=  0xFFFFFFFF
        self.rctr ^= (self.rctr << 17)
        self.rctr %=  0xFFFFFFFF
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
