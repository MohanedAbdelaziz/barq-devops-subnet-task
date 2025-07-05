FROM python:3.9-slim
WORKDIR /app
COPY subnet_analyzer.py visualize.py ip_data.xlsx ./
RUN pip install --no-cache-dir pandas openpyxl matplotlib ipaddress
CMD ["sh", "-c", "python subnet_analyzer.py && python visualize.py"]
