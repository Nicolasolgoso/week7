import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

data = {
"Jugadores": [Ramos, Casillas, Marcelo, Ronaldo, Boateng],
"Veces": [ 2, 4, 6, 8, 10, 12]
}
df = pd.DataFrame(data)

sns.lineplot( data=df, x = "Jugadores", y = "Veces")
plt.xlabel("Jugadores")
plt.ylabel("Veces")
plt.title("Comparacion de veces que messi ha humillado a distintos jugadores")
plt.show()