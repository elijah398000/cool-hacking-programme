import tkinter as tk
import requests

def make_request(url, method, headers, data):
    result_label.configure(text="")
    try:
        response = requests.request(method=method, url=url, headers=headers, data=data)
        result_text = f"Status code: {response.status_code}\n\n"
        result_text += f"Headers:\n{response.headers}\n\n"
        result_text += f"Content:\n{response.content}"
        result_label.configure(text=result_text)
    except requests.exceptions.RequestException as e:
        result_label.configure(text=str(e))

root = tk.Tk()

method_label = tk.Label(root, text="Method:")
method_label.grid(row=0, column=0)

method_var = tk.StringVar(value="GET")
method_optionmenu = tk.OptionMenu(root, method_var, "GET", "POST", "PUT", "DELETE")
method_optionmenu.grid(row=0, column=1)

url_label = tk.Label(root, text="URL:")
url_label.grid(row=1, column=0)

url_entry = tk.Entry(root)
url_entry.grid(row=1, column=1, columnspan=3)

headers_label = tk.Label(root, text="Headers:")
headers_label.grid(row=2, column=0)

headers_text = tk.Text(root, height=5, width=40)
headers_text.grid(row=2, column=1, columnspan=3)

data_label = tk.Label(root, text="Data:")
data_label.grid(row=3, column=0)

data_text = tk.Text(root, height=5, width=40)
data_text.grid(row=3, column=1, columnspan=3)

submit_button = tk.Button(root, text="Submit", command=lambda: 
                          make_request(url_entry.get(), method_var.get(),
                                       headers=headers_text.get("1.0", "end-1c"),
                                       data=data_text.get("1.0", "end-1c")))
submit_button.grid(row=4, column=0, columnspan=4)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=4)

root.mainloop()
