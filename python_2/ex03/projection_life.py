import matplotlib.pyplot as plt
from load_csv import load
import matplotlib.ticker as ticker


def format_k(x, pos):
    """Convertit les valeurs >= 1000 en k"""
    if x >= 1000:
        return f"{int(x/1000)}k"
    else:
        return f"{int(x)}"


def main():
    """Programme qui genere un graph comparant l'esperance de vie avec le PIB
    de chaque pays pour l'année 1900"""
    try:
        df_life = load("life_expectancy_years.csv")
        df_income = load("income_per_person_gdppercapita_ppp_\
inflation_adjusted.csv")
        df_life = df_life.loc[:, '1900']
        df_income = df_income.loc[:, '1900']
        df_life = df_life.T
        df_income = df_income.T
        plt.scatter(df_income, df_life, color='r', s=25)
        plt.xscale("log")
        plt.xlim(300, 10000)
        plt.gca().xaxis.set_major_locator(
            ticker.FixedLocator([300, 1000, 10000]))
        plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format_k))
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy")
        plt.show()
    except Exception as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("KeyboardInterrupt: a signal has been catched")


if __name__ == "__main__":
    main()
