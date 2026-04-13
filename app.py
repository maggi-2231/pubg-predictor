import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="PUBG Predictor", page_icon="🎮", layout="centered")

# Load model
model = pickle.load(open("pubg_model.pkl", "rb"))

st.title("🎮 PUBG Winner Prediction")
st.markdown("### Enter Player Stats")

# Layout (2 columns)
col1, col2 = st.columns(2)

with col1:
    kills = st.slider("Kills", 0, 30, 0)
    damage = st.slider("Damage Dealt", 0, 5000, 0)
    walk = st.slider("Walk Distance", 0, 10000, 0)

with col2:
    ride = st.slider("Ride Distance", 0, 20000, 0)
    swim = st.slider("Swim Distance", 0, 500, 0)
    weapons = st.slider("Weapons Acquired", 0, 20, 0)

heals = st.slider("Heals", 0, 20, 0)
boosts = st.slider("Boosts", 0, 20, 0)
headshotKills = st.slider("Headshot Kills", 0, 20, 0)

# Button
if st.button("🚀 Predict"):

    totalDistance = walk + ride + swim
    headshot_rate = headshotKills / (kills + 1)
    healing_items = heals + boosts

    input_df = pd.DataFrame([{
        'kills': kills,
        'damageDealt': damage,
        'walkDistance': walk,
        'rideDistance': ride,
        'swimDistance': swim,
        'weaponsAcquired': weapons,
        'heals': heals,
        'boosts': boosts,
        'headshotKills': headshotKills,
        'totalDistance': totalDistance,
        'headshot_rate': headshot_rate,
        'healing_items': healing_items
    }])

    prediction = model.predict(input_df)[0]

    st.subheader(f"🎯 Win Probability: {prediction*100:.2f}%")

    if prediction >= 0.7:
        st.success("🏆 Very High chance of winning!")
    elif prediction >= 0.5:
        st.info("👍 Moderate chance")
    else:
        st.error("❌ Low chance of winning")