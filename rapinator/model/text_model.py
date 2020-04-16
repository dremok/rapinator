import gpt_2_simple as gpt2


class GPT2:
    def __init__(self):
        self.tf_session = gpt2.start_tf_sess()
        gpt2.load_gpt2(self.tf_session)
        print('Done!')

    def sample(self, model_input: str) -> str:
        return gpt2.generate(self.tf_session, temperature=0.9, top_k=70, prefix=model_input, return_as_list=True)[0]
