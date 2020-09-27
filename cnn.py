import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten, BatchNormalization

import pandas as pd



class CovNet:
    callback = None
    checkpoint = None
    model = None

    def __init__(self):
        self.model = Sequential([
            Conv2D(filters=64, kernel_size=3, activation='relu', input_shape=(7, 8, 8), data_format='channels_first'),
            BatchNormalization(),
            Conv2D(filters=64, kernel_size=3, activation='relu'),
            BatchNormalization(),
            Conv2D(filters=64, kernel_size=3, activation='relu'),
            Flatten(),
            Dense(3, activation='softmax')

        ])

        self.model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

        if os.path.isfile('Data/model/model_weights.h5'):
            self.model.load_weights('Data/model/model_weights.h5')

    def train(self, train_data):
        history_df = pd.DataFrame(columns=['game_count',[f'epoch_{i}' for i in range(1, 101)]]) \
            if not os.path.isfile('Data/model_progression/hist_df') \
            else pd.read_pickle('Data/model_progression/hist_df')

        history = self.model.fit(train_data, verbose=1, epochs=100)

        model_hist = history.history

        # append accuracy

        # history_df.to_pickle('Data/model_progression/hist_df')

        self.model.save_weights('Data/model/model_weights.h5')

    def predict(self, x):
        y = self.model.predict(x)

        return y[0].tolist()
