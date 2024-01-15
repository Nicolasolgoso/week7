import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

data = {
"Jugadores": ["Ramos", "Casillas", "Marcelo", "Ronaldo", "Boateng"],
"Veces": [ 8, 4, 7, 2, 5,]
}
df = pd.DataFrame(data)

sns.lineplot( data=df, x = "Jugadores", y = "Veces")
plt.xlabel("Jugadores")
plt.ylabel("Veces")
plt.title("Comparacion de veces que messi ha humillado a distintos jugadores")
plt.show()