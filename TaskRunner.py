

class TaskRunner:
    @staticmethod
    def executeTask(files: list[str]):
        for path in files:
            print(f"currently running : {path}")
            with open(path) as file:
                content = file.read()
                exec(content)
