bad_words = ['dis','|']


with open('issue_1') as oldfile, open('issue_f', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
with open('issue_1','r') as newfile, open('issue', 'w') as last:
    for line in newfile:
        line = line.replace('dis','')
	line = line.replace('|','')
        line = line.replace('"','')
        last.write(line)



print './done'
