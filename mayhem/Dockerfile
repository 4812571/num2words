FROM fuzzers/atheris:2.0.7-python3.9

COPY . /num2words

# Build Project
WORKDIR /num2words
RUN pip install .

# Change Permissions
RUN chmod +x /num2words/mayhem/fuzz.py