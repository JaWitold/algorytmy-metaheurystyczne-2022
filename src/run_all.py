import os

main = os.getcwd()
tsp = "../vendors/ALL_tsp"
atsp = "../vendors/ALL_atsp"

fails = ''


def run(path, ending):
    # runs only on Windows
    os.chdir(path)
    cwd = os.getcwd()
    
    list = [x for x in os.listdir(cwd) if x.endswith(ending)]
    index = 0
    
    for directory in list:
        index += 1
        os.chdir(directory)
        cwd = os.getcwd()
        command = "python.exe " + main + "\\main.py " + cwd + '\\' + os.listdir(cwd)[0]
        print(f"finished {round(index / len(list) * 100)}%, ({index}/{len(list)})")
        result = os.system(command)
        # if result != 0:
        print(command)
        os.chdir('..')
    
    print(list)


run(tsp, ".tsp")
run(atsp, ".atsp")
