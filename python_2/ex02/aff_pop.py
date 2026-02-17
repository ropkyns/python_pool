import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def main():
    try:
        df = load("population_total.csv")
        fr_df = df.loc[df['country'].isin(['France', 'Portugal'])]
        fr_df = fr_df.loc[:, '1800':'2050']
        fr_df = fr_df.replace({'K': 'e3', 'M': 'e6', 'B': 'e9'}, regex=True)
        fr_df = fr_df.apply(pd.to_numeric, errors='coerce')
        fr_df = fr_df.T
        fr_df.plot()
        plt.title("Populations Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend(['France', 'Portugal'])
        plt.show()
    except Exception as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("KeyboardInterrupt: a signal has been catched")


if __name__ == "__main__":
    main()
