import paramiko

sshipinput=input("ssh ip giriniz: ")
userinput=input("username giriniz: ")
passwordinput=input("şifreyi giriniz: ")
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(sshipinput,username=userinput,password=passwordinput)
stdin, stdout, stderr = ssh.exec_command("ls")
print(stdout.read())