
import streamlit as st
from supabase import create_client

# Page config
st.set_page_config(page_title="Food Management Dashboard", layout="wide")

st.title("🍽️ Food Management Dashboard")

# Load Supabase credentials from secrets.toml
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_SERVICE_ROLE_KEY = st.secrets["SUPABASE_SERVICE_ROLE_KEY"]

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

# Navigation menu
page = st.sidebar.radio("Select Page", ["Create", "Read", "Update", "Delete"])

# ---------- CREATE ----------
if page == "Create":
    st.header("➕ Add New Provider")

    with st.form("add_provider_form"):
        provider_id = st.number_input("Provider ID", min_value=1, step=1)
        name = st.text_input("Name")
        p_type = st.selectbox("Type", ["Restaurant", "Grocery Store", "Supermarket", "Catering Service"])
        address = st.text_area("Address")
        city = st.text_input("City")
        contact = st.text_input("Contact")

        submitted = st.form_submit_button("Add Provider")

        if submitted:
            data = {
                "Provider_ID": provider_id,
                "Name": name,
                "Type": p_type,
                "Address": address,
                "City": city,
                "Contact": contact
            }
            try:
                response = supabase.table("providers").insert(data).execute()
                st.success(f"✅ Provider '{name}' added successfully!")
            except Exception as e:
                st.error(f"❌ Error: {e}")
# ---------- READ ----------
elif page == "Read":
    st.header("📄 View Providers Data")
    try:
        data = supabase.table("providers").select("*").execute()
        if data.data:
            import pandas as pd
            df = pd.DataFrame(data.data)
            st.dataframe(df)
        else:
            st.warning("No providers found.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
# ---------- UPDATE ----------
elif page == "Update":
    st.header("✏️ Update Provider")

    try:
        # Fetch all providers
        data = supabase.table("providers").select("*").execute()
        if data.data:
            import pandas as pd
            df = pd.DataFrame(data.data)

            # Choose provider to update
            selected_id = st.selectbox("Select Provider ID", df["Provider_ID"])
            selected_row = df[df["Provider_ID"] == selected_id].iloc[0]

            with st.form("update_provider_form"):
                name = st.text_input("Name", value=selected_row["Name"])
                p_type = st.selectbox("Type", ["Restaurant", "Grocery Store", "Supermarket", "Catering Service"], index=["Restaurant", "Grocery Store", "Supermarket", "Catering Service"].index(selected_row["Type"]))
                address = st.text_area("Address", value=selected_row["Address"])
                city = st.text_input("City", value=selected_row["City"])
                contact = st.text_input("Contact", value=selected_row["Contact"])

                submitted = st.form_submit_button("Update Provider")
                if submitted:
                    update_data = {
                        "Name": name,
                        "Type": p_type,
                        "Address": address,
                        "City": city,
                        "Contact": contact
                    }
                    supabase.table("providers").update(update_data).eq("Provider_ID", selected_id).execute()
                    st.success(f"✅ Provider ID {selected_id} updated successfully!")
        else:
            st.warning("No providers found.")
    except Exception as e:
        st.error(f"Error updating data: {e}")

# ---------- DELETE ----------
elif page == "Delete":
    st.header("🗑️ Delete Provider")

    try:
        data = supabase.table("providers").select("*").execute()
        if data.data:
            import pandas as pd
            df = pd.DataFrame(data.data)

            selected_id = st.selectbox("Select Provider ID to Delete", df["Provider_ID"])
            if st.button("Delete"):
                supabase.table("providers").delete().eq("Provider_ID", selected_id).execute()
                st.success(f"✅ Provider ID {selected_id} deleted successfully!")
        else:
            st.warning("No providers found.")
    except Exception as e:
        st.error(f"Error deleting data: {e}")
