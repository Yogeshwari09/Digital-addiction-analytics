import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Digital Addiction Analytics", layout="wide")

st.title("📱 Digital Addiction Analytics Dashboard")
st.markdown("Analyze screen time behavior and addiction patterns")

@st.cache_data
def load_data():
    df = pd.read_csv("digital_addiction_screentime.csv", parse_dates=["date"])
    return df

df = load_data()

st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

df["addiction_score"] = (
    df["usage_minutes"] * 0.5 +
    df["pickups"] * 0.3 +
    df["notifications"] * 0.2
)

def addiction_level(score):
    if score < 100:
        return "Low"
    elif score < 200:
        return "Moderate"
    else:
        return "High"

df["addiction_level"] = df["addiction_score"].apply(addiction_level)

st.sidebar.header("🔍 Filters")

category = st.sidebar.multiselect(
    "Select Category",
    options=df["category"].unique(),
    default=df["category"].unique()
)

filtered_df = df[df["category"].isin(category)]

st.subheader("📊 Total Usage by App")

app_usage = filtered_df.groupby("app_name")["usage_minutes"].sum()

fig, ax = plt.subplots()
app_usage.plot(kind="bar", ax=ax)
ax.set_ylabel("Minutes")

st.pyplot(fig)

st.subheader("🧠 Addiction Level Distribution")

fig, ax = plt.subplots()
sns.countplot(data=filtered_df, x="addiction_level", ax=ax)
st.pyplot(fig)

st.subheader("⏰ Hourly Usage Pattern")

hourly = filtered_df.groupby("hour")["usage_minutes"].mean()

fig, ax = plt.subplots()
ax.plot(hourly)
ax.set_xlabel("Hour")
ax.set_ylabel("Avg Usage Minutes")
st.pyplot(fig)

total_usage = int(df["usage_minutes"].sum())
avg_addiction = round(df["addiction_score"].mean(), 2)
high_addiction = (df["addiction_level"] == "High").sum()

col1, col2, col3 = st.columns(3)
col1.metric("📱 Total Screen Time (min)", total_usage)
col2.metric("🧠 Avg Addiction Score", avg_addiction)
col3.metric("⚠ High Addiction Records", high_addiction)

st.subheader("📝 Key Insights")

st.write(f"- Highest usage app: **{app_usage.idxmax()}**")
st.write(f"- Most addictive category: **{filtered_df.groupby('category')['addiction_score'].mean().idxmax()}**")
st.write("- Evening hours show higher digital engagement")

st.subheader("💡 Personalized Recommendations")

avg_score = filtered_df["addiction_score"].mean()
top_app = filtered_df.groupby("app_name")["usage_minutes"].sum().idxmax()
top_category = filtered_df.groupby("category")["usage_minutes"].sum().idxmax()

if avg_score > 200:
    st.warning("⚠ High digital addiction detected. Consider reducing screen time, especially during night hours.")
elif avg_score > 120:
    st.info("ℹ Moderate addiction level. Try scheduling regular screen breaks.")
el

st.sidebar.title("🔐 Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if username != "admin" or password != "1234":
    st.sidebar.warning("Please login to continue")
    st.stop()
else:
    st.sidebar.success("Login successful")
