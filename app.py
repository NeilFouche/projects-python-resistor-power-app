import streamlit as st
import numpy as np
import pandas as pd

# App title and description
st.title("Power Dissipation in a Resistor")
st.write("This app calculates the power dissipated through a resistor, based on the voltage applied to it and its rated resistance.")

with st.container(height=30, border=False):
    st.empty()

# User inputs
st.subheader("Parameters")
st.caption("""
    Enter values for the voltage, current and resistance to calculate the power dissipated in the resistor.
    Set a value to 0 to calculate the power in terms of the other two (2) parameters.
""")
voltage = st.number_input("Voltage (V)", value=st.session_state.get("voltage"))
current = st.number_input("Current (A)", value=st.session_state.get("current"), step=0.001, format="%.3f")
resistance = st.number_input("Resistance (Ω)", value=st.session_state.get("resistance"))

# Calculate power
if st.button("Calculate Power", type="primary"):
    st.session_state.power = None
    st.session_state.voltage = voltage
    st.session_state.current = current
    st.session_state.resistance = resistance
    if voltage and current:
        st.session_state.power = voltage * current
        st.session_state.resistance = voltage / current
        st.rerun()
    elif current and resistance:
        st.session_state.power = current ** 2 * resistance
        st.session_state.voltage = current * resistance
        st.rerun()
    elif voltage and resistance:
        st.session_state.power = voltage ** 2 / resistance
        st.session_state.current = voltage / resistance
        st.rerun()
    else:
        st.error("Please provide a pair of voltage, current and resistance.")

with st.container(height=30, border=False):
    st.empty()

if st.session_state.get("power"):
    power = st.session_state.power
    st.metric(f"Power, P ({st.session_state.get('resistance')}Ω)", value=f"{power:.3f} W", border=True)

with st.container(height=30, border=False):
    st.empty()

if st.session_state.get("voltage"):
    st.subheader("Power vs Voltage and Resistance plot")
    st.markdown(r"$P=\frac{V^2}{R}$")
    v = st.session_state["voltage"]
    r = st.session_state.get("resistance", 1000)

    R = np.linspace(r*0.5, r*1.5, 5)
    V = np.linspace(0, v, 100)

    df = pd.DataFrame(index=V)
    for r_value in R:
        df[f"P ({r_value:.2f}Ω)"] = V ** 2 / r_value # P = V²/R

    st.line_chart(df, x_label="Voltage (V)", y_label="Power (W)", )
    st.caption(f"""
        An array of power curves showing how power changes as the voltage changes.
        Each curve corresponds to a resistance which is the ratio of the voltage to the current.
        P ({r:.2f}Ω) shows the curve corresponding to the calculated power.
    """)