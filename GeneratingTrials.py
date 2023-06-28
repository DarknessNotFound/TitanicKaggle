import csv

# Trail format: ([layers], [# of nodes])
OUTPUT_FILE = "trials.csv"
def WriteTrials(trials: list):
    with open(OUTPUT_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        for trial in trials:
            writer.writerow(trial[0])
            writer.writerow(trial[1])

def main():
    trials = []
    for a in range(128, 512, 16):
        first_layer = int(a)
        for b in range(16, 256, 16):
            second_layer = int(b)
            for c in range(8, 16, 2):
                third_layer = int(b / 4)

                layers = ["linear", "relu", "relu"]
                nodes = [first_layer, second_layer, third_layer]
                trials.append((layers, nodes))
    print(trials)
    WriteTrials(trials)

if __name__ == "__main__":
    main()