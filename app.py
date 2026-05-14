import streamlit as st
import pandas as pd
import random
import plotly.express as px

# =========================
# STEP 10 — UI DESIGN
# =========================

st.title("🏭 AI-Based Digital Twin for Smart Factory")

st.sidebar.title("⚙️ Control Panel")
st.sidebar.write("Monitor factory performance")

st.header("📊 Factory Overview")

# =========================
# STEP 9 — DATA GENERATION
# =========================

machines = []

for i in range(1, 6):
    machine = {
        "Machine": f"M{i}",
        "Temperature": random.randint(50, 110),
        "Efficiency": random.randint(40, 100),
        "Power": random.randint(100, 300)
    }

    # Status logic
    if machine["Temperature"] < 80:
        machine["Status"] = "Healthy"
    elif machine["Temperature"] < 90:
        machine["Status"] = "Warning"
    else:
        machine["Status"] = "Critical"

    machines.append(machine)

df = pd.DataFrame(machines)

# =========================
# METRICS
# =========================

total = len(df)
healthy = len(df[df["Status"] == "Healthy"])
critical = len(df[df["Status"] == "Critical"])

col1, col2, col3 = st.columns(3)
col1.metric("Total Machines", total)
col2.metric("Healthy", healthy)
col3.metric("Critical", critical)

st.markdown("---")

# =========================
# MONITORING
# =========================

st.subheader("🛠 Machine Monitoring")
st.dataframe(df)

st.markdown("---")

for index, row in df.iterrows():
    st.write(f"### {row['Machine']}")
    st.write(f"Temperature: {row['Temperature']} °C")
    st.write(f"Efficiency: {row['Efficiency']} %")
    st.write(f"Power Usage: {row['Power']} kWh")
    st.write(f"Status: {row['Status']}")

    if row['Status'] == "Healthy":
        st.success("Machine is running smoothly ✅")
    elif row['Status'] == "Warning":
        st.warning("Machine needs attention ⚠️")
    else:
        st.error("Critical issue! Immediate action required 🚨")

    st.markdown("---")

# =========================
# AI ALERTS
# =========================

st.subheader("🤖 AI Alerts")

alerts = []

for index, row in df.iterrows():
    if row["Temperature"] > 90:
        alerts.append(f"⚠ {row['Machine']} is overheating!")

    if row["Efficiency"] < 60:
        alerts.append(f"⚠ {row['Machine']} has low efficiency!")

if alerts:
    for alert in alerts:
        st.error(alert)
else:
    st.success("✅ All machines operating normally")

# =========================
# OPTIMIZATION
# =========================

st.subheader("💡 Optimization Suggestions")

for index, row in df.iterrows():

    if row["Temperature"] > 90:
        st.write(f"{row['Machine']}: Reduce load to prevent overheating 🔥")

    elif row["Efficiency"] < 60:
        st.write(f"{row['Machine']}: Schedule maintenance 🛠")

    elif row["Power"] > 250:
        st.write(f"{row['Machine']}: Optimize power usage ⚡")

    else:
        st.write(f"{row['Machine']}: Operating efficiently ✅")

st.markdown("---")

# =========================
# CHARTS (VERY IMPORTANT 🔥)
# =========================

st.subheader("📈 Factory Analytics")

# Temperature Chart
fig1 = px.bar(df, x="Machine", y="Temperature", color="Status",
              title="Machine Temperature")
st.plotly_chart(fig1)

# Efficiency Chart
fig2 = px.bar(df, x="Machine", y="Efficiency", color="Status",
              title="Machine Efficiency")
st.plotly_chart(fig2)

# Power Usage Chart
fig3 = px.pie(df, names="Machine", values="Power",
              title="Power Consumption Distribution")
st.plotly_chart(fig3)
