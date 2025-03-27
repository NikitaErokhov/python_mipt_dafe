import math
# import pathlib
import sys

from typing import Callable, Optional

from random import randint
# from utils import read_floats_from_bytes
from utils import visualize_1d_array

sample_amount = int(1e7)                    # количество отсчетов в сигнале
sampling_period = 6 * math.pi * 1e-7         # период дискретизации
gane = 10                                   # коэффициент усиления
threshold = 4                               # порог
eps = 1e-6                                  # точность


def modulate(signal: float) -> float:
    return math.exp(-0.1 * signal)


def get_signal(
    sampling_period: float,
    sample_amount: int,
    modulation: Optional[Callable[[float], float]] = None,
) -> list[float]:
    signal = []
    for i in range(sample_amount):
        x = sampling_period*i
        signal.append(math.sin(x)*modulation(x))
    return signal


def amplify_signal(
    signal: list[float],
    gane: float,
) -> list[float]:
    new_signal = []
    for i in range(len(signal)):
        new_signal.append(signal[i]*gane)
    return new_signal


def clip_signal(
    signal: list[float],
    threshold: float,
) -> list[float]:
    cutted_signal = []
    for i in range(len(signal)):
        if abs(signal[i]) <= threshold:
            cutted_signal.append(signal[i])
        else:
            cutted_signal.append(threshold*(abs(signal[i])/signal[i]))
    return cutted_signal


signal = get_signal(sampling_period, sample_amount, modulate)
signal_amplified = amplify_signal(signal, gane)
signal_clipped = clip_signal(signal_amplified, threshold)

print(f"signal size: {sys.getsizeof(signal)} bytes")

assert signal is not signal_amplified
assert signal_amplified is not signal_clipped


visualize_1d_array(ordinate=signal_clipped)


columns_amount = 1000           # число колонок в матрице для тестирования
rows_amount = 500               # число строк в матрице для тестирования

bottom = -10                    # нижняя граница значений чисел в матрице
top = 10                        # верхняя граница значений чисел в матрице


class ShapeMismatchError(Exception):
    """Возбуждается, если матрицы не могут быть перемножены."""


def multiply_matrices(
    lhs: list[list[float]],
    rhs: list[list[float]],
) -> list[list[float]]:
    # в матрице n строк и m столбцов
    n_lhs = len(lhs)
    m_lhs = len(lhs[0])
    n_rhs = len(rhs)
    m_rhs = len(rhs[0])
    if m_lhs != n_rhs:
        raise ShapeMismatchError("матрицы не могут быть перемножены")
    result = []
    for i in range(n_lhs):
        result += [[0]*m_rhs]
    for i in range(n_lhs):
        for j in range(m_rhs):
            for k in range(m_lhs):
                result[i][j] += lhs[i][k]*rhs[k][j]
    return result


lhs = [
    [7, -1, -4],
    [-1, 5, -1],
]
rhs = [
    [-2, -5],
    [-5, -6],
    [-5, 3],
]
reference = [
    [11, -41],
    [-18, -28]
]

result = multiply_matrices(lhs, rhs)

assert all(
    all(
        num_res == num_ref
        for num_res, num_ref in zip(row_res, row_ref)
    )
    for row_res, row_ref in zip(result, reference)
)

was_raised = False

try:
    result = multiply_matrices(lhs, rhs[:2])

except ShapeMismatchError:
    was_raised = True

assert was_raised

# %%timeit -r 1 -n 1
lhs = [
    [randint(bottom, top) for _ in range(columns_amount)]
    for _ in range(rows_amount)
]

rhs = [
    [randint(bottom, top) for _ in range(rows_amount)]
    for _ in range(columns_amount)
]

result = multiply_matrices(lhs, rhs)

del lhs
del rhs
del result
