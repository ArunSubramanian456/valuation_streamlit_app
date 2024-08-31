import streamlit as st
import pandas as pd
import numpy as np


def dcf_valuation(fcfps, growth_rate, discount_rate, terminal_pe_ratio, years=5):
    """
    Calculates intrinsic stock value using the DCF model.

    Args:
        fcf: Free cash flow per share for the trailing twelve months
        growth_rate: Projected annual growth rate of free cash flow per share
        discount_rate: Discount rate (weighted average cost of capital)
        years: Number of years to project free cash flow

    Returns:
        Intrinsic stock value
    """

    # Calculate discounted cash flows for projection period
    for year in range(1, years + 1):
        fcfps*=(1 + growth_rate)        

    # Calculate intrinsic value
    intrinsic_value = (fcfps * terminal_pe_ratio)/(1+discount_rate)**(years)

    return intrinsic_value

def main():
    st.title("Intrinsic Stock Value Calculator (DCF)")

    # User input fields
    tickr = st.text_input("Ticker Symbol", value = "AAPL")
    fcfps = st.number_input("Free Cash Flow Per Share", value=6.73)
    growth_rate = st.number_input("Growth Rate (%)", value=12) / 100
    discount_rate = st.number_input("Discount Rate (%)", value=10) / 100
    terminal_pe_ratio = st.number_input("Terminal PE Ratio", value=20) 
    years = st.number_input("Number of Years to Project", value=5)


    if st.button("Calculate Intrinsic Value"):
        # Calculate intrinsic value
        intrinsic_value = dcf_valuation(fcfps, growth_rate, discount_rate, terminal_pe_ratio, years)

        # Display result
        st.write(f"Intrinsic Stock Value of {tickr}: ${intrinsic_value:.2f}")

if __name__ == "__main__":
    main()