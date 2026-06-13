import numpy as np
import time

def func_lm_ls(
        func_lm_jacobian,
        func_lm_residu,
        datat,
        datay,
        itmax,
        tolmax,
        lambd,
        init):

    awal = time.perf_counter()

    # realokasi
    x = np.zeros((2, itmax))
    x[:, 0] = init

    for i in range(itmax - 1):

        # Jacobian dan residu
        Jac = func_lm_jacobian(func_lm_residu,
            datat,
            datay,
            x[0, i],
            x[1, i],
            1e-5
        )

        res = func_lm_residu(
            datat,
            datay,
            x[0, i],
            x[1, i]
        )

        # LM update
        H = Jac.T @ Jac + lambd * np.eye(2)

        L = Jac.T @ res

        delta = -np.linalg.solve(H, L)

        x[:, i + 1] = x[:, i] + delta.flatten()

        # stopping criterion
        res = func_lm_residu(
            datat,
            datay,
            x[0, i + 1],
            x[1, i + 1]
        )

        if abs(0.5 * res.T @ res) < tolmax:
            break

    iterasi = i + 1

    param = [
        x[0, iterasi],
        x[1, iterasi]
    ]

    res = func_lm_residu(
        datat,
        datay,
        x[0, iterasi],
        x[1, iterasi]
    )

    fx = 0.5 * res.T @ res

    waktu = time.perf_counter() - awal

    return iterasi, param, fx, waktu