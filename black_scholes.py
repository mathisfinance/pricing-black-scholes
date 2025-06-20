import math
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    """
    Calcule le prix d'une option européenne avec le modèle Black-Scholes.
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == "call":
        price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type doit être 'call' ou 'put'.")

    return price

# Exemple d'utilisation
if __name__ == "__main__":
    S = 100     # Prix actuel de l'actif
    K = 100     # Prix d'exercice
    T = 1       # Temps jusqu'à échéance (en années)
    r = 0.05    # Taux sans risque
    sigma = 0.2 # Volatilité
    option_type = "call"

    price = black_scholes_price(S, K, T, r, sigma, option_type)
    print(f"Prix de l'option {option_type} : {price:.2f} €")
