import tkinter as tk
import dns.resolver

def make_request(url, query_type):
    result_label.configure(text="")
    try:
        answers = dns.resolver.query(url, query_type)
        result_text = "Results:\n"
        for rdata in answers:
            result_text += str(rdata) + "\n"
        result_label.configure(text=result_text)
    except dns.exception.DNSException as e:
        result_label.configure(text=str(e))

root = tk.Tk()

query_type_label = tk.Label(root, text="Query type:")
query_type_label.grid(row=0, column=0)

query_type_var = tk.StringVar(value="A")
query_type_radiobutton1 = tk.Radiobutton(root, text="A", variable=query_type_var, value="A")
query_type_radiobutton1.grid(row=0, column=1)
query_type_radiobutton2 = tk.Radiobutton(root, text="AAAA", variable=query_type_var, value="AAAA")
query_type_radiobutton2.grid(row=0, column=2)
query_type_radiobutton3 = tk.Radiobutton(root, text="MX", variable=query_type_var, value="MX")
query_type_radiobutton3.grid(row=0, column=3)
query_type_radiobutton4 = tk.Radiobutton(root, text="TXT", variable=query_type_var, value="TXT")
query_type_radiobutton4.grid(row=0, column=4)

url_label = tk.Label(root, text="Domain name:")
url_label.grid(row=1, column=0)

url_entry = tk.Entry(root)
url_entry.grid(row=1, column=1, columnspan=4)

submit_button = tk.Button(root, text="Submit", command=lambda: 
                          make_request(url_entry.get(), query_type_var.get()))
submit_button.grid(row=2, column=0, columnspan=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=5)

root.mainloop()
