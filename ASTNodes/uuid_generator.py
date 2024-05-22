class UUIDgen:
    def __init__(self) -> None:
        self.start_sequence = 0


    def gen_uuid(self) -> str:
        self.start_sequence += 1
        return self.start_sequence.__str__()
    
    def gen_label(self, prefix: str) -> str:
        return f"{prefix}{self.gen_uuid()}"


uuid_gen = UUIDgen()
