import pathlib
settingsLocation = pathlib.Path("settings.txt") #Path to UG settings file.

class grab():
    def __init__(this, settingsFile):
        this.settings = {}
        this.settingsFile = settingsFile
        this.loadSettings("settings")
        
    def loadSettings(this, variable: str):
        try:
            with open(this.settingsFile, "r") as file:
                for line in file.readlines():
                    start = line.find("[")
                    end = -1 if (start == -1) else line[start:].find("]")
                    if start != -1 and end != -1:
                        setting = line[start+1: end]
                        name = setting[:setting.find(":")]
                        value = setting[setting.find(":")+1:]
                        exec(f"this.{variable}[\"{name}\"] = {value}\nthis.{name} = {value}")
        except Exception as error:
            return error
        
    def update(this, repo=None, user=None, branch=None, globalPath=None):
        if not repo:   repo=this.GITHUB_TARGET_REPOSITORY
        if not user:    user=this.GITHUB_USERNAME
        if not branch:    branch=this.GITHUB_TARGET_BRANCH
        if not globalPath:    globalPath=this.GLOBAL_DIRECTORY_PATH
        try:
            import requests
            import zipfile
            import time
            import os
            import shutil
            this.fileRequest = requests.get(f"https://codeload.github.com/{user}/{repo}/zip/{branch}")
            if this.fileRequest.status_code != 200:
                return "Generated GitHub link is invalid. Be sure to check if GITHUB_TARGET_REPOSITORY, GITHUB_USERNAME, and GITHUB_TARGET_BRANCH are all correct."
            else:
                markTime = time.time()
                parentPath = pathlib.PurePath(globalPath).parents[0]
                with open(os.path.join(parentPath, f"{markTime}.zip"), "wb") as zipFileOBJ:
                    zipFileOBJ.write(this.fileRequest.content)
                with zipfile.ZipFile(os.path.join(parentPath, f"{markTime}.zip"), "r") as zipFileOBJ:
                    zipFileOBJ.extractall(pathlib.Path(parentPath))
                os.remove(os.path.join(parentPath, f"{markTime}.zip"))
                oldDirTitle = pathlib.PurePath(globalPath).parts[-1]
                shutil.rmtree(os.path.join(parentPath,oldDirTitle))
                os.rename(f"{repo}-{branch}", oldDirTitle)
        except Exception as error:
            print(error)
            if type(error)==AttributeError:
                return "Initialize the \"grab\" class before calling!"
            if type(error)==ModuleNotFoundError:
                return "One or more modules not found. Please see list of prerequisites at \"https://github.com/TheTurtleStudio/UpdateGrabber\"."
            else: return error
    def TS(function):
        print(function)
h = grab(settingsLocation)
print(h.update())
