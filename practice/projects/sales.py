# LSTM-based Sales Trend Analysis System

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# -------------------------------
# 1. Load & Preprocess Data
# -------------------------------
data = pd.read_csv("sales_data.csv")
data['date'] = pd.to_datetime(data['date'])
data = data.sort_values('date')

sales = data[['sales']].values

# Normalize data
scaler = MinMaxScaler(feature_range=(0, 1))
sales_scaled = scaler.fit_transform(sales)

# -------------------------------
# 2. Create Sequences for LSTM
# -------------------------------
def create_sequences(dataset, time_steps=5):
    X, y = [], []
    for i in range(len(dataset) - time_steps):
        X.append(dataset[i:i + time_steps])
        y.append(dataset[i + time_steps])
    return np.array(X), np.array(y)

TIME_STEPS = 5
X, y = create_sequences(sales_scaled, TIME_STEPS)

# Train-test split
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# -------------------------------
# 3. Build LSTM Model
# -------------------------------
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(TIME_STEPS, 1)))
model.add(LSTM(50))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

# -------------------------------
# 4. Train Model
# -------------------------------
model.fit(
    X_train,
    y_train,
    epochs=30,
    batch_size=8,
    validation_data=(X_test, y_test),
    verbose=1
)

# -------------------------------
# 5. Trend Prediction
# -------------------------------
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# Inverse scaling
train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)
y_train_actual = scaler.inverse_transform(y_train)
y_test_actual = scaler.inverse_transform(y_test)

# -------------------------------
# 6. Future Forecast (Next 10 Days)
# -------------------------------
future_steps = 10
last_sequence = sales_scaled[-TIME_STEPS:]
future_predictions = []

current_seq = last_sequence.reshape(1, TIME_STEPS, 1)

for _ in range(future_steps):
    next_value = model.predict(current_seq)[0]
    future_predictions.append(next_value)
    current_seq = np.append(current_seq[:, 1:, :], [[next_value]], axis=1)

future_predictions = scaler.inverse_transform(future_predictions)

# -------------------------------
# 7. Visualization
# -------------------------------
plt.figure(figsize=(10, 6))
plt.plot(data['date'], sales, label='Actual Sales')

# Plot test predictions
test_dates = data['date'][TIME_STEPS + train_size:]
plt.plot(test_dates, test_predict, label='LSTM Prediction')

plt.title("LSTM-Based Sales Trend Analysis")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

# -------------------------------
# 8. Forecast Output
# -------------------------------
print("Future Sales Forecast:")
for i, value in enumerate(future_predictions, 1):
    print(f"Day +{i}: {value[0]:.2f}")
