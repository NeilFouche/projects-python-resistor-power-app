import streamlit as st

# App title and description
st.title("Power Dissipation in a Resistor")
st.markdown(r"Enter values for $\text{Voltage} (V)$, $\text{Current} (I)$ and $\text{Resistance} (R)$ to calculate the $\text{Power} (P)$ dissipated in the resistor.")

# User inputs
voltage = st.number_input("Voltage (V)", value=st.session_state.get("voltage"))
current = st.number_input("Current (A)", value=st.session_state.get("current"))
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
    st.metric("Power, P", value=f"{power:.3f} W", border=True)