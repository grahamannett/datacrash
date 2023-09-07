class Plugin:
    def process(cls, dataclass):
        return dataclass

    # def __post_init__(self):
    #     self.pre_post_init()
    #     super().__post_init__()
    #     self.on_post_init()

    def on_pre_post_init(self):
        pass

    def on_post_init(self):
        pass

    def on_change(self, key, val):
        pass
