import subprocess

def run_shell():
    while True:
        cmd = input("myshell> ").strip()
        if cmd == "":
            continue
        if cmd == "exit":
            break
        try:
            if "|" in cmd:
                left, right = cmd.split("|", 1)
                p1 = subprocess.Popen(left.strip().split(), stdout=subprocess.PIPE)
                p2 = subprocess.Popen(right.strip().split(), stdin=p1.stdout)
                p1.stdout.close()
                p2.communicate()
            elif ">" in cmd:
                command, filename = cmd.split(">", 1)
                with open(filename.strip(), "w") as f:
                    subprocess.run(command.strip().split(), stdout=f)
            elif "<" in cmd:
                command, filename = cmd.split("<", 1)
                with open(filename.strip(), "r") as f:
                    subprocess.run(command.strip().split(), stdin=f)
            else:
                subprocess.run(cmd.split())
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    run_shell()