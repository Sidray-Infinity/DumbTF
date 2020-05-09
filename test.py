from keras.datasets import boston_housing
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import normalize
from sklearn.metrics import mean_squared_error, mean_absolute_error

if __name__ == "__main__":
    (train_x, train_y), (test_x, test_y) = boston_housing.load_data()

    train_x = normalize(train_x)
    test_x = normalize(test_x)

    model = Sequential()
    model.add(Dense(64, input_shape=(train_x.shape[1], ),
                    activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1))

    model.compile(optimizer="SGD", loss="mse",
                  metrics=['mae'])

    model.fit(train_x, train_y, epochs=80, batch_size=16)

    pred = model.predict(test_x)

    print(mean_squared_error(test_y, pred))
    print(mean_absolute_error(test_y, pred))
