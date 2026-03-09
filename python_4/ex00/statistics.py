def ft_statistics(*args: any, **kwargs: any) -> None:
    for val in kwargs.values():
        try:
            if (val == "mean"):
                assert len(args) > 0 and len(kwargs) > 0, "ERROR"
                mean = sum(args) / len(args)
                print(f"mean : {mean}")
            elif (val == "median"):
                assert len(args) > 0 and len(kwargs) > 0, "ERROR"
                median = sorted(args)
                print(f"median : \
{int((median[len(median) // 2] + median[~len(median) // 2]) / 2)}")
            elif (val == "quartile"):
                assert len(args) > 0 and len(kwargs) > 0, "ERROR"
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
            elif (val == "std"):
                assert len(args) > 0 and len(kwargs) > 0, "ERROR"
                std_var = sum(pow(x - sum(args) / len(args), 2) for x in args)\
                    / len(args)
                std = std_var ** 0.5
                print(f"std : {std}")
            elif (val == "var"):
                assert len(args) > 0 and len(kwargs) > 0, "ERROR"
                var = sum(pow(x - sum(args) / len(args), 2) for x in args)\
                    / len(args)
                print(f"var : {var}")
        except Exception as error:
            print(error)
            continue
