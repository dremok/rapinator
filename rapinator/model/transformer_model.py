import gpt_2_simple as gpt2
import tensorflow as tf
from tensorflow.core.protobuf import rewriter_config_pb2


def start_tf_sess():
    """
    Returns a tf.Session w/ config
    """
    print('Forcing CPU...')
    config = tf.compat.v1.ConfigProto(
        device_count={'GPU': 0}
    )
    config.graph_options.rewrite_options.layout_optimizer = rewriter_config_pb2.RewriterConfig.OFF
    return tf.compat.v1.Session(config=config)


class GPT2:
    def __init__(self):
        self.tf_session = start_tf_sess()
        gpt2.load_gpt2(self.tf_session)
        print('Done!')

    def sample(self, model_input: str) -> str:
        return gpt2.generate(self.tf_session, temperature=0.9, top_k=70, prefix=model_input, return_as_list=True)[0]
