import json
from kafka import KafkaProducer
import streamlit as st


TOPIC_NAME = "marketing"
SERVER_ADDRESS = "127.0.0.1:9092"

st.title("Kafka Producer via Streamlit")

name = st.text_input("Name")
address = st.text_area("Address")
email = st.text_input("Email")
country = st.text_input("Country")

send_button = st.button("Send to Kafka")

if send_button:
    if not (name and address and email and country):
        st.warning("Please fill in all fields before sending.")
    else:
        user_data = {
            "name": name,
            "address": address,
            "email": email,
            "country": country
        }

        try:
            producer = KafkaProducer(
                bootstrap_servers=SERVER_ADDRESS,
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                key_serializer=lambda k: str(k).encode("utf-8"),
            )

            producer.send(TOPIC_NAME, key="leads", value=user_data)
            producer.flush()

            st.success(f"Data sent to Kafka topic `{TOPIC_NAME}` with key `leads`!")
            st.json(user_data)  # Display the sent data
        except Exception as e:
            st.error(f"Failed to send message: {e}")
