import matplotlib.pyplot as plt
from load_csv import load


def main():
    try:
        df = load("life_expectancy_years.csv")
        fr_df = df.loc[df['country'] == 'France']
        fr_df = fr_df.drop(columns="country").T
        fr_df.plot()
        plt.title("France Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()
    except Exception as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("KeyboardInterrupt: a signal has been catched")


if __name__ == "__main__":
    main()
