# Project Save Edit: save edit for everyone

Project Save Edit is a simple command line tool to help you with save editing for Inscryption by Daniel Mullins.  
If you somehow get here and not know what Inscryption is, nothing here will make any sense.

## Some Important note

Save edit can be very buggy sometime so it may corrupt your save file so making backup is recommended.  
And for some stupid reason save editing with kmod can be quite buggy. Some commands are lock when you are in kmod, some are still unlock because I haven't test all command in kmod so if you found a bug just tell me on discord (khanhFG#3753) or make an issue here on github.

## How to install

**I have only tested this on Window so I have no idea if it work for Mac or Linux.**

So let install this thing. First go to the lasted release and download `ProjectSaveEdit.zip`. After you downloaded it, now unzip it. In there you will find a text file call `path.txt` opening it you should see something like this.

```text
Your save file directory here
```
**So now enter your Inscryption save file directory**. If you don't know where to get it here a quick guide.

Open up steam go to the game in your library now click the little gear icon on the right of the game name, then click `Manage > Browse Local File`. It should open file explorer on your computer in there you will find all the game file. Ok now look in that folder find a file call `SaveFile.gwsave` that is your game save file. Now right-click it "Copy as path" then paste that into the `path.txt` file. Then remove the two little quote at the start and end of it.

I should look something like this:
```text
C:\Program Files (x86)\Steam\steamapps\common\Inscryption\SaveFile.gwsave
```
After you done all that, then you are set now just run `main.exe` and start using the tool.

## Usage

Using this tool is quite easy you just input and run command. For a list of commands just input `help` and run it. It will print out a list of commands that look like this.
```
******************** HELP FORMAT ********************
[Command Name] [Command Alias]: [Command Description]
*****************************************************

- addCard ['ac']: [card name] add card to your deck using save edit
- backup ['bkup']: Backup your save file
- changeAct ['ca']: [act] change the current act that you save edit from (0: act 1, 1: act 2, etc.)
- changeChallengeLevel ['ccl']: [New challenge level] Change Kaycee's mod challenge level. Will not affect other act
```
Let unpack what just happened. Firstly the `HELP FORMAT` should help you with how to read what it prints. Let analyze one of the command shall we.
```
- backup ['bkup']: Backup your save file
```
The command name is `backup` which mean you can input `backup` into the command line to run this command.   
The command alias in this case `['bkup']` meaning you can also input `bkup` to run the command.  
Finally, the command description `Backup your save file` is a short description about the command and what it do in this case "backup your save file".

Let look at another one:
```
- changeChallengeLevel ['ccl']: [New challenge level] Change Kaycee's mod challenge level. Will not affect other act
```
Same as the other one `changeChallengeLevel` and `ccl` is it alias so you can input either of those to run the command. Now the description is a little bit different now it has that square bracket thing. So that mean it is the command argument. So here an example changing th challenge level to 5, I would enter `ccl 5`.  
And that explain pretty much all the command in this tool. Some command can print a detail error message some just print `Error`. `Error` can be cause by typo or missing argument.
