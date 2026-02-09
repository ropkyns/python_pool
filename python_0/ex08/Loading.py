import os


def ft_tqdm(lst: range) -> None:  #type: ignore
    time = os.times().elapsed
    total = len(lst)
    size = os.get_terminal_size().columns
    for i, x in enumerate(lst, 1):
        elapsed = os.times().elapsed - time
        progression = i / total
        speed = i / elapsed if elapsed > 0 else 0
        percent = int(progression * 100)
        status = f"{percent:3}%|| {i}/{total} [{elapsed:05.1f}s, {speed:.2f}it/s]"
        bar_size = size - len(status)
        bar = ("█" * int(bar_size * progression)) + ("░" * (bar_size - int(bar_size * progression)))

        print(f"\r{percent:3}%|{bar}| {i}/{total} [{elapsed:05.1f}s, {speed:.2f}it/s]", end='', flush=True)

        yield x


