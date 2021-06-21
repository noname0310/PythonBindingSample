import clr
import mc_pi_rust
import mc_pi_csharp
import mc_pi_python
import ctypes
import time
import matplotlib.pyplot as plt
clr.AddReference("D:/noname/Projects/GitHub/PythonBindingSample/mc_pi_csharp_df/bin/Release/mc_pi_csharp_df.dll")
import mc_pi_csharp_df
def logging_time(fn):
    start_time = time.time()
    result = fn()
    end_time = time.time()
    return (result, int((end_time - start_time) * 1000))

def main():
    elapsedtimes = []
    iterations = 100000
    print(f"iteration count: {iterations}")

    (result, time) = logging_time(lambda: mc_pi_python.mc_pi(iterations))
    print(f"mc_pi_python: {time} ms, PI={result}")
    elapsedtimes.append((time, "python"))
    
    #(result, time) = logging_time(lambda: mc_pi_rust.mc_pi(iterations))
    print(f"mc_pi_rust: {time} ms, PI={result}")
    elapsedtimes.append((time, "rust"))

    (result, time) = logging_time(lambda: mc_pi_csharp_df.McpiCsharp.Mcpi(iterations))
    print(f"mc_pi_csharp: {time} ms, PI={result}")
    elapsedtimes.append((time, "csharp"))

    elapsedtimes.sort()
    plt.bar(range(len(elapsedtimes)), [x[0] for x in elapsedtimes])
    ax = plt.subplot()
    ax.set_xticks(range(len(elapsedtimes)))
    ax.set_xticklabels([x[1] for x in elapsedtimes])
    plt.title(f"Monte Carlo Method PI Compute Benchmark\nIteration Count: {iterations}")
    plt.xlabel("language")
    plt.ylabel("elapsed time(ms)\nlower is better")
    plt.show()

if __name__ == '__main__':
    main()
