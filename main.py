import os

class Cauculator:
    def __init__(self) -> None:
        self.AVE: float = 0
        self.CR: float = 0
    
    def input(self, data: list[float]) -> None:
        self.AVE = sum([n**2 for n in data]) / len(data)
        self.CR = sum(data)**2 / ( sum(data)**2 + sum([1 - n**2 for n in data]) )
    
    def ave(self) -> float: return self.AVE

    def cr(self) -> float: return self.CR

class Interface:
    def __init__(self) -> None:
        self.caulculator = Cauculator()
        self.data: list[float] = []
        self.results: list[tuple[float,float]] = []
        self.input()
        with open("last_results.txt", "w") as f:
            f.write('AVE\tCR\n')
            for n in self.results: f.write(f"{n[0]}\t{n[1]}\n")
        print("===== GOOD BYE! =====")
    
    def output(self) -> None:
        print("=====RESULT=====")
        self.caulculator.input(self.data)
        print(f"AVE : {self.caulculator.ave()}")
        print(f"CR : {self.caulculator.cr()}")
        self.results.append((self.caulculator.ave(), self.caulculator.cr()))
        print("=====RESULT=====")
        input("Press Enter to continue...")
    
    def input(self):
        print("=====Start Loop=====")
        en = "Enter your data (float number), splited by space.\nEnter 'file' or 'f' to load data from file.\nEnter 'quit' or 'q' to quit."
        zh = "输入数据（浮点数），以空格分隔。\n输入 'file' 或 'f' 从文件加载数据。\n输入 'quit' 或 'q' 退出。"
        cmd = input(f"{en}\n{zh}\ndata : > ")
        if cmd == "file" or cmd == "f":
            en = "Enter the path (abs/rel) of your file. With extension name."
            zh = "输入文件路径（绝对/相对）。带扩展名。"
            name = input(f"{en}\n{zh}\nfile_name : > ")
            if not os.path.exists(name):
                print("File not found!")
            else:
                with open(f"{name}", "r") as f: data = f.read().split()
                self.data = [float(n) for n in data]
                self.output()
        elif cmd == "quit" or cmd == "q": return
        else:
            try:
                self.data = [float(n) for n in cmd.split(" ")]
                self.output()
            except:
                print("Invalid input!")
        print("=====Ended Loop=====")
        self.input()

if __name__ == "__main__":
    Interface()