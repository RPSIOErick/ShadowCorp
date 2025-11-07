import random




def add_dp_noise(value: float, epsilon: float = 1.0) -> float:
# Laplace noise stub — para demonstração apenas
scale = 1.0 / epsilon
noise = random.gauss(0, scale)
return value + noise