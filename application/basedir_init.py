def basedir():
    """There will be a need to keep track in which directory we are located, so by running
    this function in the beginning of the project initialization, a json file will be prepared
    that will keep track what is a base directory is, from which navigation can be handled.

    This is primarily done, to ease the process of navigation for the code between computers
    and not cram all of the code files into one place. Database_init does not require this 
    function beforehand, because it is ran from the base directory as well.

    Inputs:
        None

    Return:
        Generates a .json file in the core directory
    """
    import os
    import json

    cwd = os.getcwd()
    output = {"Directory": cwd}
    with open("directory.json", "w") as outfile:
        json.dump(output, outfile)

if __name__ == "__main__":
    basedir()