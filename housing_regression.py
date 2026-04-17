import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def run_model():
    data = load_boston()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['PRICE'] = data.target

    X = df[['RM']]
    y = df['PRICE']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("MSE:", mean_squared_error(y_test, y_pred))
    print("R2 Score:", r2_score(y_test, y_pred))

    plt.scatter(X_test, y_test)
    plt.plot(X_test, y_pred)
    plt.xlabel("RM")
    plt.ylabel("Price")
    plt.show()

if __name__ == "__main__":
    run_model()
