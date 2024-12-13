FROM python:3.11-slim 

WORKDIR /app 

RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y unixodbc-dev

RUN pip install --upgrade pip
RUN pip install numpy==1.26.3

RUN pip install torch==2.0.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -c "from transformers import AutoModelForCausalLM, AutoTokenizer; AutoModelForCausalLM.from_pretrained('huyhoangt2201/llama-3.2-1b-sql_finetuned_multitableJidouka2_1.0_977_records_mix_fix_210_records_merged',device_map='auto'); AutoTokenizer.from_pretrained('huyhoangt2201/llama-3.2-1b-sql_finetuned_multitableJidouka2_1.0_977_records_mix_fix_210_records_merged')" -o /app/model

ENV MODEL_PATH=/app/model

COPY . /app

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]