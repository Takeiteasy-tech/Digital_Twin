import streamlit as st
import pandas as pd
import random
import plotly.express as px

# =========================
#  UI DESIGN
# =========================

st.set_page_config(page_title="Digital Twin Factory", layout="wide")

st.title("🏭 AI-Based Digital Twin for Smart Factory")

st.sidebar.title("⚙️ Control Panel")
st.sidebar.write("Monitor factory performance")

st.header("📊 Factory Overview")

# =========================
#  DATA GENERATION
# =========================

machines = []

for i in range(1, 6):

    machine = {
        "Machine": f"M{i}",
        "Temperature": random.randint(50, 110),
        "Efficiency": random.randint(40, 100),
        "Power": random.randint(100, 300),
        "Production": random.randint(500, 1500)
    }

    # STATUS LOGIC
    if machine["Temperature"] < 80:
        machine["Status"] = "Healthy"

    elif machine["Temperature"] < 90:
        machine["Status"] = "Warning"

    else:
        machine["Status"] = "Critical"

    machines.append(machine)

# CREATE DATAFRAME
df = pd.DataFrame(machines)

# =========================
# FACTORY METRICS
# =========================

total = len(df)
healthy = len(df[df["Status"] == "Healthy"])
critical = len(df[df["Status"] == "Critical"])

avg_efficiency = round(df["Efficiency"].mean(), 2)
total_power = df["Power"].sum()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Machines", total)
col2.metric("Healthy", healthy)
col3.metric("Critical", critical)
col4.metric("Avg Efficiency", f"{avg_efficiency}%")
col5.metric("Power Usage", f"{total_power} kWh")

st.markdown("---")

# =========================
#  MACHINE MONITORING
# =========================

st.subheader("🛠 Machine Monitoring")

st.dataframe(df)

st.markdown("---")

for index, row in df.iterrows():

    st.write(f"## {row['Machine']}")

    st.write(f"🌡 Temperature: {row['Temperature']} °C")
    st.write(f"⚙ Efficiency: {row['Efficiency']} %")
    st.write(f"⚡ Power Usage: {row['Power']} kWh")
    st.write(f"🏭 Production: {row['Production']} units")
    st.write(f"📌 Status: {row['Status']}")

    if row['Status'] == "Healthy":
        st.success("Machine is operating normally ✅")

    elif row['Status'] == "Warning":
        st.warning("Machine requires maintenance attention ⚠️")

    else:
        st.error("Critical machine condition detected 🚨")

    st.markdown("---")

# =========================
#  AI ALERTS
# =========================

st.subheader("🤖 AI Alerts")

alerts = []

for index, row in df.iterrows():

    if row["Temperature"] > 90:
        alerts.append(f"🔥 {row['Machine']} is overheating!")

    if row["Efficiency"] < 60:
        alerts.append(f"⚠ {row['Machine']} efficiency is very low!")

    if row["Power"] > 250:
        alerts.append(f"⚡ {row['Machine']} power usage is extremely high!")

if alerts:

    for alert in alerts:
        st.error(alert)

else:
    st.success("✅ All machines operating efficiently")

st.markdown("---")

# =========================
#  OPTIMIZATION SUGGESTIONS
# =========================

st.subheader("💡 AI Optimization Suggestions")

for index, row in df.iterrows():

    if row["Temperature"] > 90:

        st.write(
            f"🔧 {row['Machine']}: Reduce workload immediately to prevent overheating."
        )

    elif row["Efficiency"] < 60:

        st.write(
            f"🛠 {row['Machine']}: Schedule predictive maintenance to improve efficiency."
        )

    elif row["Power"] > 250:

        st.write(
            f"⚡ {row['Machine']}: Optimize power consumption to reduce energy waste."
        )

    else:

        st.write(
            f"✅ {row['Machine']}: Operating under optimal factory conditions."
        )

st.markdown("---")

# =========================
# FACTORY ANALYTICS & CHARTS
# =========================

st.subheader("📈 Factory Analytics Dashboard")

# ---------------------------------
# TEMPERATURE BAR CHART
# ---------------------------------

fig1 = px.bar(
    df,
    x="Machine",
    y="Temperature",
    color="Status",
    text="Temperature",
    title="🌡 Machine Temperature Analysis"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------------------------
# EFFICIENCY LINE CHART
# ---------------------------------

fig2 = px.line(
    df,
    x="Machine",
    y="Efficiency",
    markers=True,
    title="⚙ Machine Efficiency Analysis"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------
# POWER CONSUMPTION PIE CHART
# ---------------------------------

fig3 = px.pie(
    df,
    names="Machine",
    values="Power",
    title="⚡ Power Consumption Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------
# PRODUCTION ANALYTICS
# ---------------------------------

fig4 = px.bar(
    df,
    x="Machine",
    y="Production",
    color="Status",
    text="Production",
    title="🏭 Production Output Analysis"
)

st.plotly_chart(fig4, use_container_width=True)

# ---------------------------------
# MACHINE STATUS DISTRIBUTION
# ---------------------------------

status_count = df["Status"].value_counts()

fig5 = px.pie(
    values=status_count.values,
    names=status_count.index,
    title="📌 Machine Health Distribution"
)

st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")

# =========================
# FINAL FACTORY SUMMARY
# =========================

st.subheader("📋 Factory Summary Report")

st.write(f"✅ Total Machines Monitored: {total}")

st.write(f"⚙ Average Factory Efficiency: {avg_efficiency}%")

st.write(f"⚡ Total Energy Consumption: {total_power} kWh")

st.write(
    "🏭 AI-based Digital Twin system successfully monitoring and optimizing factory operations."
)

st.success("🚀 Smart Factory System Running Successfully")