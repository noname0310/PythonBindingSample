using System.Runtime.InteropServices;
using RGiesecke.DllExport;

namespace mc_pi_csharp
{
    public class McpiCsharp
    {
        private class Fastrand
        {
            private ulong _rctr;
            public Fastrand() => _rctr = 0x956126898;
            public void SplitMix64(ulong seed) => _rctr = seed;
            public double Rand()
            {
                _rctr %= 0xFFFFFFFF;
                _rctr ^= _rctr << 13;
                _rctr %= 0xFFFFFFFF;
                _rctr ^= _rctr >> 7;
                _rctr %= 0xFFFFFFFF;
                _rctr ^= _rctr << 17;
                _rctr %= 0xFFFFFFFF;
                return (float) (_rctr % 0xFFFFFFFF) / 0xFFFFFFFF;
            }
        }

        [DllExport("mc_pi", CallingConvention.Cdecl)]
        public static double Mcpi(int acc)
        {
            var rng = new Fastrand();
            var hitCount = 0;
            var count = 0;
            for (var i = 0; i < acc; i++)
            {
                var x = rng.Rand();
                var y = rng.Rand();
                if (x * x + y * y <= 1.0) {
                    hitCount += 1;
                }
                count += 1;
            }

            return (float)hitCount / count * 4.0;
        }
    }
}
