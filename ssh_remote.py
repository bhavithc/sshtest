import paramiko
import sys

def usage():

    message = """Usage:
\thello.py <ip> <username> <password> <cmd>
\twhere:
\t\t ip: Ip address of the target to connect 
\t\t username: Username 
\t\t password: Password
\t\t cmd: Command to be executed on the target
\texample: hello.py 192.168.1.10 bhavith bhavith@123 ls
\texample: hello.py 192.168.1.10 bhavith bhavith@123 'ls -la'
"""
    print(message)

def main(logger):

    cmd_line_args = sys.argv

    # if (len(cmd_line_args) == 2):
    #     if ip == "--help":
    #         usage()
    #         exit(0)

    if len(cmd_line_args) != 5:
        print("Invalid arguments are passed !")
        usage()
        exit(0)

    ip = cmd_line_args[1]
    username = cmd_line_args[2]
    password = cmd_line_args[3]
    cmd = cmd_line_args[4]


    logger.debug("setting up ssh")
    ssh = paramiko.SSHClient()
    logger.debug("setting policies")
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    logger.debug("connecting to remote server..")
    # ssh.connect(hostname=ip,
    #             username=username,
    #             password=password)

    # stdin, stdout, stderr = ssh.exec_command(cmd)

    # with open("out.txt", "w") as f:
    #     for line in stdout.read().splitlines():
    #         # print(line.decode("utf-8"))
    #         f.write(line.decode("utf-8"))
    #         f.write("\n")

    # logger.info("closing the terminal")
    # ssh.close()

if __name__ == "__main__":
    main()
