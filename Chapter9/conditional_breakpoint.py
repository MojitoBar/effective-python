#!/usr/bin/env python3.8
# conditional_breakpoint.py
import math
def compute_rmse(observed, ideal):
    total_err_2 = 0
    count = 0
    for got, wanted in zip(observed, ideal):
        err_2 = (got - wanted) ** 2
        if err_2 >= 1: # True인 경우에만 디버거를 실행함
            breakpoint()
        total_err_2 += err_2
        count += 1
    mean_err = total_err_2 / count
    rmse = math.sqrt(mean_err)
    return rmse

result = compute_rmse(
    [1.8, 1.7, 3.2, 7],
    [2, 1.5, 3, 5])
print(result)
