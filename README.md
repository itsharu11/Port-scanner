

## Port Scanner Code Documentation

The given Python code is a simple port scanner script that can be used to scan all the open ports on a given target IP. The script uses the `socket` module to establish a connection to each port on the target IP address and check if it is open or closed.

The code starts by importing the required modules: `pyfiglet`, `sys`, `socket`, and `datetime`. The `pyfiglet` module is used to create an ASCII art banner that says "PORT SCANNER". The `sys` module is used to handle exceptions and exit the script, while the `socket` module is used to create a socket object that can be used to connect to a specific port on the target IP. The `datetime` module is used to display the time when the scanning process was started.

```python
import pyfiglet
import sys
import socket
from datetime import datetime
```

The code then prints the ASCII art banner using the `pyfiglet` module and prompts the user to enter the target IP address.

```python
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

target = input(str("Target IP: "))
```

After that, the code prints a separator and displays the time when the scanning process was started.

```python
print("_" * 50)
print("Scanning Started at: " + str(datetime.now()))
print("_" * 50)
```

Next, the code tries to establish a connection to each port on the target IP address using a for loop that iterates over a range of ports from 1 to 65535. The `socket.socket()` method creates a socket object, and the `socket.setdefaulttimeout()` method sets the default timeout for the socket object to 0.5 seconds. 

```python
try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
```

The `s.connect_ex()` method is then used to establish a connection to the current port on the target IP. If the connection is successful and the port is open, the code prints a message to indicate that the port is open. 

```python
        result = s.connect_ex((target, port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()
```

If an exception occurs, the code will print a message to indicate the reason for the exception and exit the script. If the user interrupts the scanning process using the keyboard (i.e., `Ctrl + C`), the code will print a message and exit the script. 

```python
except KeyboardInterrupt:
        print("\n Exiting :(")
        sys.exit()
except socket.error:
        print("\ Host not responding :()")
        sys.exit()
```

Overall, this is a simple yet effective port scanner script that can be used to identify open ports on a given target IP. However, it should be used responsibly and only on targets that you have permission to scan.
