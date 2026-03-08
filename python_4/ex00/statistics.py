def ft_statistics(*args: any, **kwargs: any) -> None:
    try:
        assert len(args) > 0 and len(kwargs) > 0, "ERROR"

        for val in kwargs.values():
            if (val == "mean"):
                mean = sum(args) / len(args)
                print(f"mean : {mean}")
            elif (val == "median"):
                median = sorted(args)
                print(f"median : \
{int((median[len(median) // 2] + median[~len(median) // 2]) / 2)}")
            elif (val == "quartile"):
                sorted_list = sorted(args)
                first_quart = sorted_list[: len(sorted_list) // 2 + 1]
                third_quart = sorted_list[len(sorted_list) // 2:]
                if ((len(first_quart) // 2) % 2 == 0):
                    q1 = float((first_quart[len(first_quart) // 2] +
                                first_quart[len(first_quart) // 2 - 1]) / 2)
                else:
                    q1 = float((first_quart[len(first_quart) // 2]) / 2)
                if ((len(third_quart) // 2) % 2 == 0):
                    q3 = float((third_quart[len(third_quart) // 2] +
                                third_quart[len(third_quart) // 2 - 1]) / 2)
                else:
                    q3 = float((third_quart[len(third_quart) // 2]) / 2)
                print(f"quartile : [{q1}, {q3}]")

    except Exception as error:
        print(error)
