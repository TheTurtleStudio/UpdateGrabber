import pathlib
imports_list = ['subprocess','handler', 'psutil','sys','pathlib']
settingsLocation = pathlib.Path("settings.txt") #Direct path to settings.txt

def update(repo=None, user=None, branch=None, globalPath=None, settings=settingsLocation):
    try:
        for i in globals()['imports_list']:
            exec(f"import {i}")
        reverse = str(locals()['handler'])[::-1]
        handlerPath = locals()['pathlib'].Path(reverse[reverse.find('\'')+1:reverse[reverse.find('\'')+1:].find('\'')+reverse.find('\'')+1][::-1])
        locals()['subprocess'].Popen(['py', f"-{locals()['sys'].version_info.major}", str(handlerPath), str(repo), str(user), str(branch), str(globalPath), "update", str(locals()['psutil'].Process().pid), str(settings)])
        exit()
    except Exception as error:
        return f"{type(error)}: {error}"
input("")
