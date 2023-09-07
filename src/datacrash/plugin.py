# since we want @datacrash above @dataclass, means modifying/changing __post_init__ wont work since it will be called
# after _process from dataclass
# 
class Plugin:
    def process(cls, dataclass):
        return dataclass

    def on_pre_post_init(self):
        pass

    def on_post_init(self):
        pass

    def on_change(self, key, val):
        pass
