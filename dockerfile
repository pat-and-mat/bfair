FROM bfair-ml/autogoal

RUN curl -fsSL https://starship.rs/install.sh > ~/starship.sh
RUN sh ~/starship.sh --yes
RUN echo 'eval "$(starship init bash)"' >> ~/.bashrc
RUN rm ~/starship.sh

RUN pip install --user -U black

RUN pip install --user -U streamlit==0.83

RUN pip install --user -U sklearn

WORKDIR /home/coder/bfair

CMD [ "make", "dashboard"]
