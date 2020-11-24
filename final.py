import matplotlib.axes, matplotlib.figure, matplotlib.pyplot as plt
from matplotlib.pyplot import figure
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
    plt.plot(data[:, 1],'o', color='blue')
    plt.title("Dividends vs Earnings")
    plt.show()
    #Need to make the X-Axis display the year


def figure2(data):
    plt.plot(data[:, 2],'o', color='blue')
    plt.plot(data[:, 3],'o', color='red')
    plt.xlabel("Year")
    plt.ylabel("S & P 500")
    plt.title("S & P 500")
    plt.show()


def figure3(data):
    plt.plot(data[:, 2],'o', color='blue')
    plt.plot(data[:, 7],'o', color='red')
    plt.title("Dividends vs Real Dividends")
    plt.show()


def figure4(data):
    plt.plot(data[:, 3],'o', color='blue')
    plt.plot(data[:, 8],'o', color='red')
    plt.title("Earnings vs Real Earnings")
    plt.show()


def figure5(data):
    plt.plot((data[:, 3])/(data[:, 7]),'o', color='pink')
    plt.title("Earnings per SP500")
    plt.show()


if __name__ == "__main__":
    main()
    