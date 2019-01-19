import itchat
from pandas import DataFrame

itchat.login()

friends=itchat.get_friends(update=True)[0:]

def get_var(var):
	variable=[]
	for i in friends:
		value=i[var]
		variable.append(value)
	return variable
 

NickName=get_var('NickName')
Sex=get_var('Sex')
Province=get_var('Province')
City=get_var('City')
Signature=get_var('Signature')

data={'NickName':NickName,'Sex':Sex,'Province':Province,'City':City,'Signature':Signature}
frame=DataFrame(data)
frame.to_csv('data.csv',index=True,encoding="utf_8_sig")