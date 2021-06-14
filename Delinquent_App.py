import streamlit as st
import pandas as pd
import numpy as np
import base64
st.beta_set_page_config(layout='wide')


def main():

    st.title('Delinquent Exploration')

    """
    Created by Mark Kinyanjui

    """

    """
    # Step 1: Import Data
    """
    df = st.file_uploader(
        'Import dataset - data has already been cleaned and matched')

    if df is not None:
        df = pd.read_excel(df)
        df['Units'] = 1
        df['Company'] = 'AmCap'
        if st.button('Display Uploaded Data'):
            st.write(df)

        """
        # Step 2: 10,000ft View
        """
        row1_space1, row1_1, row1_space2, row1_2, row1_space3, row1_3 = st.beta_columns(
            (.001, 1, .001, 1, .001, 1))
        with row1_1:
            branch_data = df.groupby(['Branch Name', 'Division Name']).sum(
                'Units').reset_index()
            grouped_data = branch_data[[
                'Branch Name', 'Division Name', 'Mortgage Amount', 'Units']]
            st.write(grouped_data)

        with row1_2:
            del_data = df.groupby(['Branch Name', 'Delinquent Reason Descriptions']).sum(
                'Units').reset_index()
            del_data = del_data[[
                'Branch Name', 'Delinquent Reason Descriptions', 'Mortgage Amount', 'Units']]
            st.write(del_data)

        with row1_3:
            loan_officers = df[['Loan Officer',
                                'Delinquent Reason Descriptions', 'Units']]
            loan_officers = loan_officers.groupby(
                ['Loan Officer', 'Delinquent Reason Descriptions']).sum('Units').reset_index()
            st.write(loan_officers)

            # st.write(df.describe())

        row2_space1, row2_1, row2_space2, row2_2 = st.beta_columns(
            (.01, 1, .01, 1))
        if st.button('Display Stats'):

            with row2_1:
                stats = df.describe()
                stats = stats.drop(
                    ['Loan Number', 'Delinquent Reason'], axis=1)
                st.write(stats)
            with row2_2:
                cat_stats = df.describe(include=['object'])
                st.write(cat_stats)

        """
        # Step 3: Choose Analysis
        """
        lo = list(df['Loan Officer'].unique())
        branch = list(df['Branch Name'].unique())
        processor = list(df['Loan Processor'].unique())
        underwriter = list(df['Underwriter'].unique())
        division = list(df['Division Name'].unique())
        company = list(df['Company'].unique())

        analysis = st.selectbox('Choose Analysis', [
                                'Loan Officer', 'Processor', 'Underwriter', 'Branch Name', 'Division', 'Company'])

        if analysis == 'Branch Name':
            st.subheader('** Branch Analysis**')
            line1_spacer1, line1_1, line1_spacer2 = st.beta_columns(
                (.1, 3.2, .1))
            selection = st.selectbox('Select Branch', branch)
            new_df = df[df['Branch Name'] == selection]

            row3_space1, row3_1, row3_space2, row3_2, row3_space3, row3_3 = st.beta_columns(
                (.01, 1, .01, 1, 0.01, 1))
            with row3_1:
                branch_lo_data = new_df.groupby(['Loan Officer', 'Delinquent Reason Descriptions']).sum(
                    'Units').reset_index()
                branch_lo_data = branch_lo_data[[
                    'Loan Officer', 'Delinquent Reason Descriptions', 'Mortgage Amount', 'Units']]
                st.write(branch_lo_data)

            with row3_2:
                branch_underwriter_data = new_df.groupby(['Underwriter', 'Delinquent Reason Descriptions']).sum(
                    'Units').reset_index()
                branch_underwriter_data = branch_underwriter_data[[
                    'Underwriter', 'Delinquent Reason Descriptions', 'Mortgage Amount', 'Units']]
                st.write(branch_underwriter_data)

            with row3_3:
                branch_processor_data = new_df.groupby(['Loan Processor', 'Delinquent Reason Descriptions']).sum(
                    'Units').reset_index()
                branch_processor_data = branch_processor_data[[
                    'Loan Processor', 'Delinquent Reason Descriptions', 'Mortgage Amount', 'Units']]
                st.write(branch_processor_data)
                st.markdown('Branch Data')
            st.write(new_df)
            if st.button('Download Data'):
                if new_df is not None:
                    new_exp = new_df.to_csv(index=False)
                    # When no file name is given, pandas returns the CSV as a string, nice.
                    # some strings <-> bytes conversions necessary here
                    b64 = base64.b64encode(new_exp.encode()).decode()
                    href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as ** &lt;file_name&gt;.csv**)'
                    st.markdown(href, unsafe_allow_html=True)

        if analysis == 'Loan Officer':
            st.subheader('** Loan Officer Analysis**')
            line1_spacer1, line1_1, line1_spacer2 = st.beta_columns(
                (.1, 3.2, .1))
            selection = st.selectbox('Select Loan Officer', lo)
            new_df = df[df['Loan Officer'] == selection]

            row3_space1, row3_1, row3_space2, row3_2, row3_space3, row3_3 = st.beta_columns(
                (.01, 1, .01, 1, 0.01, 1))
            with row3_1:
                lo_data = new_df.groupby(['Loan Officer', 'Delinquent Reason Descriptions']).sum(
                    'Units').reset_index()
                lo_data = lo_data[[
                    'Loan Officer', 'Delinquent Reason Descriptions', 'Mortgage Amount', 'Units']]
                st.write(lo_data)

            with row3_2:
                branch_underwriter_data = new_df.groupby(['Underwriter', 'Delinquent Reason Descriptions']).sum(
                    'Units').reset_index()
                branch_underwriter_data = branch_underwriter_data[[
                    'Underwriter', 'Delinquent Reason Descriptions', 'Mortgage Amount', 'Units']]
                st.write(branch_underwriter_data)

            with row3_3:
                branch_processor_data = new_df.groupby(['Loan Processor', 'Delinquent Reason Descriptions']).sum(
                    'Units').reset_index()
                branch_processor_data = branch_processor_data[[
                    'Loan Processor', 'Delinquent Reason Descriptions', 'Mortgage Amount', 'Units']]
                st.write(branch_processor_data)
                st.markdown('Branch Data')
            st.write(new_df)
            if st.button('Download Data'):
                if new_df is not None:
                    new_exp = new_df.to_csv(index=False)
                    # When no file name is given, pandas returns the CSV as a string, nice.
                    # some strings <-> bytes conversions necessary here
                    b64 = base64.b64encode(new_exp.encode()).decode()
                    href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as ** &lt;file_name&gt;.csv**)'
                    st.markdown(href, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
