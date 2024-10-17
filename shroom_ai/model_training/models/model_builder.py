from tensorflow.keras.applications import ResNet50V2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from config import config

def build_model():
    base_model = ResNet50V2(weights='imagenet', include_top=False, input_shape=(*config.IMAGE_SIZE, 3))
    
    for layer in base_model.layers:
        layer.trainable = False
    
    x = GlobalAveragePooling2D()(base_model.output)
    x = Dense(config.DENSE_UNITS, activation='relu')(x)
    output = Dense(1, activation='sigmoid')(x)
    
    model = Model(inputs=base_model.input, outputs=output)
    
    model.compile(optimizer=Adam(learning_rate=config.LEARNING_RATE),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    return model