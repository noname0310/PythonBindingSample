namespace mc_pi_csharp_df
{
    public class McpiCsharp
    {
        private struct Fastrand
        {
            private ulong _rctr;
            public void SplitMix64(ulong seed = 0x956126898) => _rctr = seed;
            public double Rand()
            {
                _rctr %= 0xFFFFFFFF;
                _rctr ^= _rctr << 13;
                _rctr %= 0xFFFFFFFF;
                _rctr ^= _rctr >> 7;
                _rctr %= 0xFFFFFFFF;
                _rctr ^= _rctr << 17;
                _rctr %= 0xFFFFFFFF;
                return (float)(_rctr % 0xFFFFFFFF) / 0xFFFFFFFF;
            }
        }

        public static double Mcpi(int acc)
        {
            var rng = new Fastrand();
            rng.SplitMix64();
            var hitCount = 0;
            var count = 0;
            for (var i = 0; i < acc; i++)
            {
                var x = rng.Rand();
                var y = rng.Rand();
                if (x * x + y * y <= 1.0)
                {
                    hitCount += 1;
                }
                count += 1;
            }

            return (float)hitCount / count * 4.0;
        }
    }
}
