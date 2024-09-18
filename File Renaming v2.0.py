import os
import re

#Variables
ValidType = False
ValidUser = False
ValidInstallment = False
prefix = str()
installment = 1
FileType = str()

#Sort list to fix issue
#I used chatgpt because I couldn't find any solutions like at all
#I kind of understand it though, never used the re package before.
def listSort(strings):
    #inner function to help out
    def extractNumbers(s):
        #re.findall to find all numbers in ascending order
        numbers = re.findall(r'\d+', s)
        #turn all the numbers found into integers and puts anything without int at the back
        return int(numbers[0]) if numbers else float('inf')
    #sort by the ints
    return sorted(strings, key=extractNumbers)

#Notes for user
print('VERSION 2.0 BABY')
print('PREVIOUS FLAWS FIXED WE LOVE IT\n')
print('Please make sure the folder is in the downloads folder.')
print('This program assumes and is dependant on the fact that the destination of the file is in hard drive C: and the Downloads folder.')
print('Please note if the program encounters an error that you typed everything in properly.')
print('Another note, please make sure the volumes can be arranged properly in numerical order.\
 This is necessary for the program to work properly')
print('Next note is that if the program crashes, and error probably happened so just restart it it\'s fine,')
print('Second last note is that this isn\'t a file reformatter so don\' try to change up the file type.')
print('Last note is that this program doesn\'t take decimals into consideration - Only integers.')
print()
print('Code by Rinko (Discord user rinko__)')
print()
while ValidType == False:
    print('Are the contents of the folder a TV series or manga/comic series?')
    print('If you would like to assign your own prefix, enter other')
    print('TYPE PREFIX OR P TO SEE PREFIXES')
    type = input('Enter TV/Comic/Manga/Other/Prefix: ')
    type = type.upper()
    if type == 'TV' or type == 'T':
        ValidType = True
        prefix = 'S'
    elif type == 'MANGA'or type == 'M':
        ValidType = True
        prefix = 'v'
    elif type == 'COMIC'or type == 'C':
        ValidType = True
        prefix == 'Issue'
    elif type == 'OTHER' or type == 'O':
        ValidType = True
        print('Note that there is no secondary prefix.')
        prefix = input('Enter your desired prefix (Enter nothing for blank): ')
    elif type == 'PREFIX' or type == 'P' or type == 'PREFIXES':
        print()
        print('PREFIXES')
        print('TV show: S and E (Season and Episode)')
        print('Comic: Issue')
        print('Manga: v')
        print('Other: Custom (You pick)')
        print()
    else:
        print('Selection invalid. Please check spelling or enter correct type.')
        print()
while ValidUser == False:
    username = str(input('Enter the first 5 letters of the current username on the computer \n(File Manager > This PC > Your Hard Drive > Users): '))
    username = username.lower()
    NameCount = 0
    for i in username:
        NameCount += 1
    if NameCount == 5:
        ValidUser = True
    elif NameCount > 5:
        print('There are too many letters in your username.')
        print()
    elif NameCount < 5:
        print('There are too few letters in your username.')
        print()
folder = str(input('Enter the folder\'s name: '))
destination = str('C:/Users/' + username + '/Downloads/' + folder + '/')
SeriesName = str(input('Enter The Series Name (This is the name of your series): '))
if type == 'TV':
    Season = str(input('Enter the season: '))
while ValidInstallment == False:
    installment = int(input('Enter what Episode/Volume/Issue/Number your series starts with: '))
    if installment.is_integer() == False:
        print('INVALID ENTRY')
        print('MUST BE NUMBER')
    else:
        ValidInstallment = True
FileType = str(input('Finally, input the format of the files (Don\'t include the period) (Blank for folders): '))
FileList = os.listdir(destination)
#Sorting
FileList = listSort(FileList)
filecount = 0
for i in FileList:
    filecount += 1
if type == 'TV':
    for i in FileList:
        file = destination + i
        if filecount < 10:
            newname = destination + '/' + SeriesName + ' {}{}E{}.{}'.format(prefix, Season, installment, FileType)
        elif filecount < 100:
            if installment < 10:
                newname = destination + '/' + SeriesName + ' {}{}E0{}.{}'.format(prefix, Season, installment, FileType)
            else:
                newname = destination + '/' + SeriesName + ' {}{}E{}.{}'.format(prefix, Season, installment, FileType)
        elif filecount < 1000:
            if installment < 10:
                newname = destination + '/' + SeriesName + ' {}{}E00{}.{}'.format(prefix, Season, installment, FileType)
            elif installment < 100:
                newname = destination + '/' + SeriesName + ' {}{}E0{}.{}'.format(prefix, Season, installment, FileType)
            else:
                newname = destination + '/' + SeriesName + ' {}{}E{}.{}'.format(prefix, Season, installment, FileType)
        elif filecount < 10000:
            if installment < 10:
                newname = destination + '/' + SeriesName + ' {}{}E000{}.{}'.format(prefix, Season, installment, FileType)
            elif installment < 100:
                newname = destination + '/' + SeriesName + ' {}{}E00{}.{}'.format(prefix, Season, installment, FileType)
            elif installment < 1000:
                newname = destination + '/' + SeriesName + ' {}{}E0{}.{}'.format(prefix, Season, installment, FileType)
            else:
                newname = destination + '/' + SeriesName + ' {}{}E{}.{}'.format(prefix, Season, installment, FileType)
        os.rename(file, newname)
        installment += 1
else:
    for i in FileList:
        file = destination + i
        if filecount < 10:
            newname = destination + '/' + SeriesName + ' {}{}.{}'.format(prefix, installment, FileType)
        elif filecount < 100:
            if installment < 10:
                newname = destination + '/' + SeriesName + ' {}0{}.{}'.format(prefix, installment, FileType)
            else:
                newname = destination + '/' + SeriesName + ' {}{}.{}'.format(prefix, installment, FileType)
        elif filecount < 1000:
            if installment < 10:
                newname = destination + '/' + SeriesName + ' {}00{}.{}'.format(prefix, installment, FileType)
            elif installment < 100:
                newname = destination + '/' + SeriesName + ' {}0{}.{}'.format(prefix, installment, FileType)
            else:
                newname = destination + '/' + SeriesName + ' {}{}.{}'.format(prefix, installment, FileType)
        elif filecount < 10000:
            if installment < 10:
                newname = destination + '/' + SeriesName + ' {}000{}.{}'.format(prefix, installment, FileType)
            elif installment < 100:
                newname = destination + '/' + SeriesName + ' {}00{}.{}'.format(prefix, installment, FileType)
            elif installment < 1000:
                newname = destination + '/' + SeriesName + ' {}0{}.{}'.format(prefix, installment, FileType)
            else:
                newname = destination + '/' + SeriesName + ' {}{}.{}'.format(prefix, installment, FileType)
        os.rename(file, newname)
        installment += 1
print('\nThanks for downloading and using my program! I hope it worked as well for you as it did for me.')
print('Your files should be renamed now check the folder.')
input('Press Enter/Return to close the program: ')