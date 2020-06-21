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


class StaticModel(object):
    def sample(self, model_input: str) -> str:
        return """<<Bizzy Bone - Enduring Fantasy>>
[Verse 1: Bizzy Bone]
And now the music's getting pushed around
And now it all hits me

And now they all wish they had me

And now it's all the same, but the end is here

It's the same end, so you can feel my music

I'm with the same crowd so I think I'm done with this party

We're gonna keep it alive and never let it die

We're gonna keep it alive and never let it die

I'm gonna keep my foot on the gas and let the world know

We're gonna keep it alive and never let it die



[Refrain: Bizzy Bone]

'Cause we're gonna keep it alive and never let it die

We're gonna keep it alive and never let it die

And we're gonna keep it alive and never let it die



[Verse 2: Bizzy Bone]

And now everything and everyone

And every other word, it's the same ending

If you don't want it with me, then suck my dick

I will make you feel the same, it's just a different ending

No I ain't new to this, I won't change anything

I will just keep it true, the word is bond

I will not just let it roll up and swallow me

That's why I'm telling you this is the end for me

And if I can't win, then you will lose

You will be just like me, then I'll be like you

That's what I'm thinking

That's the world is yours, that is what I'm thinking

I'm pulling all the cards out of you

You will learn no new tricks



[Refrain: Bizzy Bone]

'Cause we're gonna keep it alive and never let it die

We're gonna keep it alive and never let it die

And keep on winning, keep on winning



[Bridge: Bizzy Bone]

And we still winning, keep on winning

But you can keep on winning, keep on winning

Because we're gonna keep it alive and never let it die

We're gonna keep it alive and never let it die

And keep on winning, keep on winning

Keeping on winning, keeping on winning



[Verse 3: Bizzy Bone]

That's why I'm telling you this is the end of the road

I'm a bad person, I don't want to be this way

I don't like your attitude, I think it's crazy

I just want to stay out of your business

And you know that good fucking shit right?

And you know you're a bad person, so

I ain't going in any more

I ain't going in your business any more

And you know that good fucking shit right?

I got a bad person inside of me

That bad person inside of me

That bad person inside of me

That bad person inside of me



[Refrain: Bizzy Bone]

'Cause we're gonna keep it alive and never let it die

We're gonna keep it alive and never let it die

And keep on winning, keep on winning

Keep on winning, keep on winning



[Outro: Bizzy Bone]
Oh
*************************************************
"""
