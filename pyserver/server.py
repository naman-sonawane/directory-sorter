from flask import Flask, jsonify, request
from flask_cors import CORS
from os import *

myApp = Flask(__name__)
CORS(myApp)

@myApp.route("/sendingdata")
def userPaths():
    return jsonify({"msg": ""})

@myApp.route("/createfolder", methods=['POST'])
def create():

    userPath = request.get_json()['path']

    if not path.isdir(userPath):
        return jsonify({"msg":"Folder could not be found."})

    with scandir(userPath) as entries:
        for entry in entries:
            filename = entry.name
            extension = entry.name.split('.')[-1]
            
            if extension == "png" or extension == "jpg" or extension == "jpeg":
                try:
                    mkdir(userPath+ "\\" + "Images")
                except:
                    pass
                finally:
                    rename(userPath+'\\'+filename, userPath + '\\Images\\' + filename)
            elif extension == "gif":
                try:
                    mkdir(userPath+ "\\" + "Gifs")
                except:
                    pass
                finally:
                    rename(userPath+'\\'+filename, userPath + '\\Gifs\\' + filename)
            elif extension == "pdf":
                try:
                    mkdir(userPath+ "\\" + "PDFs")
                except:
                    pass
                finally:
                    rename(userPath+'\\'+filename, userPath + '\\PDFs\\' + filename)
            elif extension == "docx":
                try:
                    mkdir(userPath+ "\\" + "Documents")
                except:
                    pass
                finally:
                    rename(userPath+'\\'+filename, userPath + '\\Documents\\' + filename)
            elif extension == "mp4":
                try:
                    mkdir(userPath+ "\\" + "Videos")
                except:
                    pass
                finally:
                    rename(userPath+'\\'+filename, userPath + '\\Videos\\' + filename)
            elif extension == "mp3":
                try:
                    mkdir(userPath+ "\\" + "Audio")
                except:
                    pass
                finally:
                    rename(userPath+'\\'+filename, userPath + '\\Audio\\' + filename)
        return jsonify({"msg":"Folder sorted!"})

    
if __name__ == "__main__":
    myApp.run(debug=True, port=2323)