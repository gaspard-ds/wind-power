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


TO_KEEP_PRODUCTION = [
    "Code INSEE région",
    "Région",
    "Nature",
    "Date",
    "Heure",
    "Date - Heure",
    "Consommation (MW)",
    "Eolien (MW)",
    "TCO Eolien (%)",
    "TCH Eolien (%)",
]

TO_KEEP_WEATHER = [
    "ID OMM station",
    "Date",
    "Pression au niveau mer",
    "Variation de pression en 3 heures",
    "Direction du vent moyen 10 mn",
    "Vitesse du vent moyen 10 mn",
    "Température",
    "Pression station",
    "Niveau barométrique",
    "Variation de pression en 24 heures",
    "Température du thermomètre mouillé",
    "Rafale sur les 10 dernières minutes",
    "Rafales sur une période",
    "Periode de mesure de la rafale",
    "Altitude",
    "region (name)",
    "region (code)",
    "mois_de_l_annee",
]

FEATURES = [
    "speed",
    "direction",
    "temperature",
    "pressure",
    "gust",
    "speed_11",
    "direction_11",
    "speed_24",
    "direction_24",
    "speed_27",
    "direction_27",
    "speed_28",
    "direction_28",
    "speed_32",
    "direction_32",
    "speed_44",
    "direction_44",
    "speed_52",
    "direction_52",
    "speed_53",
    "direction_53",
    "speed_75",
    "direction_75",
    "speed_76",
    "direction_76",
    "speed_84",
    "direction_84",
    "speed_93",
    "direction_93",
    "speed_94",
    "direction_94",
    "month",
]

FEATURES_REDUCED = [
    "speed_28",
    "speed_44",
    "temperature",
    "speed_24",
    "speed",
    "pressure",
    "gust",
    "speed_11",
    "speed_32",
    "speed_53",
    "speed_75",
    "speed_76",
    "speed_94",
    "direction_94",
]

FEATURES_GLOBAL = [
    "speed",
    "direction",
    "pressure",
    "temperature",
    "gust",
]

TARGET = "relative_production"

ALT_TARGET = "production"
ALT_FEATURES = FEATURES + ["capacity"]
