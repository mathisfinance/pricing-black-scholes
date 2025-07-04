# Black-Scholes Option Pricing
# 📈 Black-Scholes Option Pricing

Ce projet propose une implémentation simple et pédagogique du **modèle de Black-Scholes**, utilisé en finance de marché pour calculer la valeur théorique des options européennes.

> 🔍 Ce projet fait partie de mon portfolio d’apprentissage en **finance de marché** (front office), avec pour objectif de maîtriser les outils et modèles utilisés en salle de marché.

---
# 📈 Explication

**Concrètement Pricer une option c'est quoi ?**
Pricer une option signifie déterminer sa valeur aujourd'hui. 
Une option c'est un produit financier qui permet d'acheter ou de vendre un actif (pas l'obligation), à un prix fixé à l'avance (strike) pour une date future.
**L'intérêt ?**
En sachant combien l'actif vaut, on peut prendre une décision éclairée. En reprérant les opportunités de gqin si le marché sur-évalue ou sous-évalue un actif.

En claire c'est un pari intelligent sur l'évolution futur de notre actif.
---

## 🧠 Formule Black-Scholes

Le modèle Black-Scholes permet de calculer le prix d’un **call** ou d’un **put européen** :

- **Call** :  
  `C = S × N(d₁) - K × exp(-r × T) × N(d₂)`

- **Put** :  
  `P = K × exp(-r × T) × N(-d₂) - S × N(-d₁)`

avec :

- `d₁ = [ln(S / K) + (r + σ² / 2) × T] / (σ × √T)`
- `d₂ = d₁ - σ × √T`

où :

- `S` = prix du sous-jacent  
- `K` = prix d’exercice  
- `T` = temps jusqu’à maturité (en années)  
- `r` = taux sans risque  
- `σ` = volatilité  
- `N()` = fonction de répartition de la loi normale standard

---

## 💻 Exemple d'utilisation

```bash
python black_scholes.py
