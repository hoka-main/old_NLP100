def wether(time, C, cc):
    exit_str = f"{time}時の{C}は{cc}℃である"
    return exit_str


to_use = wether(12, '気温', 22.4)

print(to_use)
