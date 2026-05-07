import matplotlib
matplotlib.use("Agg")
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fredapi import Fred
import os
import tempfile
from PIL import Image, ImageTk

API_KEY = "0edbe5011d8b90b46bc6474920b5bf8e"

REGIONS = {
    "California (Statewide)": "MEDLISPRICA",
    "Los Angeles County": "MEDLISPRI6037",
    "San Diego County": "MEDLISPRI6073",
    "Sacramento County": "MEDLISPRI6067",
    "San Francisco (Price Index)": "ATNHPIUS41884Q",
}

DATE_RANGES = {
    "1 Year": 1,
    "5 Years": 5,
    "10 Years": 10,
    "20 Years": 20,
}

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)


def fetch_data(region, years):
    filename = f"{DATA_DIR}/{region.replace(' ', '_')}_{years}yr.csv"

    if os.path.exists(filename):
        df = pd.read_csv(filename, index_col=0, parse_dates=True)
        return df

    fred = Fred(api_key=API_KEY)
    series_id = REGIONS[region]
    end_date = pd.Timestamp.today()
    start_date = end_date - pd.DateOffset(years=years)

    data = fred.get_series(series_id, observation_start=start_date, observation_end=end_date)
    df = pd.DataFrame(data, columns=["Median Home Price"])
    df.index.name = "Date"
    df.to_csv(filename)
    return df


def show_chart(region, years, parent):
    try:
        df = fetch_data(region, years)
    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch data:\n{e}")
        return

    df = df.dropna()
    prices = df["Median Home Price"].values
    dates = df.index

    moving_avg = np.convolve(prices, np.ones(6) / 6, mode='valid')
    pct_change = ((prices[-1] - prices[0]) / prices[0]) * 100
    avg = np.mean(prices)
    high = np.max(prices)
    low = np.min(prices)

    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.plot(dates, prices, label="Median Home Price", color="#2563eb", linewidth=2)
    ax.plot(dates[5:], moving_avg, label="6-Month Moving Avg", color="#f97316", linewidth=1.5, linestyle="--")
    ax.set_title(f"{region} Median Home Prices ({years} Years)", fontsize=13)
    ax.set_xlabel("Date")
    ax.set_ylabel("Median Home Price (USD)")
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    fig.savefig(tmp.name, dpi=100)
    plt.close(fig)

    popup = tk.Toplevel(parent)
    popup.title(f"{region} - {years} Year Housing Prices")
    popup.geometry("920x640")

    tk.Label(popup,
             text=f"Average: ${avg:,.0f}   |   High: ${high:,.0f}   |   Low: ${low:,.0f}   |   Change: {pct_change:.1f}%",
             font=("Arial", 11), pady=8).pack()

    img = Image.open(tmp.name)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(popup, image=photo)
    label.image = photo
    label.pack()

    tk.Button(popup, text="Close", command=popup.destroy, padx=10, pady=5).pack(pady=8)


def main():
    root = tk.Tk()
    root.title("California Housing Market Dashboard")
    root.geometry("500x350")
    root.resizable(False, False)

    tk.Label(root, text="California Housing Market Dashboard",
             font=("Arial", 16, "bold"), pady=20).pack()

    form_frame = tk.Frame(root)
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Region:", font=("Arial", 12), width=12, anchor="w").grid(row=0, column=0, pady=8)
    region_var = tk.StringVar(value="California (Statewide)")
    region_dropdown = ttk.Combobox(form_frame, textvariable=region_var,
                                   values=list(REGIONS.keys()), state="readonly", width=25)
    region_dropdown.grid(row=0, column=1, pady=8)

    tk.Label(form_frame, text="Date Range:", font=("Arial", 12), width=12, anchor="w").grid(row=1, column=0, pady=8)
    range_var = tk.StringVar(value="5 Years")
    range_dropdown = ttk.Combobox(form_frame, textvariable=range_var,
                                  values=list(DATE_RANGES.keys()), state="readonly", width=25)
    range_dropdown.grid(row=1, column=1, pady=8)

    def on_fetch():
        region = region_var.get()
        years = DATE_RANGES[range_var.get()]
        show_chart(region, years, root)

    tk.Button(root, text="Fetch Data", command=on_fetch,
              font=("Arial", 12), bg="#2563eb", fg="white",
              padx=20, pady=8).pack(pady=20)

    tk.Label(root, text="Data sourced from FRED (Federal Reserve Economic Data)",
             font=("Arial", 9), fg="gray").pack(side=tk.BOTTOM, pady=8)

    root.mainloop()


if __name__ == "__main__":
    main()
