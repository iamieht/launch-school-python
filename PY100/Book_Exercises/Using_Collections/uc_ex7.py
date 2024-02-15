# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
infoLst = info.split(':')
print('+'.join(infoLst))
