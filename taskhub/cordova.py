import matplotlib.pyplot as plt
import random

def plot_fake_chem_reactions():
    reactions = [
        "H₂ + O₂ → H₂O",
        "Na + Cl → NaCl",
        "C + O₂ → CO₂",
        "Fe + O₂ → Fe₂O₃"
    ]

    energy = [random.randint(-500, -100) for _ in reactions] 

    plt.bar(reactions, energy, color="turquoise")
    plt.title("Reaction Energy Chart")
    plt.ylabel("Energy Released (kJ/mol)")
    plt.xlabel("Reaction")
    plt.xticks(rotation=15)
    plt.axhline(0, color='gray', linewidth=0.8)  
    plt.tight_layout()
    plt.show()
