import numpy as np
import matplotlib.pyplot as plt 

n_trys= 137000
p = 1/137000
target_prob = 0.99
n_99 = np.log(1-target_prob)/np.log(1-p)
current_prob_success = 1-(1-p)**n_trys

x_range = np.linspace(0, n_99 * 1.1 , 1000)
y_range = (1-(1-p) ** x_range) * 100

plt.plot(x_range, y_range, label="Kumulative Wahrscheinlichkeit (%)", color="blue")

# Deinen aktuellen Standpunkt als roten Punkt einzeichnen
plt.scatter(
    [n_trys],
    [current_prob_success * 100],
    color="red",
    s=100,
    zorder=5,
    label=f"Du bist hier ({n_trys:,} Tries)",
)

n_simulations = 10000000

results = np.random.binomial(n=n_trys, p=p, size=(n_simulations))
successes = np.sum(results > 0) 
simulated_prob = (successes / n_simulations) * 100
print(f"Simulierte Wahrscheinlichkeit, den Pirate Token in {n_trys} Versuchen zu ziehen: {simulated_prob:.2f}%")


# Hilfslinien & Beschriftungen
plt.axhline(50, color="gray", linestyle="--", alpha=0.6, label="50% Chance (Median)")
plt.title("Wahrscheinlichkeit, den Pirate Token zu ziehen")
plt.xlabel("Anzahl Versuche (Tries)")
plt.ylabel("Wahrscheinlichkeit (%)")
plt.grid(True)
plt.legend()
plt.show()

