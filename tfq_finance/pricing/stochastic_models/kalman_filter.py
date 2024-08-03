import tensorflow as tf
import tensorflow_quantum as tfq
import cirq
import sympy
import numpy as np

def kalman_filter(Y, A, C, Q, R, x0, P0):
    N = len(Y)
    n = x0.shape[0]
    x_est = np.zeros((N, n))
    P_est = np.zeros((N, n, n))
    x_pred = x0
    P_pred = P0
    for t in range(N):
        K = P_pred @ C.T @ np.linalg.inv(C @ P_pred @ C.T + R)
        x_pred = x_pred + K @ (Y[t] - C @ x_pred)
        P_pred = (np.eye(n) - K @ C) @ P_pred
        x_est[t] = x_pred
        P_est[t] = P_pred
        if t < N - 1:
            x_pred = A @ x_pred
            P_pred = A @ P_pred @ A.T + Q
    return x_est, P_est