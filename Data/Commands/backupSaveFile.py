from Data.Library import saveEditFunc
name = "backup"
alias = ['bkup']
description = "Backup your save file"
def run(arg: list):
   saveFile = saveEditFunc.readSaveFile()
   newBackup = open("Data\Backup\Backup.gwsave", "w")
   for line in saveFile:
      newBackup.write(line)
      
   print("Save file backup")
