import mc_pi_rust
import mc_pi_python
import time
import matplotlib.pyplot as plt

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
    
    (result, time) = logging_time(lambda: mc_pi_rust.mc_pi(iterations))
    print(f"mc_pi_rust: {time} ms, PI={result}")
    elapsedtimes.append((time, "rust"))

    elapsedtimes.sort()
    plt.bar(range(len(elapsedtimes)), [x[0] for x in elapsedtimes])
    ax = plt.subplot()
    ax.set_xticks(range(len(elapsedtimes)))
    ax.set_xticklabels([x[1] for x in elapsedtimes])
    plt.title("Monte Carlo Method PI Compute Benchmark")
    plt.xlabel("language")
    plt.ylabel("elapsed time (lowr is better)")
    plt.show()

if __name__ == '__main__':
    main()
