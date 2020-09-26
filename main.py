"""Main Module"""

# Plot Params
LARGE = 22
MEDIUM = 16
SMALL = 12
params = {
    "axes.titlesize": LARGE,
    "legend.fontsize": MEDIUM,
    "figure.figsize": (30, 15),
    "axes.labelsize": LARGE,
    "xtick.labelsize": MEDIUM,
    "ytick.labelsize": MEDIUM,
    "figure.titlesize": LARGE,
}

REGIONS = [
    "Auvergne-Rhône-Alpes",
    "Bourgogne-Franche-Comté",
    "Bretagne",
    "Centre-Val de Loire",
    "Corse",
    "Grand-Est",
    "Hauts-de-France",
    "Ile-de-France",
    "Normandie",
    "Nouvelle-Aquitaine",
    "Occitanie",
    "Pays de la Loire",
    "Provence-Alpes-Côte d'Azur",
]

CODE_REGIONS = {
    11: "Ile-de-France",
    24: "Centre-Val de Loire",
    27: "Bourgogne-Franche-Comté",
    28: "Normandie",
    32: "Hauts-de-France",
    44: "Grand-Est",
    52: "Pays de la Loire",
    53: "Bretagne",
    75: "Nouvelle-Aquitaine",
    76: "Occitanie",
    84: "Auvergne-Rhône-Alpes",
    93: "Provence-Alpes-Côte d'Azur",
    94: "Corse",
}
