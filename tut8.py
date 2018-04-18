#retrieving directory listing or copy of file from ftp server
import ftplib
f=ftplib.FTP("ftp.gnu.org","anonymous","dave@dabeaz.coms")
files=[]
f.retrlines("LIST",files.append)
# f.retrbinary("RETR MISSING-FILES",files.append)
print(len(files))
print(files[2])
host = "ftp.foo.com"
username = "dave"
password = "1235"
filename = "file1.dat"

# storing files in the ftp server
import ftplib
ftp_serv = ftplib.FTP(host,username,password)
# Open the file you want to send
f = open(filename,"rb")
# Send it to the FTP server
resp = ftp_serv.storbinary("STOR "+filename, f)
# Close the connection
ftp_serv.close()