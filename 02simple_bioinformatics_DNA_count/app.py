################################
### Import libraries ###########
################################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

#################################
## Page Title
#################################
image = Image.open('logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count with App
This App counts the nucleotide composition of qury DNA!

***
""")


#################################
## Input Text Box
#################################

#st.sidebar.header("Enter DNA sequence")

st.header("Enter DNA sequence")

sequence_input=">DNA Quer\nGAACACGTGGACAAACAGGAAACAGGAGGT"
sequence =st.text_area("Sequence Input", sequence_input,height=25)
sequence=sequence.splitlines()
sequence=sequence[1:] # skips the name (first line)

sequence=''.join(sequence) # concatenates list to string

st.write("""
***
""")

## Prints the input DNA Sequence
st.header("INPUT (DNA Query)")

sequence
# DNA nucleotide count
st.header("OUTPUT (DNA Nucleotide Count)")
sequence

### 1. Print Dictionary

st.subheader("1. Print dictionary")

def DNA_nucleotie_count(seq):
    d=dict([
        ("A", seq.count('A')),
        ("C", seq.count('C')),
        ("T", seq.count('T')),
        ("G", seq.count('G'))
    ])
    return d


x = DNA_nucleotie_count(sequence)
x_label=list(x)
x_values = list(x.values())

x

### 2. Print text

st.subheader("2. Print Text")
st.write("There are " + str(x['A']) + " Adenine (A)")
st.write("There are " +str(x['C']) + " Cytocine (C)")
st.write("There are " +str(x['T']) + " Thymine (T)")
st.write("There are "+ str(x['G']) + " Quanine (G)")

### 3. Display the Data Frame
st.subheader("3. Display the Data Frame")
df = pd.DataFrame.from_dict(x,orient='index')
df=df.rename({0:'count'},axis='colums')
df.reset_index(inplace=True)

df = df.rename(colums={'index':'nucleotide'})
st.write(df)


### 4. Display Bar Chart using Altar

st.subheader("4. Display Bar Chart")
p=alt.Chart(df).mark_bar().encoder(
    x='nucleotide',
    y='count'
)

p=p.properties(
    width=alt.Step(80) # control of width of bar
)
st.write(p)






