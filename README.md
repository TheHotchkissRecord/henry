# Henry
*Henry* is named after Henry Luce '16. It is a command-line widget that compiles *Off the Record* newsletters automatically. 

## Installation
Run
```shell
git clone https://github.com/TheHotchkissRecord/henry.git
```
## Usage
*Henry* can be run simply from the Terminal or any command line interface, it runs on Python 3. 
```shell
python henry.py
```
However, it it optimal to compile *Henry* into an executable and run it alongside the directory of newsletters. To do this, we use `pyinstaller` to compile the executable. Run
```shell
pyinstaller --onefile henry.py
```
and the executable file will be in `dist` folder. Drag `henry` into the newsletter folder to use. 

## Upcoming
*Henry* is (hopefully) getting a GUI soon. 
```
      ___           ___           ___           ___                 
     /__/\         /  /\         /__/\         /  /\          ___   
     \  \:\       /  /:/_        \  \:\       /  /::\        /__/|  
      \__\:\     /  /:/ /\        \  \:\     /  /:/\:\      |  |:|  
  ___ /  /::\   /  /:/ /:/_   _____\__\:\   /  /:/~/:/      |  |:|  
 /__/\  /:/\:\ /__/:/ /:/ /\ /__/::::::::\ /__/:/ /:/___  __|__|:|  
 \  \:\/:/__\/ \  \:\/:/ /:/ \  \:\~~\~~\/ \  \:\/:::::/ /__/::::\  
  \  \::/       \  \::/ /:/   \  \:\  ~~~   \  \::/~~~~     ~\~~\:\ 
   \  \:\        \  \:\/:/     \  \:\        \  \:\           \  \:\
    \  \:\        \  \::/       \  \:\        \  \:\           \__\/
     \__\/         \__\/         \__\/         \__\/                
```
