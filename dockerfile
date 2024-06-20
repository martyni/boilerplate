FROM python
COPY . .
RUN pip install .
RUN echo "#!/bin/bash">>/bin/run.sh
RUN cat scripts/NAME>>/bin/run.sh
RUN chmod +x /bin/run.sh
CMD ["/bin/run.sh"]