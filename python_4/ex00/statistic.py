def ft_statistics(*args: Any, **kwargs: Any) -> None:
    try:
        assert len(args) > 0 and len(kwargs) > 0, "ERROR"

        for val in kwargs.values:
            if (val == "mean"):
                mean = sum(args) / len(args)
            elif (val == "median"):
                if (len(args) / 2 == 0):
                    median = args[(len(args) + 1) / 2]
                else:
                    median = (args[(len(args) + 1) / 2] + args[(len(args) + 1) / 2]) / 2

        print(f"mean = {mean}")
        print(f"median = {median}")

    except Exception as error:
        print(error)
