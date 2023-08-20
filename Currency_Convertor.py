pip install forex-python
import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates, RatesNotAvailableError

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        self.root_width = 500
        self.root_height = 200
        
        self.root.geometry(f"{self.root_width}x{self.root_height}+{int((self.screen_width - self.root_width) / 2)}+{int((self.screen_height - self.root_height) / 2)}")

        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()

        self.from_currency_label = ttk.Label(root, text="Convert from:")
        self.from_currency_entry = ttk.Combobox(root, textvariable=self.from_currency_var, values=self.get_currency_list())

        self.to_currency_label = ttk.Label(root, text="Convert to:")
        self.to_currency_entry = ttk.Combobox(root, textvariable=self.to_currency_var, values=self.get_currency_list())

        self.amount_label = ttk.Label(root, text="Amount:")
        self.amount_entry = ttk.Entry(root, textvariable=self.amount_var)

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_currency)
        self.layout_widgets()

    def layout_widgets(self):
        self.from_currency_label.grid(row=0, column=0, padx=10, pady=10)
        self.from_currency_entry.grid(row=0, column=1, padx=10, pady=10)

        self.to_currency_label.grid(row=1, column=0, padx=10, pady=10)
        self.to_currency_entry.grid(row=1, column=1, padx=10, pady=10)

        self.amount_label.grid(row=2, column=0, padx=10, pady=10)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)

        self.convert_button.grid(row=3, columnspan=2, padx=10, pady=10)

    def get_currency_list(self):
        currencies = [
            'USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN',
            'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD',
            'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK',
            'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 
            'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD',
            'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 
            'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 
            'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD',
            'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 
            'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 
            'QAR', 'RON', 'RSD', 'RUB', 'RWF', 
            'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 
            'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 
            'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL'

        ]
        return currencies

    def convert_currency(self):
        from_currency = self.from_currency_var.get().upper()
        to_currency = self.to_currency_var.get().upper()
        amount = self.amount_var.get()

        c = CurrencyRates()

        try:
            exchange_rate = c.get_rate(from_currency, to_currency)
            converted_amount = amount * exchange_rate
            result_text = f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}"
        except RatesNotAvailableError:
            result_text = "Conversion not available for selected currencies."

        self.show_result_window(result_text)

    def show_result_window(self, result_text):
        result_window = tk.Toplevel(self.root)
        result_window.title("Conversion Result")

        x_position = int((self.screen_width - self.root_width) / 2)
        y_position = int((self.screen_height - self.root_height) / 2)
        
        result_window.geometry(f"{self.root_width}x{self.root_height}+{x_position}+{y_position}")

        result_label = tk.Label(result_window, text=result_text, font=("Helvetica", 12, "bold"))
        result_label.pack(padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()

