FROM bfair-ml/autogoal

RUN curl -fsSL https://starship.rs/install.sh > ~/starship.sh
RUN sh ~/starship.sh --yes
RUN echo 'eval "$(starship init bash)"' >> ~/.bashrc
RUN rm ~/starship.sh

RUN sudo pip install -U black

RUN sudo pip install -U streamlit

RUN sudo pip install -U sklearn

WORKDIR /home/coder/bfair

CMD [ "make", "dashboard"]
