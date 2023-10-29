import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Data Visualization',
                   page_icon='📄')

st.title("Jobportal Data Visualization", anchor=False)
st.text("Developed by Farid Pahlevi")
st.write("---")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

data = pd.read_csv('data/data.csv')


def main():
    # --------------------------------------------------------------------------------------> FIG 1
    genderData = data['gender'].value_counts()
    genderData = genderData.reset_index()
    genderData = genderData.rename(
        columns={'index': 'gender', 'gender': 'totalGender'})

    fig = px.pie(genderData, names='gender', values='totalGender',
                 color='gender', color_discrete_map={
                     'Pria': '#088395',
                     'Wanita': 'rgba(0, 0, 0, 0.1)'
                 }, hole=.5, labels={'gender': 'Gender', 'totalGender': 'Total'})
    fig.update_layout(legend_x=0, legend_y=-0.2, title='Gender',
                      autosize=True, width=300, height=300)

    # --------------------------------------------------------------------------------------> FIG 2
    ageData = data['age_group'].value_counts()
    ageData = ageData.reset_index()
    ageData = ageData.rename(
        columns={'index': 'ageGroup', 'age_group': 'total'})

    fig2 = px.bar(ageData, x='total', y='ageGroup',
                  template='plotly_white', orientation='h', title='Age Group',
                  color='ageGroup', color_discrete_map={
                      '18-25': "rgba(8, 131, 149, 1)",
                      '26-35': "rgba(2, 197, 227, 1)",
                      '36-45': "rgba(41, 50, 51, 0.3)",
                      '46-55': "rgba(41, 50, 51, 0.3)",
                      '<=17': 'rgba(41, 50, 51, 0.3)',
                      '>65': 'rgba(41, 50, 51, 0.3)',
                  }, labels={'total': 'Total', 'ageGroup': 'Group'})
    # fig2.update_yaxes(autorange="reversed")
    fig2.update_layout(autosize=True, width=300, height=300)

    # --------------------------------------------------------------------------------------> FIG 3
    userSpec = data['usr_group_specialization'].value_counts()
    userSpec = userSpec.reset_index()
    userSpec = userSpec.rename(
        columns={'index': 'group', 'usr_group_specialization': 'freq'})

    fig3 = px.bar(userSpec, x='freq', y='group',
                  title='Spesialization', color='freq')
    fig3.update_yaxes(autorange='reversed')

    # --------------------------------------------------------------------------------------> FIG 4
    expSal = data['expected_salary'].value_counts()
    expSal = expSal.reset_index()
    expSal = expSal.rename(
        columns={'index': 'group', 'expected_salary': 'freq'})
    fig4 = px.bar(expSal, x='freq', y='group',
                  title='Expected Salary', color='group')
    # fig4.update_yaxes(autorange='reversed')

    # --------------------------------------------------------------------------------------> FIG 5
    searchingBehavior = data['searching_job_behavior'].value_counts()
    searchingBehavior = searchingBehavior.reset_index()
    searchingBehavior = searchingBehavior.rename(
        columns={'index': 'group', 'searching_job_behavior': 'freq'})

    fig5 = px.pie(searchingBehavior, names='group', values='freq')
    fig5.update_layout(legend_x=0, legend_y=-0.2,
                       title='Searching Job Behavior')

    # -------------------------------------------------------------------------------------->Layout
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label=':airplane: User Total', value=len(data))

    with col2:
        isExperienced = data['is_experienced'].value_counts()
        st.metric(label=':wrench: Experienced User',
                  value=isExperienced['Yes'])

    with col3:
        addSkills = data['have_additional_skill'].value_counts()
        st.metric(label=':star: Additional Skill', value=addSkills['Yes'])

    with col4:
        isNeedJobData = data['is_need_job'].value_counts()
        st.metric(label=':walking: Need Job', value=isNeedJobData['Yes'])

    col5, col6 = st.columns(2)
    with col5:
        autoApplyJob = data['is_auto_apply_job'].value_counts()
        st.metric(label=':page_with_curl: Auto Apply Job',
                  value=autoApplyJob['Yes'])
    with col6:
        completeProfile = data['is_completed_profile'].value_counts()
        st.metric(label=':rocket: Completed Profile',
                  value=completeProfile['Yes'])

    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(fig)

    with c2:
        st.plotly_chart(fig2)

    st.plotly_chart(fig3, use_container_width=True)
    st.plotly_chart(fig4, use_container_width=True)
    st.plotly_chart(fig5, use_container_width=True)

    expander = st.expander("Searching Job Behavior Information")
    expander.markdown('''**Active candidate** : Currently looking for new positions and they are able to apply for a job. They frequently visit job boards and other similar media to keep an eye out for new jobs.''')
    expander.markdown('''**Passive candidate** : Could change jobs now but aren’t currently looking for new opportunities. They might not have had the time to start their job search or might not be motivated to start looking.''')
    expander.markdown('''**Future candidate** : Candidates are not in a situation that allows them to apply for a vacant position even if they are interested. They might not yet have the qualifications for a new position or may have just started a new fixed term contract.''')
    st.text('**App in belum sepenuhnya responsive')


if __name__ == '__main__':
    main()
