

#bad_words = ['dis','|']

num1 = input("starting of files : ")
num2 = input("ending if files : ")
#with open('issue_1') as oldfile, open('issue_f', 'w') as newfile:
#    for line in oldfile:
#        if not any(bad_word in line for bad_word in bad_words):
#            newfile.write(line)

for x in range(num1,num2):
	with open('issue_'+str(x),'r') as newfile, open('fil/issue_'+str(x), 'w') as last:
	    for line in newfile:
		line = line.replace('dis','')
		line = line.replace('|','')
		line = line.replace('"','')
		if line.strip():				
			last.write(line)
			print line

	

print './done'
