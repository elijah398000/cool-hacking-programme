import tkinter as tk
import socket

def make_request(url, protocol):
    try:
        # Check if the input is an IP address or a hostname
        ip_address = socket.gethostbyname(url)
        result_label.configure(text=f"IP address: {ip_address}")
    except socket.gaierror:
        result_label.configure(text="Invalid hostname")

root = tk.Tk()

protocol_label = tk.Label(root, text="Protocol:")
protocol_label.grid(row=0, column=0)

protocol_var = tk.StringVar(value="http")
protocol_radiobutton1 = tk.Radiobutton(root, text="HTTP", variable=protocol_var, value="http")
protocol_radiobutton1.grid(row=0, column=1)
protocol_radiobutton2 = tk.Radiobutton(root, text="HTTPS", variable=protocol_var, value="https")
protocol_radiobutton2.grid(row=0, column=2)
protocol_radiobutton3 = tk.Radiobutton(root, text="DNS lookup", variable=protocol_var, value="dns")
protocol_radiobutton3.grid(row=0, column=3)

url_label = tk.Label(root, text="URL:")
url_label.grid(row=1, column=0)

url_entry = tk.Entry(root)
url_entry.grid(row=1, column=1, columnspan=3)

submit_button = tk.Button(root, text="Submit", command=lambda: 
                          make_request(url_entry.get(), protocol_var.get()))
submit_button.grid(row=2, column=0, columnspan=4)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=4)

root.mainloop()
