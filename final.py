import matplotlib.axes, matplotlib.figure, matplotlib.pyplot as plt
import numpy as np, requests, io, pandas as pd

def main():
    # Retrieve dataset from Github, remove the PE10 column, and drop records with nulls.
    csv = requests.get("https://raw.githubusercontent.com/datasets/s-and-p-500/master/data/data.csv").content
    data = pd.read_csv(io.StringIO(csv.decode('utf-8'))).drop(['PE10'], axis=1).dropna().to_numpy()

    print("Record count:", data.shape[0])

    figure1(data)
    figure2(data)
    figure3(data)
    figure4(data)
    figure5(data)
            

def figure1(data):
    test = None # placeholder


def figure2(data):
    test = None # placeholder


def figure3(data):
    test = None # placeholder


def figure4(data):
    test = None # placeholder


def figure5(data):
    test = None # placeholder


if __name__ == "__main__":
    main()

"""

ax: matplotlib.axes.Axes
x = np.zeros((5, 5))
y = np.zeros(5)

fig, ax = plt.subplots()
ax.scatter(x, y)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("X vs Y")

plt.save_fig("test.png")
plt.show()

"""