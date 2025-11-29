def compute_gcd_steps(a: int, b: int):
    """Вычисляет НОД и возвращает (gcd, steps).
    steps — список строк с пояснениями каждого шага алгоритма Евклида.
    """
    steps = []
    a0, b0 = abs(a), abs(b)
    steps.append(f"Начинаем: a = {a0}, b = {b0}")

    if a0 == 0 and b0 == 0:
        steps.append("Оба числа равны 0 — НОД не определён.")
        return None, steps

    if b0 == 0:
        steps.append(f"b = 0, поэтому НОД = {a0}")
        return a0, steps

    while b0 != 0:
        q = a0 // b0
        r = a0 % b0
        steps.append(f"{a0} = {b0} * {q} + {r}")
        a0, b0 = b0, r

    steps.append(f"Найдено: НОД = {a0}")
    return a0, steps
