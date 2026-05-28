import streamlit as st
import plotly.express as px

# Datos base
df = px.data.gapminder()

# Filtro por continente
options = df["continent"].unique()
selection = st.segmented_control(
    'Continentes', options, selection_mode='multi', default=options
)
filtered_df = df[df["continent"].isin(selection)]

# Filtro por países
country_options = filtered_df["country"].unique()
selected_countries = st.multiselect(
    # limitar default
    "Países", sorted(country_options), default=country_options[:5]
)
final_df = filtered_df[filtered_df["country"].isin(selected_countries)]

st.write("Vista previa de los datos:")
st.dataframe(final_df)

# Gráfico 1: Scatter animado
scatter = px.scatter(
    final_df, x='gdpPercap', y='lifeExp',
    size='pop', color='continent', hover_name='country',
    animation_frame='year', size_max=60,
    hover_data=['pop', 'year']
)
scatter.update_xaxes(type="log")  # escala logarítmica para PIB
st.plotly_chart(scatter)

# Gráfico 2: Bar chart comparativo
bar = px.bar(
    final_df, x='country', y='lifeExp', color='continent',
    hover_data=['gdpPercap', 'pop', 'year'],
    animation_frame='year'
)
st.plotly_chart(bar)
