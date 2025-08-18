class Simulator:
    def __init__(self): self.pos=0
    def connect(self): pass
    def send_command(self, cmd):
        if cmd.startswith("L"): self.pos-=int(cmd[1:])
        elif cmd.startswith("R"): self.pos+=int(cmd[1:])
        print(f"[SIM] {cmd} -> pos={self.pos}")
        return "OK"
    def close(self): pass
