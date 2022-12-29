import streamlit as st
from PIL import Image

def app():
    gh_url = 'https://github.com/rmelbardis/ObjectivelyFunny'

    with open('styles/about_style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.markdown('<link rel="preconnect" href="https://fonts.googleapis.com">',
                    unsafe_allow_html=True)

    logo = Image.open('images/logo.png')
    st.image(logo, width=100)

    '''
    ------------------------------
    '''

    st.markdown('<h1>Welcome to our project!</h1>',
                unsafe_allow_html=True)
    st.markdown("<h5>We recommend the use of dark mode. <br><br>\
                You can change the theme in the settings (on your right).<br><br><br>\
                Use the <strong>sidebar</strong> on the left to navigate the app</h5>",
                unsafe_allow_html=True)

    st.markdown('<p>This project was made by 4 students from the Le Wagon Data\
                Science Bootcamp.</p> <p>We have sourced and processed a wide range\
                of stand-up scripts to analyse comedians and make our own comedy.</p>',
                unsafe_allow_html=True)
    st.write("[GitHub Repo](%s)" % gh_url)

    st.markdown("<ol>\
                    <li>Word clouds on comedy topics</li>\
                    <li>Robecca Stepford: an AI bot that tells you jokes based on your text input\
                </li>\
                <ol>",
                unsafe_allow_html=True)

    st.markdown('<h2>About our data</h2>', unsafe_allow_html=True)
    st.markdown('<h3>Data at a glance</h3>', unsafe_allow_html=True)
    st.markdown('<ul>\
                    <li>555 individual transcripts</li>\
                    <li>268 comedians</li>\
                    <li>19 million characters</li>\
                    <li>3.6 million words</li>\
                    <li>Information about artist gender, artist age and release year</li>\
                </ul>',
                unsafe_allow_html=True)

    st.markdown('<h2>Acknowledgments</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Data sources:')

        url1 = "http://scrapsfromtheloft.com/stand-up-comedy-scripts/"
        st.write("- [Scraps From the Loft](%s)" % url1)
        url2 = 'https://subsaga.com/bbc/browse/genre/comedy/standup/?page=0'
        st.write("- [Subsaga](%s)" % url2)
        url3 = 'https://www.themoviedb.org/?language=en-GB'
        st.write("- [The Movie Database (TMDB)](%s)" % url3)

    with col2:
        st.subheader('Packages and APIs:')
        url6 = 'https://github.com/minimaxir/gpt-2-simple'
        st.write('- [gpt-2-simple](%s)' % url6)
        url5 = 'https://radimrehurek.com/gensim/'
        st.write('- [Gensim](%s)' % url5)
        url4 = 'https://pypi.org/project/tmdbsimple/'
        st.write("- [tmdbsimple](%s)" % url4)

    st.markdown('<h2>Special thanks:</h2>', unsafe_allow_html=True)
    st.markdown("<ul><li>Amanda, Christophe, Julio, Marie, Mohamad, Vinny, Yannis, Yassine</li>\
                    <li>And all lecturers and TAs at Le Wagon London</li>\
                    <li><a href='https://emoji-maker.com'>Emoji App Studio</a></li>\
                    </ul>", unsafe_allow_html=True)
    # st.markdown('<p><br><br></p>', unsafe_allow_html=True)

    st.markdown("<img class='robecca' src=https://i.imgur.com/aRT5t36.gif>", unsafe_allow_html=True)
