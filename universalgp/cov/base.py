"""Base class of covariance functions"""
import tensorflow as tf

class Covariance(tf.keras.layers.Layer):
    """Base class of covariance functions"""
    def __init__(self, args, **kwargs):
        """
        Args:
            args: dictionary with parameters
        """
        self.args = args
        super().__init__(**kwargs)

    def get_config(self):
        base_config = super().get_config()
        base_config['args'] = self.args
        return base_config

    @classmethod
    def from_config(cls, config):
        return cls(**config)
