import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
data = {
    'Base Resolution': ['64x64', '64x64', '64x64', '64x64', '64x64',
                        '128x128', '128x128', '128x128', '128x128', '128x128',
                        '256x256', '256x256', '256x256', '256x256', '256x256'],
    'Threads (NCPU)': [1, 2, 4, 8, 16,
                       1, 2, 4, 8, 16,
                       1, 2, 4, 8, 16],
    'Time (seconds)': [0.062713, 0.095477, 0.129798, 0.200887, 0.350457,
                       0.347892, 0.500319, 0.679868, 1.003040, 1.647560,
                       2.374230, 3.356370, 4.692390, 10.648300, 21.833600]
}

# Convert data into arrays for easier manipulation
threads = np.array(data['Threads (NCPU)'])
times = np.array(data['Time (seconds)'])

# Create subplots for each base resolution
resolutions = ['64x64', '128x128', '256x256']
plt.figure(figsize=(10, 6))

for resolution in resolutions:
    mask = np.array(data['Base Resolution']) == resolution
    plt.plot(threads[mask], times[mask], marker='o', label=f'Base Resolution {resolution}')

# Set the plot title and labels
plt.title('Time to Solution vs. Number of Threads')
plt.xlabel('Number of Threads (NCPU)')
plt.ylabel('Time to Solution (seconds)')
plt.xscale('log')  # Log scale for better visualization
plt.yscale('log')  # Log scale for better visualization
plt.xticks(threads)  # Set x-ticks to be the number of threads
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()

# Show the plot
plt.savefig("WeakScaling")
plt.show()