import pandas as pd

df = pd.read_csv("TrabajoFinal/airbnb.csv")

# ======================
# Caso 1 (Alicia)
# ======================
alicia_cols = ["room_id", "neighborhood", "room_type", "bedrooms",
               "accommodates", "price", "reviews", "overall_satisfaction"]

alicia = (
    df.query("bedrooms >= 2 and reviews > 10 and overall_satisfaction > 4")
      .sort_values(by=["overall_satisfaction", "reviews"],
                   ascending=[False, False])
      .head(3)
      .loc[:, [c for c in alicia_cols if c in df.columns]]
)

print("\n=== Caso 1: 3 alternativas para Alicia ===")
print(alicia)


# ======================
# Caso 2 (Roberto vs Clara)
# ======================
ids_rc = [97503, 90387]
roberto_clara = df[df["room_id"].isin(ids_rc)].copy()

roberto_clara.to_excel("roberto.xlsx", index=False)

print("\n=== Caso 2: Propiedades de Roberto y Clara ===")
print(roberto_clara)


# ======================
# Caso 3 (Diana)
# ======================
diana_cols = ["room_id", "room_type", "neighborhood",
              "price", "overall_satisfaction", "reviews"]

diana = df[df["price"] <= 50].copy()
diana["shared_first"] = diana["room_type"].ne("Shared room")

diana = (
    diana.sort_values(by=["shared_first", "price", "overall_satisfaction"],
                      ascending=[True, True, False])
         .head(10)
         .loc[:, [c for c in diana_cols if c in df.columns]]
)

print("\n=== Caso 3: 10 opciones para Diana (presupuesto ≤ 50€, Shared primero) ===")
print(diana)
