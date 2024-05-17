class UUIDgen:
    def __init__(self) -> None:
        self.start_sequence = 0


    def gen_uuid(self) -> str:
        self.start_sequence += 1
        return self.start_sequence.__str__()


uuid_gen = UUIDgen()
