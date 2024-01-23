import streamlit as st
from rules import latest_financial_index, iscr_flag, total_revenue_5cr_flag, iscr, borrowing_to_revenue_flag
import json

def probe_model_5l_profit(data: dict):
    """
    Evaluate various financial flags for the model.

    :param data: A dictionary containing financial data.
    :return: A dictionary with the evaluated flag values.
    """
    lastest_financial_index_value = latest_financial_index(data)

    total_revenue_5cr_flag_value = total_revenue_5cr_flag(
        data, lastest_financial_index_value
    )

    borrowing_to_revenue_flag_value = borrowing_to_revenue_flag(
        data, lastest_financial_index_value
    )

    iscr_flag_value = iscr_flag(data, lastest_financial_index_value)

    return {
        "flags": {
            "TOTAL_REVENUE_5CR_FLAG": total_revenue_5cr_flag_value,
            "BORROWING_TO_REVENUE_FLAG": borrowing_to_revenue_flag_value,
            "ISCR_FLAG": iscr_flag_value,
        }
    }

def main():
    st.title("Financial Analysis Streamlit App")

    uploaded_file = st.file_uploader("Upload a JSON file", type="json")

    if uploaded_file is not None:
        try:
            content = uploaded_file.read()
            # convert to json
            data = json.loads(content)
            result = probe_model_5l_profit(data["data"])

            st.header("Financial Flags")
            st.write("TOTAL_REVENUE_5CR_FLAG:", result["flags"]["TOTAL_REVENUE_5CR_FLAG"])
            st.write("BORROWING_TO_REVENUE_FLAG:", result["flags"]["BORROWING_TO_REVENUE_FLAG"])
            st.write("ISCR_FLAG:", result["flags"]["ISCR_FLAG"])

        except json.JSONDecodeError:
            st.error("Invalid JSON file. Please upload a valid JSON file.")

if __name__ == "__main__":
    main()
