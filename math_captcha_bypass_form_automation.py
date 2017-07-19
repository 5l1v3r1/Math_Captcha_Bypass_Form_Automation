import re
import mechanize
from mechanize import Browser

while True:

	br = mechanize.Browser()
	br.set_handle_robots( False )
	br.addheaders = [('User-agent', 'Firefox')]

	#Mentioned your website url
	response = br.open('website URL')
	html = response.read()
	print "Response Code: ",response.code
	print "Title: ",br.title()

	#Searching Captcha value and calculate it 

	searchobj = re.search(r'(<span class="field-prefix">)(\d*)(\D*)(\d*)', html, re.I)
	a = searchobj.group(2)
	print "Captcha_First_Value: ",a
	b = searchobj.group(4)
	print "Captcha_Second_Value: ",b
	sum = int(a) + int (b)
	print('Captcha_Total_Value: {0} + {1} = {2}'.format(a, b, sum))

	#Priniting Form Name

	for f in br.forms():
		print "Form name:", f.name
		#print f

	#Filling Form Values
	#Mentioned form name value here and "nr" is form number

#	br.select_form(nr=1)
#	br.form['form value'] = "anything"
#	br.form['submitted[name]'] = 'hahahah'
#	br.form['submitted[country]'] = 'India'
#	br.form['submitted[state]']= ''
#	br.form['submitted[city]']= ''
#	br.form['submitted[address]']= 'anonymous'
#	br.form['submitted[contact_number]']= ''
#	br.form['submitted[email]']= ''
#	br.form['submitted[subject]']= 'testing'
#	br.form['submitted[message]']= 'hehehehheheheheh'
#	br.form['captcha_response']= str(sum)
	br.submit()
	print "Form Submited...."


