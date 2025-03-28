import matplotlib.pyplot as plt

def plot_results(pandas_time, fireducks_time):
    tools = ['Pandas', 'FireDucks']
    times = [pandas_time, fireducks_time]
    
    plt.bar(tools, times, color=['red', 'green'])
    plt.title('Data Loading Speed Comparison')
    plt.ylabel('Time (seconds)')
    plt.savefig('images/loading_speed.png')
    plt.show()

if __name__ == "__main__":
    # Replace with your actual benchmark times
    pandas_time = 142.7
    fireducks_time = 12.3
    plot_results(pandas_time, fireducks_time)