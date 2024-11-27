import matplotlib.pyplot as plt
import numpy as np

# Data: Resolutions and times for different thread counts
resolutions = [64, 128, 256, 512, 1024]
threads = [1, 2, 4, 8, 16]
times = {
    64: [0.0629718, 0.0549711, 0.0509977, 0.0530269, 0.0826006],
    128: [0.604752, 0.353598, 0.226159, 0.199965, 0.245333],
    256: [4.34029, 2.32191, 1.24335, 0.789274, 0.670457],
    512: [33.232, 17.1841, 8.85125, 4.96217, 3.13035],
    1024: [4.67548, 2.20043, 1.30318, 0.712137, 0.699032]
}

# Plotting with log scale for time axis
plt.figure(figsize=(10, 6))
for res in resolutions:
    plt.plot(threads, times[res], marker='o', label=f'Resolution {res}x{res}')

plt.xlabel('Number of Threads (NCPU)')
plt.ylabel('Time to Solution (seconds, log scale)')
plt.yscale('log')
plt.title('Strong Scaling Performance for Different Resolutions')
plt.legend(title="Resolution")
plt.grid(True, which="both", ls="--")
plt.savefig("StrongScaling")
plt.show()
