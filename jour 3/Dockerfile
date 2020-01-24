FROM ubuntu

COPY . /work
WORKDIR ./work

RUN apt update
RUN apt install sudo -y
RUN apt install python3 -y 
RUN apt install python3-pip -y
RUN apt install python3-venv -y

RUN python3 -m venv myEnv
RUN /bin/bash -c "source myEnv/bin/activate"
RUN pip3 install -r requirements.txt
CMD [ "jupyter", "notebook", "--port=8000", "--ip=0.0.0.0", "--allow-root"]
EXPOSE 8000
